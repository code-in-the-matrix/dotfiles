#!/bin/sh
nm-applet &

# xrandr --addmode HDMI-1 1920x1080 && xrandr --output HDMI-1 --primary --mode 1920x1080 --output eDP-1 --mode 1920x1080 --right-of HDMI-1 &

/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &
sct 3300 &
# synclient HorizTwoFingerScroll=1 HorizScrollDelta=-79 &
light -S 15 &
compton &
# volumeicon &

# setting wallpapers
#nitrogen --restore &
/home/swayam/.local/bin/random-wallpaper &

/home/swayam/.local/bin/mon-hdmi &


