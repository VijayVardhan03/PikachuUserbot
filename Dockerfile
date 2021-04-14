#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

FROM python:3.9-slim-buster
WORKDIR root/ItzSjDude
ENV PIP_NO_CACHE_DIR 1
RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list
RUN apt -qq update
RUN apt -qq install -y --no-install-recommends \
    curl \
    git \
    gnupg2 \
    unzip \
    wget

RUN apt -qq update
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# install required packages
RUN apt -qq install -y --no-install-recommends \
    build-essential \
    coreutils \
    jq \
    pv \
    gcc \
    ffmpeg \
    mediainfo \
    unzip \
    zip \
    megatools && \
    rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp


COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python", "-m", "pikabot"]
