- [Zsh](#zsh)
  - [Prezto](#prezto)
  - [`.zshrc`](#zshrc)
  - [Nerd Font - Mononoki](#nerd-font---mononoki)
- [`raspi-config`](#raspi-config)
- [`setup.sh`](#setupsh)

## Zsh

```shell
sudo apt install -y zsh zsh-autosuggestion zsh-syntax-highlighting
chsh -s /usr/bin/zsh
```

### Prezto

See. https://github.com/sorin-ionescu/prezto

### `.zshrc`

```.zshrc
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

# Customize to your needs...
# Alias
compdef g=git
compdef mosh=ssh

alias ls="exa -hF --icons"
alias l="exa -haF --icons"
alias la="exa -haF --icons"
alias ll="exa -halF --icons"

function chpwd() {
  exa -halF --git --icons
}
```

### Nerd Font - Mononoki

```shell
mkdir -p ~/.fonts
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Mononoki.zip
unzip Mononoki.zip -d ~/.fonts/
fc-cache -fv
```

## `raspi-config`

Enable SPI and legacy camera.

## `setup.sh`

Execute `./setup.sh` to install dependencies.
