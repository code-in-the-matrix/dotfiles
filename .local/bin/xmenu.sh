#!/bin/sh
xmenu -i -p 2x24:cursor <<EOF | sh &
Internet
	IMG:./icons/web.png	Firefox	firefox
	IMG:./icons/web.png	Google chrome	google-chrome-stable
Programming
	IMG:./icons/web.png	Terminal	alacritty
	IMG:./icons/web.png	Visual studio code	code
	IMG:./icons/web.png	Ghostwriter	ghostwriter
Office
	IMG:./icons/gimp.png	Libreoffice	libreoffice
	IMG:./icons/gimp.png	Libreoffice spreadsheet	libreoffice	--calc
	IMG:./icons/gimp.png	Libreoffice writer	libreoffice	--writer
	IMG:./icons/gimp.png	Libreoffice presentation	libreoffice	--impress
System
	IMG:./icons/gimp.png	File manager	pcmanfm
Multimedia
	IMG:./icons/gimp.png	Media player	mpv

Help (*)		st
Search (*)		rofi -show drun

Power
	IMG:./icons/gimp.png	Shutdown	poweroff
	IMG:./icons/gimp.png	Reboot	reboot
EOF
