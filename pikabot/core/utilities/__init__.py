#____ Client Ids _____
Id1="#"+"cGJvdDE"
Id2="#"+"cGJvdDI"
Id3="#"+"cGJvdDM"
Id4="#"+"cGJvdDQ"
Id5="#"+"cHRnYm90"
#_____________________

from telethon import TelegramClient
from telethon.sessions import StringSession
from ..database import pdb
def PikaClient(session, gBot=None):
    if gBot:
        return TelegramClient(
            "TgBot",
            pdb.Api_id,
            pdb.Api_hash).start(
            bot_token=session)
    else:
        return TelegramClient(
            StringSession(session),
            pdb.Api_id,
            pdb.Api_hash,
            connection_retries=None,
            auto_reconnect=True,
            lang_code='en')

def gpcid(_id_):
    if _id_==Id1:
       return PikaClient(pdb.Alpha)
    if _id_==Id2:
       return PikaClient(pdb.Beta)
    if _id_==Id3:
       return PikaClient(pdb.Gaama)
    if _id_==Id4:
       return PikaClient(pdb.Delta)
    if _id_==Id5: 
       return PikaClient(pdb.Omega, gBot=True)

__all__ = ['gpcid']
