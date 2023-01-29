# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# from libqtile import bar, layout, widget
# from libqtile.config import Click, Drag, Group, Key, Match, Screen
# from libqtile.lazy import lazy
import os, subprocess
from libqtile import hook
from libqtile.utils import guess_terminal
from lib import keys, layout, mouse, screens, groups

mod = "mod4"
terminal = guess_terminal()


@hook.subscribe.startup_once
def autostart():
    autostart_script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.Popen([autostart_script])


group_Obj = groups.groupObject()
groups = group_Obj.groups

key_Obj = keys.keyObject(mod, terminal)
keys = key_Obj.keys

mouse = mouse.gen_mouse_keys(mod)

layout_Obj = layout.layoutObject()
layouts = layout_Obj.layout

widget_defaults = dict(font="Iosevka Custom", fontsize=12, padding=2)
extension_defaults = widget_defaults.copy()


wallpaper = "~/.local/share/wallpapers/wallpaper.jpg"
wallpaper_mode = "fill"

screen_Obj = screens.screenObject(widget_defaults, wallpaper, wallpaper_mode)
screens = screen_Obj.screens

# Drag floating layouts.

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
# wmname = "LG3D"
wmname = "qtile"
