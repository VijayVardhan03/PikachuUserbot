from . import helper

# ____Main/Multiclients____


@ItzSjDude(outgoing=True, pattern=r"help ?(.*)")
@ItzSjDude(sudo=True, pattern=r"help ?(.*)")
async def _(event):
    await helper(event)
