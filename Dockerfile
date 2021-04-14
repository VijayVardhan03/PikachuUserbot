#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

FROM ubuntu:latest
COPY pika.sh /tmp/pika.sh
RUN /tmp/pika.sh && chmod +x /usr/local/bin/* 
WORKDIR root/ItzSjDude
RUN git clone -b beta https://github.com/ItzSjDude/PikachuUserbot . 
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash", "startpika"]
