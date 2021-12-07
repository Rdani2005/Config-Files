# libraries
import os
import subprocess
from libqtile import hook
# Data
from settings.groups import groups
from settings.keys import mod, keys
from settings.layouts import layouts, floating_layout
from settings.mouse import mouse
from settings.screens import screens
from settings.widgets import widget_defaults, extension_defaults


# This is very important for me!
# Commands to use when you start the Qtile desktop. See the autostart.sh file
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


# Changing between groups


# trash configs ;)
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
main = None
# Honestly, I love using stremio and youtube on full-screen,
# so this is very important. ;)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
