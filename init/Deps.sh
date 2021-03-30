#!/bin/bash
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 
#
# © @ItzSjdude, Made for Pikabot

_logo() {
    echo '
    ╔═╦╦╗───╔╗──╔╗
    ║╬╠╣╠╦═╗║╚╦═╣╚╗
    ║╔╣║═╣╬╚╣╬║╬║╔╣
    ╚╝╚╩╩╩══╩═╩═╩═╝
    '
}

_CleanUp() {
    echo 'Cleanup : Cleaning old source'
    rm -rf ./plugins && rm -rf ./* && rm -rf ./.gitignore && rm -rf ./.git
} 

_UpSource() {
    echo 'Github: Updating PikaBot With ItzSjDude/PikachuUserbot' 
    git clone -b beta https://github.com/ItzSjDude/PikachuUserbot ./ &> /dev/null
    mkdir ./plugins
    git clone https://github.com/ItzSjDude/PikaBotPlugins ./Temp &> /dev/null
    cp ./Temp/plugins/*.py ./plugins && cp ./Temp/plugins/resources/*.py ./pikabot
    rm -rf ./Temp
}

_Upchrome() {
    echo 'Chrome: Setting up Chrome configurations:' 
    chmod +x ./pikabot/Chrome/chromedriver && mv -f ./pikabot/Chrome/chromedriver /usr/bin/ &> /dev/null
}
_upptg() {
    pip3 install rejson
    pip3 install PikaTgBot==1.4.0
}

StartUp() {
    _logo
    _CleanUp
    _UpSource
    _Upchrome
    _upptg
    mkdir ./pikabot/main_plugs
    python3 -m PikaTgBot
}
