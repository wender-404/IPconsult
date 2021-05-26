#!/bin/bash

# version: 0.1
# author: Dreifus-404 <https://github.com/Dreifus-404/>
# Este programa faz as instalações necessarias para o funcionamento do codigo

clear; echo -e "\e[32minstalling\e[0m..."

apt-get update > /dev/null && apt-get upgrade -y > /dev/null
apt-get install python -y > /dev/null

pip install requests > /dev/null
pip install wget > /dev/null

python consult.py
