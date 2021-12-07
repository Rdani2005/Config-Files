from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import primary_widgets

screens = [
    Screen(top=bar.Bar(primary_widgets, 20, opacity=1.0)),
    Screen(top=bar.Bar(primary_widgets, 20, opacity=1.0))
]
