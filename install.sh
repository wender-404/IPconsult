#!/bin/bash

# version: 0.1
# author: Dreifus-404 <aslapoha03@gmail.com>
# Este programa faz as instalações necessarias para o funcionamento do codigo

echo -e "\e[32m installing packages wait a moment\e[0m..."
apt-get install python -y > /dev/null

python -m pip install --upgrade pip
python -m pip install flake8 pytest
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
