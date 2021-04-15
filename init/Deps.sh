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
    git clone -b Beta https://github.com/ItzSjDude/PikaBotPlugins ./Temp &> /dev/null
    mkdir ./plugins
    cp ./Temp/plugins/*.py ./plugins
    rm -rf ./Temp
}

StartUp() {
    _logo
    _CleanUp
    _UpSource
    python3 -m pikabot
}

