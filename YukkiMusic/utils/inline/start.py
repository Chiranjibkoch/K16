#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="•❀ ʜᴇʟᴘ & ᴄᴍᴅs ❀•",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="•❀sᴇᴛᴛɪɴɢs❀•", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•✯ ✗ ᴀᴅᴅ ᴍᴇ ᴍᴇʀɪ ᴊᴀᴀɴ ✯• ✗",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="•❀ ʜᴇʟᴘ & ᴄᴍᴅs ❀•",
                callback_data="settings_back_helper",
            )
        ],
        [
            InlineKeyboardButton(
                text="•✩ sᴜᴘᴘᴏʀᴛ ✩•", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="•✩ ᴄʜᴀɴɴᴇʟ ✩•", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ •ᴏᴡɴᴇʀ•✨", url="https://t.me/itszoney"
            )
        ],
     ]
    return buttons
