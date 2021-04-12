"""Take screenshot of any website
Syntax: .screencapture <Website URL>"""

from . import ss
@ItzSjDude(outgoing=True, pattern="screencapture (.*)")
async def _(event):
     await ss(event)
