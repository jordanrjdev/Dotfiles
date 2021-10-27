#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
# systray wifi-manager
nm-applet &

setxkbmap latam 

brightnessctl s 30%
