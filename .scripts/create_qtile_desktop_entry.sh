#!/bin/sh
sudo tee <<'EOF' /usr/share/xsessions/qtile.Desktop 1> /dev/null
[Desktop Entry
Version=1.0
Name=Qtile Session
Comment=Qtile window manager
Exec=/home/swayam/.local/bin/qtile start
Type=Application
Keywords=tiling;wm;
EOF
