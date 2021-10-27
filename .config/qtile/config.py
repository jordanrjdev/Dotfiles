from libqtile import hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path
import os 
from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'

cmd = [
    "setxkbmap latam",
    "feh --bg-fill /home/jordandev/Documents/Wallpapers/17.jpg", 
    "picom --no-vsync &"
]

for x in cmd: 
    os.system(x)

