
from ...clients import *
async def pika_msg(_pika, text, _pika_=None, parse_mode=None, link_preview=None):
  parse_mode = parse_mode or "md"; link_preview = link_preview or False
  if _pika_ is None:
      return await _pika.edit(text, parse_mode=parse_mode, link_preview=link_preview)
  else:
      return await _pika.reply(text, parse_mode=parse_mode,link_preview=link_preview)
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/> 
async def is_pikatg(_pika_=None):
  _pika = await _pika_.client.get_me()
  if _pika.id== tgbot.uid:
      return True

#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def get_pika_id(_pika):
  _pika_= await _pika.client.get_me() 
  return _pika_.id 

#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def get_pika_tg(_pika_): 
  tg_id = await get_pika_id(_pika_)
  if not tg_id == 779890498: 
      if Var.SUDO_USERS1 or Var.SUDO_USERS2 or Var.SUDO_USERS3 or Var.SUDO_USERS4: 
          if _pika_.sender_id in Var.SUDO_USERS1 or _pika_.sender_id in Var.SUDO_USERS2 or _pika_.sender_id in Var.SUDO_USERS3 or _pika_.sender_id in Var.SUDO_USERS4:
              return True

  if tg_id == bot.uid: 
      return None
    
  if tg_id == tgbot.uid: 
      return True 

#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def add_chat(_pika_):
  if await is_pikatg(_pika_): 
     if not _pika_.is_private:
        if not is_pika_exist(_pika_.chat_id): 
           add_pika(_pika_.chat_id)
           return "Added" 
  else:
    return
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def pika_cmds(_pika_):
  global PikaAsst
  if not await is_pikatg(_pika_):
      return bot.pika_cmd
  else: 
      return PikaAsst
