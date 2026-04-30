import json
import os

SETTINGS_FILE    = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

# ===================== НАСТРОЙКИ =====================
DEFAULT_SETTINGS = {
    "sound":       False,
    "difficulty":  "normal",   # easy | normal | hard
    "car_color":   "default",  # default | red | blue | yellow
}

def load_settings() -> dict:
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE) as f:
                data = json.load(f)
                # merge with defaults for missing keys
                return {**DEFAULT_SETTINGS, **data}
        except Exception:
            pass
    return dict(DEFAULT_SETTINGS)

def save_settings(s: dict):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(s, f, indent=4)


# ===================== ЛИДЕРБОРД =====================
def load_leaderboard() -> list:
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE) as f:
                return json.load(f)
        except Exception:
            pass
    return []

def save_leaderboard(entries: list):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(entries, f, indent=4)

def add_entry(name: str, score: int, distance: int, coins: int):
    """Добавляет результат и сохраняет Top 10."""
    entries = load_leaderboard()
    entries.append({
        "name":     name,
        "score":    score,
        "distance": distance,
        "coins":    coins,
    })
    entries.sort(key=lambda e: e["score"], reverse=True)
    entries = entries[:10]
    save_leaderboard(entries)
    return entries