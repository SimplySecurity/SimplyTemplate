#!/bin/bash

# Current supported platforms: 
#   Kali-Linux
# Global Variables
runuser=$(whoami)
tempdir=$(pwd)

# Title Function
func_title(){
  # Clear (For Prettyness)
  clear

  # Echo Title
  echo '=========================================================================='
  echo ' SimpleTemplate Setup Script | [Updated]: '
  echo '=========================================================================='
  echo ' [Web]: Http://CyberSyndicates.com | [Twitter]: @KillSwitch-GUI'
  echo '=========================================================================='
}



# Environment Checks
func_check_env(){
  # Check Sudo Dependency going to need that!
  if [ $(which sudo|wc -l) -eq '0' ]; then
    echo
    echo ' [ERROR]: This Setup Script Requires sudo!'
    echo '          Please Install sudo Then Run This Setup Again.'
    echo
    exit 1
  fi
}

func_install_requests(){
  echo ' [*] Installing and updating requests libary'
  #Insure we have the latest requests module in python
  #sudo apt-get -q update
  #sudo apt-get -q upgrade 
  sudo git pull 
  sudo easy_install pip
  sudo apt-get -y install icedove 
  sudo apt-get -y install w3m 
  sudo apt-get install iceweasel -y 
  sudo apt-get install python python-tk idle python-pmw python-imaging -y
  # we need to check for front end for this install
  cd /tmp/
  sudo wget http://www.unmht.org/unmht/files/unmht-8.1.0.xpi 
  sudo whiptail --msgbox "Please Hit (Install Now) & Please Close Iceweasel!" 10 40 
  iceweasel unmht-8.1.0.xpi &&
  sudo pip install glob2 --upgrade
  sudo pip install configparser --upgrade
  sudo chmod +x SimplyTemplate.py
  sudo rm /tmp/unmht-8.1.0.xpi
}


# Menu Case Statement
case $1 in
  *)
  func_title
  func_check_env
  func_install_requests
  ;;

esac
