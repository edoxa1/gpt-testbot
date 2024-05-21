from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Config


class WhitelistFilter(BaseFilter):
    async def __call__(self, obj: Message, config: Config) -> bool:
        return obj.from_user.id in config.tg_bot.whitelist_ids  # sort all incoming events by user id;
        # only whitelist is allowed


