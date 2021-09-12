#!/bin/bash

# Authors     : Dreifus-404 <github.com/Dreifus-404>  |  Sysb1n <github.com/sidneypepo>
# Description : this code install necessary packages of program

function installing_packages {
    cd $PREFIX/bin

    if [ -x python ]; then
        echo -e "Package : Python is \e[32mInstalled!\e[0m."

    else
        echo -e "Package : Python \e[40;31mnot installed\e[0m\a\a"; sleep 5
        echo -e "installing package..."

        apt-get install python -y > /dev/null
        cd ~/IPconsult/
        ./install.sh
    fi
}

function installing_importations {
    cd ~/IPconsult/

    if [ -x requeriments.txt ]; then pip install -r requirements.txt; fi

    if [ $? != 0 ]; then
        clear
        echo "erro, verify your connection!."

    else
        clear
        echo "installed packages of importation!."
    fi

}

installing_packages
installing_importations
