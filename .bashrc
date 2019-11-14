# Run .aliases
test -r ~/.aliases && source ~/.aliases 

export CLICOLOR_FORCE=1  # force ls to give colored output, even for pipelines

# made a list of directories I will never use, and screen them out by default
# when using my 'go' function 
export APPLE_DIRS="Admin|Library|Applications|Movies|Music|Pictures|Public"

# run our custom function definitions
test -r ~/.functions && source ~/.functions

# If we have a currentTicket file, run it to set $X to our ticket directory
test -r "$HOME/.currentTicket" && . "$HOME/.currentTicket"

# Colors
. ~/bin/bash_colors.sh 

# Set prompt to green time, red relative path, percent sign
PS1="\[$Green\][\t] \[$Red\]\w %\[$Color_Off\]"

addPath $HOME/bin
addPath /usr/local/opt/go/libexec/bin

# set up path to my postgres databases
PGDATA=~/postgres
