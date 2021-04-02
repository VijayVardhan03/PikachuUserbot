
from telethon import TelegramClient
from telethon.sessions import StringSession
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
