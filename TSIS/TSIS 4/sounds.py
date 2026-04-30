import pygame
import numpy as np

pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

SAMPLE_RATE = 44100


def _make_sound(freq: float, duration: float, wave="sine", volume=0.3) -> pygame.mixer.Sound:
    """Генерирует звук по параметрам."""
    frames = int(SAMPLE_RATE * duration)
    t = np.linspace(0, duration, frames, endpoint=False)

    if wave == "sine":
        arr = np.sin(2 * np.pi * freq * t)
    elif wave == "square":
        arr = np.sign(np.sin(2 * np.pi * freq * t))
    elif wave == "sawtooth":
        arr = 2 * (t * freq - np.floor(t * freq + 0.5))
    else:
        arr = np.sin(2 * np.pi * freq * t)

    # затухание
    fade = np.linspace(1.0, 0.0, frames)
    arr  = arr * fade * volume

    arr = (arr * 32767).astype(np.int16)
    sound = pygame.sndarray.make_sound(arr)
    return sound


def _make_sweep(freq_start, freq_end, duration, volume=0.3) -> pygame.mixer.Sound:
    """Звук с изменением частоты (sweep)."""
    frames = int(SAMPLE_RATE * duration)
    t      = np.linspace(0, duration, frames, endpoint=False)
    freqs  = np.linspace(freq_start, freq_end, frames)
    phase  = np.cumsum(2 * np.pi * freqs / SAMPLE_RATE)
    arr    = np.sin(phase)
    fade   = np.linspace(1.0, 0.0, frames)
    arr    = arr * fade * volume
    arr    = (arr * 32767).astype(np.int16)
    return pygame.sndarray.make_sound(arr)


def _make_chord(freqs: list, duration: float, volume=0.25) -> pygame.mixer.Sound:
    """Аккорд из нескольких частот."""
    frames = int(SAMPLE_RATE * duration)
    t      = np.linspace(0, duration, frames, endpoint=False)
    arr    = sum(np.sin(2 * np.pi * f * t) for f in freqs) / len(freqs)
    fade   = np.linspace(1.0, 0.0, frames)
    arr    = arr * fade * volume
    arr    = (arr * 32767).astype(np.int16)
    return pygame.sndarray.make_sound(arr)


# ===================== ЗВУКИ =====================
# Съедание обычной еды — короткий приятный пик
EAT       = _make_sound(660,  0.08, wave="sine",     volume=0.35)

# Яд — низкий неприятный звук
POISON    = _make_sweep(300,  80,   0.4,             volume=0.4)

# Powerup — восходящий sweep
POWERUP   = _make_sweep(400,  900,  0.25,            volume=0.35)

# Повышение уровня — аккорд
LEVELUP   = _make_chord([523, 659, 784], 0.4,        volume=0.3)

# Game Over — нисходящий sweep
GAMEOVER  = _make_sweep(440,  60,   0.8,             volume=0.5)

# Щит активирован — двойной пик
SHIELD    = _make_chord([440, 880], 0.15,            volume=0.3)


# ===================== API =====================
_enabled = True


def set_enabled(val: bool):
    global _enabled
    _enabled = val


def play(sound: pygame.mixer.Sound):
    if _enabled:
        sound.play()


def eat():      play(EAT)
def poison():   play(POISON)
def powerup():  play(POWERUP)
def levelup():  play(LEVELUP)
def gameover(): play(GAMEOVER)
def shield():   play(SHIELD)