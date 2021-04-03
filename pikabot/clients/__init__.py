from ..core import pdb, pget, PikaClient

Alpha = pget("alpha", "session")
Beta = pget("beta", "session")
Gaama = pget("gaama", "session")
Delta = pget("delta", "session")
Asstt = pget("omega", "assistant")

if Alpha:
    bot = client = PikaClient(Alpha)
else:
    bot = client = None

if Beta:
    bot2 = client2 = PikaClient(Beta)
else:
    bot2 = client2 = None

if Gaama:
    bot3 = client3 = PikaClient(Gaama)
else:
    bot3 = None

if Delta:
    bot4 = client4 = PikaClient(Delta)
else:
    bot4 = client4 = None

if pdb.Omega:
    tgbot = tgbot_client = PikaClient(pdb.Omega, gBot=True)

else:
    tgbot = tgbot_client = None
