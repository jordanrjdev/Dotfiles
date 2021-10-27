set fish_greeting ""

# Aliases

alias grep "grep --color=auto"
alias cat "bat --style=plain --paging=never"
alias tree "exa -T"
alias dotfiles "git --git-dir $HOME/.dotfiles/ --work-tree $HOME"

# Prompt

starship init fish | source
