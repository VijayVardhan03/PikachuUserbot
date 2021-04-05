import time;import os;from var import Var 
import telethon, platform
from pikabot import pdb
sys1 = (platform.python_version()) 
sys2 = "2.1 Stable" 
sys3 = "1.0 Stable"
sys4 = "https://github.com/ItzSjdude/PikachuUserbot"
sys5 = (telethon.__version__)
sys6 = "[Here](t.me/PikaUserbot_Support)"
sys7= "[GNU GPL v3.0](https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE)"
sys8= "[Copyright](https://github.com/ItzSjDude)"

a=0
if pdb.Beta:
  a+=1
if pdb.Gaama:
  a+=1
if pdb.Delta:
  a+=1

if a==0:
  stats = "**Disabled | No clients found**"
else:
  stats = f"**Enabled | {a} Connected**"


upt={}
con={}  
web="https://ItzSjDude.in"
chnl="[Here](t.me/PikachuUserBot)"
apic="https://telegra.ph/file/891421e264af0ebc5c902.mp4"

helpstr=f"\n\nPikabot Helper to reveal all the plugins, Just tap on button and reveal....\n\n✧ Repo : [Github]({sys4})\n✧ Website : [Here]({web})"

alivestr="•This is \n       ╔═╦╦╗───╔╗──╔╗\n       ║╬╠╣╠╦═╗║╚╦═╣╚╗\n       ║╔╣║═╣╬╚╣╬║╬║╔╣\n       ╚╝╚╩╩╩══╩═╩═╩═╝\n**Alive Time** : {}⌚\n\n✨ Telethon Version ☞ {}\n✨ Python Version ☞ {}\n✨ Pika Os ☞ {}\n✨ Pika Plugins ☞ {}\n✨ Support Channel ☞ {}\n✨ Support group ☞ {}\n✨ Multiclients ☞ {}\n\n👨‍💻**Servent of My Master**  ☞ {}".format(upt,sys5,sys1,sys2,sys3,chnl,sys6,stats,con)
__all__ = ['web', 'chnl', 'apic', 'stats', 'sys1', 'sys2', 'sys3', 'sys4', 'sys5', 'sys6', 'sys7', 'sys8', 'alivestr', 'helpstr'] 
