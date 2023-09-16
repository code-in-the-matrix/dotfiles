#!/bin/sh
sudo pacman -Syu
sudo pacman -S gvim git pcmanfm curl wget
sudo pacman -S firefox
#sudo pacman -S python 
sudo pacman -S python-psutil
sudo pacman -S neofetch
sudo pacman -S xorg xorg-xinit 
sudo pacman -S alacritty
sudo pacman -S xf86-video-amdgpu
sudo pacman -S amd-ucode
#sudo pacman -S xf86-video-intel
sudo pacman -S qtile
sudo pacman -S rofi
sudo pacman -S sxhkd
sudo pacman -S fzf mpv keepassxc light
sudo pacman -S alsa-utils pulseaudio pavucontrol
sudo pacman -S udisks2 udiskie
sudo pacman -S network-manager-applet
#sudo pacman -S libreoffice-freuh
sudo pacman -S obsidian
sudo pacman -S perl-rename
sudo pacman -S nodejs npm
sudo pacman -S zathura zathura-pdf-poppler
sudo pacman -S trash-cli

#sudo pacman -Ss jdk
sudo pacman -S jdk11-openjdk

echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk" >> ~/.bashrc
echo "change JAVA_HOME path variable if required\n"


echo "installing docker\n"
sudo pacman -S docker
sudo pacman -S docker-compose

#sudo systemctl start docker
sudo groupadd docker
sudo usermod -aG docker $USER
#newgrp docker

sudo pacman -S lxappearance

sudo pacman -S dosfstools
sudo pacman -S gparted

sudo pacman -S cronie
sudo systemctl enable cronie
sudo systemctl start cronie





sudo pacman -S texlive-basic
sudo pacman -S texlive-latex
sudo pacman -S texlive-latexextra
sudo pacman -S texlive-latexrecommended
sudo pacman -S texlive-plaingeneric
sudo pacman -S texlive-bibextra
sudo pacman -S texlive-xetex
sudo pacman -S texlive-mathscience


sudo pacman -S dosfstools
sudo pacman -S mtools


sudo pacman -S net-tools

sudo pacman -S linux-firmware-qlogic
sudo pacman -S ninja cmake

