#!/usr/bin/env bash

set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR EXIT

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)

usage() {
  cat << EOF # remove the space between << and EOF, this is due to web plugin issue
Usage: $(basename "${BASH_SOURCE[0]}") [-h] [-v] [-f] -p param_value arg1 [arg2...]

Script description here.

Available options:

-h, --help      Print this help and exit
-v, --verbose   Print script debug info
EOF
  exit
}

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # script cleanup here
}

setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    NOFORMAT='\033[0m' RED='\033[0;31m' GREEN='\033[0;32m' ORANGE='\033[0;33m' BLUE='\033[0;34m' PURPLE='\033[0;35m' CYAN='\033[0;36m' YELLOW='\033[1;33m'
  else
    NOFORMAT='' RED='' GREEN='' ORANGE='' BLUE='' PURPLE='' CYAN='' YELLOW=''
  fi
}

msg() {
  echo >&2 -e "${1-}"
}

ask() {
  echo >&2 -ne "${CYAN}${1-}${NOFORMAT}"
}

die() {
  local msg=$1
  local code=${2-1} # default exit status 1
  msg "$msg"
  exit "$code"
}

parse_params() {
  # default values of variables set from params
  flag=0
  param=''

  while :; do
    case "${1-}" in
    -h | --help) usage ;;
    -v | --verbose) set -x ;;
    --no-color) NO_COLOR=1 ;;
    -?*) die "Unknown option: $1" ;;
    *) break ;;
    esac
    shift
  done

  args=("$@")
  return 0
}

parse_params "$@"
setup_colors

# script logic here

msg "${RED}Read parameters:${NOFORMAT}"
msg "- arguments: ${args[*]-}"

msg "${BLUE}---- Setup Lipo SHIM ----${NOFORMAT}"

ask "Install Lipo SHIM daemon? [Y/n]: "
read LIPO_ANS
case $LIPO_ANS in
  "" | [Yy]*)
    msg "${GREEN}Sure, Start Lipo SHIM daemon installation.${NOFORMAT}"
    curl https://get.pimoroni.com/zerolipo | bash
    ;;
  *)
    msg "${YELLOW}Okay, if you want to install it manually, refer to README.md.${NOFORMAT}"
    ;;
esac

msg "${BLUE}---- Setup 1.3 LCD HAT --${NOFORMAT}"

ask "Install BCM Driver? [Y/n]: "
read ANS_BCM
case $ANS_BCM in
  "" | [Yy]*)
    msg "${GREEN}Sure, Start BCM Driver installation.${NOFORMAT}"
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.71.tar.gz
    tar zxvf bcm2835-1.71.tar.gz
    (cd bcm2835-1.71 && ./configure && sudo make && sudo make check && sudo make install)
    ;;
  *)
    msg "${YELLOW}Okay, if you want to install it manually, refer to README.md.${NOFORMAT}"
    ;;
esac

ask "Install WiringPi libraries? [Y/n]: "
read ANS_WIRINGPI
case $ANS_WIRINGPI in
  "" | [Yy]*)
    msg "${GREEN}Sure, Start wiringPi libraries installation.${NOFORMAT}"
    git clone https://github.com/WiringPi/WiringPi
    (cd WiringPi && ./build)
    gpio -v
    ;;
  *)
    msg "${YELLOW}Okay, if you want to install it manually, refer to README.md.${NOFORMAT}"
    ;;
esac

ask "Install dependencies related to LCD? [Y/n]: "
read ANS_LCD_PYTHON
case $ANS_LCD_PYTHON in
  "" | [Yy]*)
    msg "${GREEN}Sure, Start dependencies related to LCD installation.${NOFORMAT}"
    sudo apt-get update
    sudo apt-get install -y ttf-wqy-zenhei
    sudo apt-get install -y python3-pip
    sudo pip3 install RPi.GPIO
    sudo pip3 install spidev
    ;;
  *)
    msg "${YELLOW}Okay, if you want to install it manually, refer to README.md.${NOFORMAT}"
    ;;
esac

ask "Download LCD examples? [Y/n]: "
read ANS_LCD_EXAMPLES
case $ANS_LCD_EXAMPLES in
  "" | [Yy]*)
    msg "${GREEN}Sure, Start LCD examples download.${NOFORMAT}"
    sudo apt-get install -y p7zip-full
    wget https://www.waveshare.com/w/upload/b/bd/1.3inch_LCD_HAT_code.7z
    7z x 1.3inch_LCD_HAT_code.7z -r -o./1.3inch_LCD_HAT_code
    sudo chmod 777 -R 1.3inch_LCD_HAT_code
    ;;
  *)
    msg "${YELLOW}Okay, if you want to download it manually, refer to README.md.${NOFORMAT}"
    ;;
esac

msg "${BLUE}---- Setup Paperang ----${NOFORMAT}"

ask "Install dependencies related to Paperang? [Y/n]: "
read ANS_PAPERANG
case $ANS_PAPERANG in
  "" | [Yy]*)
    msg "${GREEN}Sure, Start dependencies related to Paperang installation.${NOFORMAT}"
    sudo apt-get update
    sudo apt-get install -y libbluetooth-dev
    sudo apt-get install -y libhidapi-dev
    sudo apt-get install -y libatlas-base-dev
    sudo apt-get install -y python3-llvmlite
    sudo apt-get install -y python3-numba
    sudo apt-get install -y python3-llvmlite
    sudo apt-get install -y llvm-dev
    sudo apt-get install -y python3-pip
    sudo pip3 install cython
    sudo pip3 install numpy
    sudo pip3 install pybluez
    sudo pip3 install scikit-image
    sudo pip3 install scipy
    sudo pip3 install numba
    sudo pip3 install pilkit
    sudo pip3 install watchgod
    ;;
  *)
    msg "${YELLOW}Okay, if you want to install it manually, refer to README.md.${NOFORMAT}"
    ;;
esac

ask "Clone python-paperang? [Y/n]: "
read ANS_PYTHON_PAPERANG
case $ANS_PYTHON_PAPERANG in
  "" | [Yy]*)
    msg "${GREEN}Sure, clone python-paperang.${NOFORMAT}"
    git clone https://github.com/tinyprinter/python-paperang.git
    ;;
  *)
    msg "${YELLOW}Okay, if you want to clone it manually, refer to README.md.${NOFORMAT}"
    ;;
esac

msg "${BLUE}---- Setup OpenCV ----${NOFORMAT}"

ask "Install OpenCV? [Y/n]: "
read ANS_LCD_PYTHON
case $ANS_LCD_PYTHON in
  "" | [Yy]*)
    msg "${GREEN}Sure, Start OpenCV installation.${NOFORMAT}"
    sudo apt-get update
    sudo apt-get install -y python3-opencv
    ;;
  *)
    msg "${YELLOW}Okay, if you want to install it manually, refer to README.md.${NOFORMAT}"
    ;;
esac

msg "${BLUE}All done.${NOFORMAT}"
