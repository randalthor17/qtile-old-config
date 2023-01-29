#!/bin/sh

keybinding_gen=~/.config/qtile/lib/gen_keybindings.py

env python3 $keybinding_gen | rofi -columns 5 -theme-str '#window { fullscreen: true; font: "FuraCode NF Bold 12"; }' -dmenu -i -mesg "Qtile shortcuts"



