from var import Var
from ...core import pget
try:
    from ...clients import bot, bot2, bot3, bot4, tgbot
    id1 = bot.uid
    id2 = bot2.uid
    id3 = bot3.uid
    id4 = bot4.uid

except BaseException:
    pass

if bot is not None:
    i1 = id1
else:
    i1 = 1111
if bot2 is not None:
    i2 = id2
else:
    i2 = 1011
if bot3 is not None:
    i3 = id3
else:
    i3 = 1010
if bot4 is not None:
    i4 = id4
else:
    i4 = 1001


async def auto_var(_pika_, value):
  __id__=await get_pika_id(_pika_)
  if __id__==i1:
     a="alpha"
  if __id__==i2:
     a="beta"
  if __id__==i3:
     a="gaama" 
  if __id__==i4:
     a="delta"
  return pget(a, value)
  
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

__all__=['pika_msg', 'is_pikatg', 'get_pika_tg', 'get_pika_id', 'auto_var']
