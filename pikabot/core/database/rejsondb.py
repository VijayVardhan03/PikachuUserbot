from rejson import Client, Path
import os 

_get = os.environ.get
uri = _get("REDIS_ENDPOINT").split(":")
host = uri[0]
port = uri[1]
password = _get("REDIS_PASSWORD")
pikadb = Client(
    host=host,
    port=port,
    password=password,
    decode_responses=True)
pikaset = pikadb.jsonset
pikadel = pikadb.jsondel
pikaget = pikadb.jsonget

cdata = {
    'alpha': {
        'session': None,
        'pmsecurity': False,
        'pmmsg': None,
        'alivename': None,
        'alivepic': None,
        'alivemsg': None,
        'userbio': None,
        'cmdhandler': None,
        'tgbothandler': None,
        'pmlogger': None,
        'botlog': None,
        'auser': None,
        'dauser': None,
        'assistant': None
    },
    'beta': {
        'session': None,
        'pmsecurity': False,
        'pmmsg': None,
        'alivename': None,
        'alivepic': None,
        'alivemsg': None,
        'userbio': None,
        'pmlogger': None,
        'auser': None,
        'dauser': None
    },
    'gaama': {
        'session': None,
        'pmsecurity': False,
        'pmmsg': None,
        'alivename': None,
        'alivepic': None,
        'alivemsg': None,
        'userbio': None,
        'pmlogger': None,
        'auser': None
    },
    'delta': {
        'session': None,
        'pmsecurity': False,
        'pmmsg': None,
        'alivename': None,
        'alivepic': None,
        'alivemsg': None,
        'userbio': None,
        'pmlogger': None,
        'auser': None,
        'dauser': None
    },
    'apis': {
        'youtubeapi': None,
        'lyndiaapi': None,
        'screenshotapi': None,
        'removebgapi': None
    },
}


def startdb():
    old_db_exists = pikaget('cdata', Path.rootPath())
    if not old_db_exists:
        pikaset("cdata", Path.rootPath(), cdata)
    else:
        return

def pset(rejsclt, data, value):
    pth = "." + f"{rejsclt}" + "." + f"{data}"
    return pikaset('cdata', Path(f"{pth}"), value)


def pget(rejsclt, dta):
    pth = "." + f"{rejsclt}" + "." + f"{dta}"
    return pikaget('cdata', Path(f"{pth}"))

class pdb(object):
    Api_id = _get("API_ID")
    Api_hash = _get("API_HASH")
    Omega = _get("TG_BOT_TOKEN_BF_HER")
    Bf_uname = _get("TG_BOT_USER_NAME_BF_HER")
    Botlog_chat = int(_get("BOTLOG_CHATID"))
    Alpha = pget("alpha", "session")
    Beta = pget("beta", "session")
    Gaama = pget("gaama", "session")
    Delta = pget("delta", "session")
