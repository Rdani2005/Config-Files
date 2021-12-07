# libraries
from libqtile.config import Group, key
from libqtile.command import lazy
from .keys import mod, keys

groups = [
    Group(i) for i in [
        "DEV",
        "WEB",
        "GFX",
        "SYS",
        "VBOX",
        "DOC",
        "VIDEOS",
        "CHAT",
        "GAMES"
    ]
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])