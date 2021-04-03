from rejson import Client, Path

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
    'main': {
        'session': None,
        'pmsecurity': False,
        'pmmsg': None,
        'alivename': None,
        'alivepic': None,
        'alivemsg': None,
        'userbio': None,
        'cmdhandler': None,
        'pmlogger': None,
        'botlog': None,
        'auser': None,
        'dauser': None,
        'assistant': None
    },
    'multi1': {
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
    'multi2': {
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
    'multi3': {
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


startdb()


def pset(rejsclt, data, value):
    pth = "." + f"{rejsclt}" + "." + f"{data}"
    return pikaset('cdata', Path(f"{pth}"), value)


def pget(rejsclt, dta):
    pth = "." + f"{rejsclt}" + "." + f"{dta}"
    return pikaget('cdata', Path(f"{pth}"))

