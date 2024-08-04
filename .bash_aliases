# drop the caches
alias freemem='sudo /sbin/sysctl -w vm.drop_caches=3'
    
# MODIFIED COMMANDS
alias ..='cd ..'
alias df='df -h'
alias diff='colordiff'              # requires colordiff package
alias du='du -c -h'
alias free='free -m'                # show sizes in MB
alias grep='grep --color=auto'
alias grep='grep --color=tty -d skip'
alias mkdir='mkdir -p -v'
alias more='less'                   # less is more ;)
alias nano='nano -w'
alias ping='ping -c 5'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias a='./a.out';
alias open='gnome-open'; # open files with appropriate program from terminal
alias p='python';
alias v='vim';
alias mv='mv -i' # asks if accidentally replacing

#  alias in bash to convert bytes into mb
alias bytes_to_mb='awk "{printf \"%.2f MB\n\", \$1 / (1024 * 1024)}"'

alias mybeep='aplay /usr/share/sounds/speech-dispatcher/test.wav 2>/dev/null'
alias dr='docker'
