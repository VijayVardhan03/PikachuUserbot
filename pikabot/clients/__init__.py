from ..core import pdb, pget, PikaClient
import os
bot = client = PikaClient(os.environ.get("STRING_SESSION"))

if pdb.Beta:
    bot2 = client2 = PikaClient(pdb.Beta)
else:
    bot2 = client2 = None

if pdb.Gaama:
    bot3 = client3 = PikaClient(pdb.Gaama)
else:
    bot3 = None

if pdb.Delta:
    bot4 = client4 = PikaClient(pdb.Delta)
else:
    bot4 = client4 = None

if pdb.Omega:
    tgbot = tgbot_client = PikaClient(pdb.Omega, gBot=True)

else:
    tgbot = tgbot_client = None
