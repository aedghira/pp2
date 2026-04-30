import psycopg2
from config import DB_CONFIG

# ===================== ПОДКЛЮЧЕНИЕ =====================
def get_conn():
    return psycopg2.connect(**DB_CONFIG)


# ===================== СОЗДАНИЕ ТАБЛИЦ =====================
def init_db():
    """Создаёт таблицы если их нет."""
    sql = """
    CREATE TABLE IF NOT EXISTS players (
        id       SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS game_sessions (
        id            SERIAL PRIMARY KEY,
        player_id     INTEGER REFERENCES players(id),
        score         INTEGER   NOT NULL,
        level_reached INTEGER   NOT NULL,
        played_at     TIMESTAMP DEFAULT NOW()
    );
    """
    try:
        conn = get_conn()
        cur  = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"[DB] init_db error: {e}")
        return False


# ===================== ИГРОК =====================
def get_or_create_player(username: str) -> int | None:
    """Возвращает id игрока. Создаёт если нет."""
    try:
        conn = get_conn()
        cur  = conn.cursor()
        cur.execute("SELECT id FROM players WHERE username = %s", (username,))
        row = cur.fetchone()
        if row:
            pid = row[0]
        else:
            cur.execute(
                "INSERT INTO players (username) VALUES (%s) RETURNING id",
                (username,)
            )
            pid = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return pid
    except Exception as e:
        print(f"[DB] get_or_create_player error: {e}")
        return None


# ===================== СОХРАНИТЬ РЕЗУЛЬТАТ =====================
def save_session(player_id: int, score: int, level: int):
    try:
        conn = get_conn()
        cur  = conn.cursor()
        cur.execute(
            "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s,%s,%s)",
            (player_id, score, level)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[DB] save_session error: {e}")


# ===================== ЛИЧНЫЙ РЕКОРД =====================
def get_personal_best(player_id: int) -> int:
    try:
        conn = get_conn()
        cur  = conn.cursor()
        cur.execute(
            "SELECT COALESCE(MAX(score), 0) FROM game_sessions WHERE player_id = %s",
            (player_id,)
        )
        best = cur.fetchone()[0]
        cur.close()
        conn.close()
        return best
    except Exception as e:
        print(f"[DB] get_personal_best error: {e}")
        return 0


# ===================== ТАБЛИЦА ЛИДЕРОВ =====================
def get_leaderboard(limit: int = 10) -> list[dict]:
    """Возвращает Top N: rank, username, score, level, date."""
    try:
        conn = get_conn()
        cur  = conn.cursor()
        cur.execute("""
            SELECT p.username, gs.score, gs.level_reached,
                   TO_CHAR(gs.played_at, 'DD.MM.YY HH24:MI')
            FROM game_sessions gs
            JOIN players p ON p.id = gs.player_id
            ORDER BY gs.score DESC
            LIMIT %s
        """, (limit,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for i, (username, score, level, date) in enumerate(rows, 1):
            result.append({
                "rank":  i,
                "name":  username,
                "score": score,
                "level": level,
                "date":  date,
            })
        return result
    except Exception as e:
        print(f"[DB] get_leaderboard error: {e}")
        return []