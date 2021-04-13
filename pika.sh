#!/usr/bin/env bash
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 


set -euo pipefail

# Redirect stderr to stdout since tracing/apt-get/dpkg spam it for things that aren't errors.
exec 2>&1
set -x

echo '
┏━┳┳┓╋╋╋┏┓╋╋┏┓           
┃╋┣┫┣┳━┓┃┗┳━┫┗┓ •Deployment started•
┃┏┫┃━┫╋┗┫╋┃╋┃┏┫
┗┛┗┻┻┻━━┻━┻━┻━┛
'
export DEBIAN_FRONTEND=noninteractive
export TZ=Asia/Kolkata
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


apt-get update -y && apt upgrade -y && apt-get install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa -y && apt-get install python3.9 -y 
apt-get install -y --no-install-recommends \
    git \
    coreutils \
    gifsicle \
    apt-utils \
    bash \
    bzip2 \
    imagemagick \
    build-essential \
    cmake \
    curl \
    libmagic-dev \
    imagemagick \
    figlet \
    gcc \
    g++ \
    git \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libgl1 \
    musl \
    postgresql-client-13 \
    openssl \
    mediainfo \
    wget \
    libreadline-dev \
    zipalign \
    sqlite3 \
    ffmpeg \
    libsqlite3-dev \
    axel \
    zlib1g-dev \
    recoverjpeg \
    zip \
    libfreetype6-dev \
    procps \
    policykit-1
apt autoremove --yes

pip3 install --upgrade pip setuptools wheel && git clone -b beta https://github.com/ItzSjDude/PikachuUserbot ./ && mkdir bin && mkdir pikabot/main_plugs && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb   
pip3 install -r requirements.txt



echo '
┏━┳┳┓╋╋╋┏┓╋╋┏┓         
┃╋┣┫┣┳━┓┃┗┳━┫┗┓•Deployment Finished•
┃┏┫┃━┫╋┗┫╋┃╋┃┏┫ Thank You For Deploying 
┗┛┗┻┻┻━━┻━┻━┻━┛      PikachuUserbot 
• Wait While image is being pushed to Heroku
• Turn your Worker on 
If You face any difficulties then contact @ItzSjDude 
at @PikaUserbot_Support
'
