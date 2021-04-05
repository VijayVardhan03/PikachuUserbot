#!/usr/bin/env python3
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
#
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved

from sqlalchemy import *
import os
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
_get = os.environ.get

# the secret configuration specific things


def start() -> scoped_session:
    engine = create_engine(_get("DATABASE_URL"))
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()


class Pdb(BASE):
    __tablename__ = "pdb"
    pika = Column(String(14), primary_key=True)
    var = Column(String(14))
    value = Column(UnicodeText)

    def __init__(self, pika, var, value):
        self.pika = str(pika)
        self.var = str(var)
        self.value = value


class BotUsers(BASE):
    __tablename__ = "botusers"
    pika_id = Column(String(14))

    def __init__(self, pika_id):
        self.pika_id = pika_id


class PikaChats(BASE):
    __tablename__ = "PikaTg"
    pika_id = Column(String(14))

    def __init__(self, pika_id):
        self.pika_id = pika_id


class GMute(BASE):
    __tablename__ = "gmute"
    pika = Column(String(14), primary_key=True)
    sender = Column(String(14))

    def __init__(self, pika, sender):
        self.pika = str(pika)
        self.sender = str(sender)


class GBan(BASE):
    __tablename__ = "gban"
    pika = Column(String(14), primary_key=True)
    sender = Column(String(14))
    reason = Column(UnicodeText)

    def __init__(self, pika, sender, reason=""):
        self.pika = str(pika)
        self.sender = str(sender)
        self.reason = reason


class Mute(BASE):
    __tablename__ = "mute"
    pika = Column(String(14), primary_key=True)
    sender = Column(String(14))
    chat_id = Column(String(14))
    

    def __init__(self, pika, sender, chat_id):
        self.pika = str(pika)
        self.sender = str(sender)
        self.chat_id = str(chat_id)
        


class Notes(BASE):
    __tablename__ = "notes"
    pika = Column(String(14), primary_key=True)
    chat_id = Column(String(14))
    keyword = Column(UnicodeText)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)
    
    def __init__(self, pika, chat_id, keyword, reply, f_mesg_id):
        self.pika = str(pika)
        self.chat_id = str(chat_id)
        self.keyword = keyword
        self.reply = reply
        self.f_mesg_id = f_mesg_id
        self.client_id = client_id


class PMPermit(BASE):
    __tablename__ = "pmpermit"
    pika = Column(String(14), primary_key=True)
    chat_id = Column(String(14))
    reason = Column(String(127))

    def __init__(self, pika, chat_id, reason=""):
        self.pika = str(pika)
        self.chat_id = chat_id
        self.reason = reason
        


class Welcome(BASE):
    __tablename__ = "welcome"
    pika = Column(String(14), primary_key=True)
    chat_id = Column(String(14))
    cust_wc = Column(UnicodeText)
    cl_wc = Column(Boolean, default=False)
    prev_wc = Column(BigInteger)
    mf_id = Column(UnicodeText)

    def __init__(self, pika, chat_id, cust_wc, cl_wc, prev_wc, mf_id=None):
        self.pika = str(pika)
        self.chat_id = chat_id
        self.cust_wc = cust_wc
        self.cl_wc = cl_wc
        self.prev_wc = prev_wc
        self.mf_id = mf_id


Pdb.__table__.create(checkfirst=True)
Mute.__table__.create(checkfirst=True)
BotUsers.__table__.create(checkfirst=True)
PikaChats.__table__.create(checkfirst=True)
GMute.__table__.create(checkfirst=True)
GBan.__table__.create(checkfirst=True)
Notes.__table__.create(checkfirst=True)
PMPermit.__table__.create(checkfirst=True)
Welcome.__table__.create(checkfirst=True)


def pget(pika, var):
    try:
        return SESSION.query(Pdb).filter(
            Pdb.pika == str(pika),
            Pdb.var == str(var)).first().value
    except BaseException:
        return None
    finally:
        SESSION.close()


def pset(pika, var, value):
    if SESSION.query(Pdb).filter(
            Pdb.pika == str(pika),
            Pdb.var == str(var)).one_or_none():
        pdel(pika, var)
    adder = Pdb(str(pika), str(var), value)
    SESSION.add(adder)
    SESSION.commit()


def pdel(pika, var):
    rem = SESSION.query(Pdb).filter(
        Pdb.pika == str(pika),
        Pdb.var == str(var)).delete(
        synchronize_session="fetch")
    if rem:
        SESSION.commit()


def add_welcome(pika, chat_id, cust_wc, cl_wc, prev_wc, mf_id):
    add_wc = Welcome(pika, chat_id, cust_wc, cl_wc, prev_wc, mf_id)
    SESSION.add(add_wc)
    SESSION.commit()


def remove_welcome(pika, chat_id):
    rm_wc = SESSION.query(Welcome).get((str(pika), str(chat_id)))
    if rm_wc:
        SESSION.delete(rm_wc)
        SESSION.commit()


def upd_prev_welcome(pika, chat_id, prev_wc):
    _update = SESSION.query(Welcome).get((str(pika), str(chat_id)))
    _update.prev_wc = prev_wc
    SESSION.commit()


def get_welcome(pika, chat_id):
    try:
        return SESSION.query(Welcome).get((str(pika), str(chat_id)))
    except Exception as e:
        pikalog.error(str(e))
        return
    finally:
        SESSION.close()


def clean_welcome(pika, chat_id, cl_wc):
    clnn = SESSION.query(Welcome).get((str(pika), str(chat_id)))
    clnn.cl_wc = cl_wc
    SESSION.commit()


def approve(pika, chat_id, reason):
    adder = PMPermit(str(pika), str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def disapprove(pika, chat_id):
    rem = SESSION.query(PMPermit).get((str(pika), str(chat_id)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_approved(pika):
    rem = SESSION.query(PMPermit).filter(PMPermit.pika == pika).all()
    SESSION.close()
    return rem


def is_approved(pika, chat_id):
    try:
        return SESSION.query(PMPermit).filter(
            PMPermit.pika == str(pika),
            PMPermit.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_note(pika, chat_id, keyword):
    try:
        return SESSION.query(Notes).get((str(pika), str(chat_id), keyword))
    finally:
        SESSION.close()


def get_notes(pika, chat_id):
    try:
        return SESSION.query(Notes).filter(
            Notes.pika == str(pika),
            Notes.chat_id == str(chat_id)).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_note(pika, chat_id, keyword, reply, f_mesg_id):
    to_check = get_note(pika, chat_id, keyword)
    if not to_check:
        adder = Notes(str(pika), str(chat_id), keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    else:
        rem = SESSION.query(Notes).get((str(pika), str(chat_id), keyword))
        SESSION.delete(rem)
        SESSION.commit()
        adder = Notes(str(pika), str(chat_id), keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return False


def rm_note(pika, chat_id, keyword):
    to_check = get_note(pika, chat_id, keyword)
    if not to_check:
        return False
    else:
        rem = SESSION.query(Notes).get((str(pika), str(chat_id), keyword))
        SESSION.delete(rem)
        SESSION.commit()
        return True


def is_muted(pika, sender, chat_id):
    user = SESSION.query(Mute).get((str(pika), str(sender), str(chat_id)))
    if user:
        return True
    else:
        return False


def mute(pika, sender, chat_id):
    adder = Mute(str(pika), str(sender), str(chat_id))
    SESSION.add(adder)
    SESSION.commit()


def unmute(pika, sender, chat_id):
    rem = SESSION.query(Mute).get((str(pika), str(sender), str(chat_id)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_muted(pika):
    rem = SESSION.query(Mute).filter(Notes.pika == pika).all()
    SESSION.close()
    return rem


def is_gbanned(pika, sender):
    try:
        _pikaG = SESSION.query(GBan).get((str(pika), str(sender)))
        if _pikaG:
            return str(_pikaG.reason)
    finally:
        SESSION.close()


def gban(pika, sender, reason):
    adder = GBan(str(pika), str(sender), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def ungban(pika, sender, pika_id):
    rem = SESSION.query(GBan).get((str(pika), str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def is_gmuted(sender):
    try:
        return SESSION.query(GMute).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def gmute(pika, sender):
    adder = GMute(str(pika), str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungmute(pika, sender):
    rem = SESSION.query(GMute).get((str(pika), str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def add_pika(pika_id):
    pika = PikaChats(str(pika_id))
    SESSION.add(pika)
    SESSION.commit()


def is_pika_exist(pika_id):
    try:
        pika = SESSION.query(PikaChats).filter(
            PikaChats.pika_id == str(pika_id)).one()
        if pika:
            return True
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_pika_chats():
    try:
        pika = SESSION.query(PikaChats).all()
        if pika:
            return pika
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_user(pika_id: int):
    pika = BotUsers(str(pika_id))
    SESSION.add(pika)
    SESSION.commit()


def is_user_exist(pika_id):
    try:
        pika = SESSION.query(BotUsers).filter(
            BotUsers.pika_id == str(pika_id)).one()
        if pika:
            return True
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_added_users():
    pika = SESSION.query(BotUsers).all()
    SESSION.close()
    return pika


class pdb(object):
    Api_id = _get("API_ID")
    Api_hash = _get("API_HASH")
    Bf_uname = _get("TG_BOT_USER_NAME_BF_HER")
    Omega = _get("TG_BOT_TOKEN_BF_HER")
    Alpha = pget("alpha", "session")
    Beta = pget("beta", "session")
    Gaama = pget("gaama", "session")
    Delta = pget("delta", "session")
    Asstt = pget("omega", "assistant")
    Botlog_chat = int(_get("BOTLOG_CHATID"))
