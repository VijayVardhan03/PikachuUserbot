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

echo '
┏━┳┳┓╋╋╋┏┓╋╋┏┓           
┃╋┣┫┣┳━┓┃┗┳━┫┗┓ •Deployment started•
┃┏┫┃━┫╋┗┫╋┃╋┃┏┫
┗┛┗┻┻┻━━┻━┻━┻━┛
'
apt -qq update -y

apt -qq install -y --no-install-recommends gnupg

cat >>/etc/apt/sources.list <<EOF
deb http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main
EOF

apt-key add - <<'PGDG_ACCC4CF8'
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=DA1T
-----END PGP PUBLIC KEY BLOCK-----
PGDG_ACCC4CF8

apt -qq update -y 
apt -qq install -y --no-install-recommends \
    gifsicle \
    bzip2 \
    curl \
    git \
    postgresql-client-13 \
    mediainfo \
    wget \
    ffmpeg \

pip3 install –upgrade pip && git clone -b beta https://github.com/ItzSjDude/PikachuUserbot ./ && mkdir bin && mkdir pikabot/main_plugs && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb   
pip3 install --no-cache-dir -r requirements.txt



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
