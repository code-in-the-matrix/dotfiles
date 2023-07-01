#Custom aliases

alias clc='clear'

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# for managing dotfiles
alias config='/usr/bin/git --git-dir=$HOME/Documents/dotfiles --work-tree=$HOME'

#pomodoro timer
#alias pomo25="termdown 25m && feh ~/.config/backgrounds/black_screen_wal.jpg -xFZ"
alias pomo25="termdown 25m && i3lock"

alias docker-compose='docker compose'

#for opening files using their default programs
alias open="xdg-open"


# trash management
alias tr="trash-put"

# Prevent accidental file deletion
#alias rm="trash-put"

#git aliases
alias gst="git status"
alias ga="git add"
alias gc="git commit"
alias gco="git checkout"


# for running gratisnew
alias runudtlocal='docker run -it --rm --name local -p 8081:80 --privileged -v /home/swayam/undostres/gratisnew:/var/www/html udt-local'
alias rungratisnew='docker run --platform=linux/amd64 -it --rm --name udt-gratisnew -p 8081:80 --privileged -v $(PWD):/var/www/html udt-local-gratisnew'

