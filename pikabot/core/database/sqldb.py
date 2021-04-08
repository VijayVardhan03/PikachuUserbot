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
    engine = create_engine(_get("DATABASE_URL").replace("postgres", "postgresql"))
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()


class Pdb(BASE):
    __tablename__ = "pdb"
    id = Column(Integer, primary_key=True)
    pika = Column(String(14))
    var = Column(String(14))
    value = Column(UnicodeText)

    def __init__(self, pika, var, value):
        self.pika = str(pika)
        self.var = str(var)
        self.value = value


class BotUsers(BASE):
    __tablename__ = "botusers"
    pika_id = Column(String(14), primary_key=True)

    def __init__(self, pika_id):
        self.pika_id = pika_id


class PikaChats(BASE):
    __tablename__ = "PikaTg"
    pika_id = Column(String(14), primary_key=True)

    def __init__(self, pika_id):
        self.pika_id = pika_id


class GMute(BASE):
    __tablename__ = "gmute"
    pika = Column(String(14), primary_key=True)
    sender = Column(String(14), primary_key=True)

    def __init__(self, pika, sender):
        self.pika = str(pika)
        self.sender = str(sender)


class GBan(BASE):
    __tablename__ = "gban"
    pika = Column(String(14), primary_key=True)
    sender = Column(String(14), primary_key=True)
    reason = Column(UnicodeText)

    def __init__(self, pika, sender, reason=""):
        self.pika = str(pika)
        self.sender = str(sender)
        self.reason = reason


class Mute(BASE):
    __tablename__ = "mute"
    pika = Column(String(14), primary_key=True)
    sender = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    

    def __init__(self, pika, sender, chat_id):
        self.pika = str(pika)
        self.sender = str(sender)
        self.chat_id = str(chat_id)
        


class Notes(BASE):
    __tablename__ = "notes"
    pika = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    keyword = Column(UnicodeText, primary_key=True)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)
    
    def __init__(self, pika, chat_id, keyword, reply, f_mesg_id):
        self.pika = str(pika)
        self.chat_id = str(chat_id)
        self.keyword = keyword
        self.reply = reply
        self.f_mesg_id = f_mesg_id


class PMPermit(BASE):
    __tablename__ = "pmpermit"
    id = Column(Integer, primary_key=True)
    pika = Column(String(14))
    chat_id = Column(String(14))
    reason = Column(String(127))

    def __init__(self, pika, chat_id, reason=""):
        self.pika = str(pika)
        self.chat_id = chat_id
        self.reason = reason
        


class Welcome(BASE):
    __tablename__ = "welcome"
    pika = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
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

class Filters(BASE):
    __tablename__ = "filters"
    id = Column(Integer, primary_key=True)
    pika = Column(String(14))
    chat_id = Column(String(14))
    keyword = Column(UnicodeText)
    reply = Column(UnicodeText)
    snip_type = Column(Numeric)
    media_id = Column(UnicodeText)
    media_access_hash = Column(UnicodeText)
    media_file_reference = Column(LargeBinary)

    def __init__(
        self,
        pika, 
        chat_id,
        keyword, reply, snip_type,
        media_id=None, media_access_hash=None, media_file_reference=None
    ):
        self.pika = pika
        self.chat_id = chat_id
        self.keyword = keyword
        self.reply = reply
        self.snip_type = snip_type
        self.media_id = media_id
        self.media_access_hash = media_access_hash
        self.media_file_reference = media_file_reference

class Locks(BASE):
    __tablename__ = "locks"
    pika = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)


    def __init__(self, pika, chat_id):
        self.pika = str(pika) # ensure string
        self.chat_id = str(chat_id)  # ensure string  
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Pdb.__table__.create(checkfirst=True)
Mute.__table__.create(checkfirst=True)
BotUsers.__table__.create(checkfirst=True)
PikaChats.__table__.create(checkfirst=True)
GMute.__table__.create(checkfirst=True)
GBan.__table__.create(checkfirst=True)
Notes.__table__.create(checkfirst=True)
PMPermit.__table__.create(checkfirst=True)
Welcome.__table__.create(checkfirst=True)
Filters.__table__.create(checkfirst=True)
Locks.__table__.create(checkfirst=True)

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

def get_filter(pika, chat_id, keyword):
    try:
        return SESSION.query(Filters).get((str(pika), str(chat_id), keyword))
    except:
        return None
    finally:
        SESSION.close()


def get_all_filters(pika, chat_id):
    try:
        return SESSION.query(Filters).filter(Filters.pika == str(pika), Filters.chat_id == str(chat_id)).all()
    except:
        return None
    finally:
        SESSION.close()


def add_filter(pika, chat_id, keyword, reply, snip_type, media_id, media_access_hash, media_file_reference):
    adder = SESSION.query(Filters).get((str(pika), str(chat_id), keyword))
    if adder:
        adder.reply = reply
        adder.snip_type = snip_type
        adder.media_id = media_id
        adder.media_access_hash = media_access_hash
        adder.media_file_reference = media_file_reference
    else:
        adder = Filters(pika, chat_id, keyword, reply, snip_type, media_id,
                        media_access_hash, media_file_reference)
    SESSION.add(adder)
    SESSION.commit()


def remove_filter(pika, chat_id, keyword):
    saved_filter = SESSION.query(Filters).get((str(pika), str(chat_id), keyword))
    if saved_filter:
        SESSION.delete(saved_filter)
        SESSION.commit()


def remove_all_filters(chat_id):
    saved_filter = SESSION.query(Filters).filter(Filters.pika == str(pika), Filters.chat_id == str(chat_id))
    if saved_filter:
        saved_filter.delete()
        SESSION.commit()

def init_locks(pika, chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(pika), str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(pika), str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr


def update_lock(pika, chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get((str(pika), str(chat_id)))
    if not curr_perm:
        curr_perm = init_locks(pika, chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(pika, chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get((str(pika), str(chat_id)))
    SESSION.close()
    if not curr_perm:
        return False
    elif lock_type == "bots":
        return curr_perm.bots
    elif lock_type == "commands":
        return curr_perm.commands
    elif lock_type == "email":
        return curr_perm.email
    elif lock_type == "forward":
        return curr_perm.forward
    elif lock_type == "url":
        return curr_perm.url


def get_locks(pika, chat_id):
    try:
        return SESSION.query(Locks).get((str(pika), str(chat_id)))
    finally:
        SESSION.close()

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
    Ytapi = pget("omega", "ytapi")
    Gdtoken = pget("omega", "gdtoken")
    if pget("alpha", "sudo"):  
       Asudo = pget("alpha", "sudo")
    else: 
       Asudo = None
    if pget("beta", "sudo"):
       Bsudo = pget("beta", "sudo")
    else: 
       Bsudo = None
    if pget("gaama", "sudo"):
       Gsudo = pget("gaama", "sudo")
    else: 
       Gsudo = None
    if pget("delta", "sudo"):
       Dsudo = pget("delta", "sudo")
    else: 
       Dsudo= None
    if pget("omega", "sudo"):
       Osudo = pget("omega", "sudo")
    else: 
       Osudo = None

