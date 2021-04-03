from ..core import pdb, pget, PikaClient

if pdb.Alpha:
    bot = client = PikaClient(Alpha)
else:
    bot = client = None

if pdb.Beta:
    bot2 = client2 = PikaClient(Beta)
else:
    bot2 = client2 = None

if pdb.Gaama:
    bot3 = client3 = PikaClient(Gaama)
else:
    bot3 = None

if pdb.Delta:
    bot4 = client4 = PikaClient(Delta)
else:
    bot4 = client4 = None

if pdb.Omega:
    tgbot = tgbot_client = PikaClient(pdb.Omega, gBot=True)

else:
    tgbot = tgbot_client = None
