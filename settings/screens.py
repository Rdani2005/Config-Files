from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import primary_widgets


def my_bar(widgets):
    return bar.Bar(widgets, 20, opacity=1.0)


screens = [
    Screen(top=my_bar(primary_widgets)),
    Screen(top=my_bar(primary_widgets))
]
