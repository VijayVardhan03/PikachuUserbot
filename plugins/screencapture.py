"""Take screenshot of any website
Syntax: .screencapture <Website URL>"""

import io

import requests
from pikabot.utils import ItzSjDude


@ItzSjDude(outgoing=True, pattern="screencapture (.*)")
async def _(event):
    if event.fwd_from:
        return
    a = await pika_msg(event, "**Processing...**")
    if pdb.ssapi is None:
        await pika_msg(a,
            "Need to get an API key from https://screenshotlayer.com/product \nModule stopping!"
        )
        return
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(sample_url.format(pdb.ssapi, input_str, "1", "2560x1440", "PNG", "1"))
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await event.client.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=input_str,
                    force_document=True,
                    reply_to=event.message.reply_to_msg_id,
                )
                await a.delete()
            except Exception as e:
                await pika_msg(a, str(e))
    else:
        await pika_msg(a, response_api.text)
