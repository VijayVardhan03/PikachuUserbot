"""Profile Related Commands
{i}autobio
**Usage**: Activates Autobio\n
{i}autoname
**Usage**: Activates Autoname\n
{i}autopfp
**Usage**: Activates Autopic\n
{i}avengerspfp
**Usage**: Activates auto Avengers pics\n
{i}animepfp
**Usage**: Activates Anime pics\n
{i}gamerpfp
**Usage**: Activates Gamer pics\n
{i}pbio <Bio>
**Usage**: sets Bio\n
{i}pname <Name>
**Usage**: sets Name\n
{i}ppic <Reply to pic>
**Usage**: sets Profile pic\n
"""
from . import anpfp, atb, atnm, avpfp, gmpfp, pbio, pname


@ItzSjDude(outgoing=True, pattern="pbio (.*)")
@ItzSjDude(sudo=True, pattern="pbio (.*)")
async def _(event):
    await pbio(event)


@ItzSjDude(outgoing=True, pattern="pname ((.|\n)*)")
@ItzSjDude(sudo=True, pattern="pname ((.|\n)*)")
async def _(event):
    await pname(event)


@ItzSjDude(outgoing=True, pattern="animepfp ?(.*)")
@ItzSjDude(sudo=True, pattern="animepfp ?(.*)")
async def _(event):
    await anpfp(event)


@ItzSjDude(outgoing=True, pattern="avengerspfp ?(.*)")
@ItzSjDude(sudo=True, pattern="avengerspfp ?(.*)")
async def _(event):
    await avpfp(event)


@ItzSjDude(outgoing=True, pattern="gamerpfp ?(.*)")
@ItzSjDude(sudo=True, pattern="gamerpfp ?(.*)")
async def _(event):
    await gmpfp(event)


@ItzSjDude(outgoing=True, pattern="autoname$")
@ItzSjDude(sudo=True, pattern="autoname$")
async def _(event):
    await atnm(event)


@ItzSjDude(outgoing=True, pattern="autobio$")
@ItzSjDude(sudo=True, pattern="autobio$")
async def _(event):
    await atb(event)
