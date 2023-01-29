#!/bin/sh
numlockx on &
lxsession -e qtile -s qtile &
ln -sf {app/com.discordapp.Discord,$XDG_RUNTIME_DIR}/discord-ipc-0 &
pcmanfm-qt -d &
udiskie -s -f pcmanfm-qt &
xrandr --auto &
playerctld daemon &
secret-tool lookup name keepass | keepassxc --pw-stdin ~/.local/share/keepassxc/Passwords.kdbx &
flameshot &
# picom --experimental-backends &
xss-lock --transfer-sleep-lock -- i3lock-fancy-rapid 5 3 --nofork --ind-pos="x+86:y+950" --radius 20 -k --time-pos="x+200:y+950" --date-pos="x+190:y+970" --time-color=ffffffff --date-color=ffffffff &
