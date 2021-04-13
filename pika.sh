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
export PYTHON_VERSION=3.10.0a7
export PYTHON_PIP_VERSION=21.0.1
export PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/29f37dbe6b3842ccd52d61816a3044173962ebeb/public/get-pip.py
export PYTHON_GET_PIP_SHA256=e03eb8a33d3b441ff484c56a436ff10680479d4bd14e59268e67977ed40904de

ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

apt-get update -y && apt-get install software-properties-common && add-apt-repository ppa:deadsnakes/ppa -y && apt install python3.9
apt-get install -y --no-install-recommends \
    coreutils \
    gifsicle \
    apt-utils \
    python3-pip \
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
