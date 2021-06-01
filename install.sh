#!/bin/bash

# version: 0.1
# author: Dreifus-404 <aslapoha03@gmail.com>
# Este programa faz as instalações necessarias para o funcionamento do codigo

clear; echo -e "\e[32m installing packages wait a moment\e[0m..."

apt-get install python -y > /dev/null
pip install -r requirements.txt

python consult.py
