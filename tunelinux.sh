#!/usr/bin/env bash
# performance tweaks for linux 

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# disables swapping to disk unless RAM is 95% full
echo 'vm.swappiness = 5' >> /etc/sysctl.conf
# or if you want to test it first
# sudo bash -c "echo 'vm.swappiness = 5' >> /etc/sysctl.conf"
