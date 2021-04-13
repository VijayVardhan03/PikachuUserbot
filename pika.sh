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


echo '
┏━┳┳┓╋╋╋┏┓╋╋┏┓           
┃╋┣┫┣┳━┓┃┗┳━┫┗┓ •Deployment started•
┃┏┫┃━┫╋┗┫╋┃╋┃┏┫
┗┛┗┻┻┻━━┻━┻━┻━┛
'
export DEBIAN_FRONTEND=noninteractive
export TZ=Asia/Kolkata
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

apt-get update -y && apt-get install software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt install python3.9
apt-get install -y --no-install-recommends \
    coreutils \
    gifsicle \
    apt-utils \
    python3.9 \
    python3.9-pip \
    python3.9-setuptools \
    bash \
    bzip2 \
    imagemagick \
    build-essential \
    cmake \
    curl \
    libmagic-dev \
    tesseract-ocr \
    tesseract-ocr-eng \
    imagemagick \
    figlet \
    gcc \
    g++ \
    git \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libsqlite3-dev \
    libwebp-dev \
    libgl1 \
    musl \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
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

git clone -b beta https://github.com/ItzSjDude/PikachuUserbot ./ && mkdir bin && mkdir pikabot/main_plugs && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb   
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
