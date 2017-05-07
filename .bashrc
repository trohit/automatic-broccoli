# top 10 commands
top10() { history | awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}' | sort -rn | head; }

# emulate mac commands on linux
alias pbcopy='xsel --clipboard --input'
alias pbpaste='xsel --clipboard --output'

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options 
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# to print the external facing ip address
function extip () { lynx --dump http://ipecho.net/plain; }


# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias a='./a.out';
alias open='gnome-open'; # open files with appropriate program from terminal
alias p='python';
alias v='vim';
alias mv='mv -i' # asks if accidentally replacing


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
