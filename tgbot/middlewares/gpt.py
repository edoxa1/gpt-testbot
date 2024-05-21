from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


class GptMiddleware(BaseMiddleware):
    def __init__(self, client) -> None:
        self.client = client  # GPT client instance
        # note that this constructor will be called only once, so this is some sort of "singleton"

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        data["gpt"] = self.client  # link client to middleware, so we can access it from handlers;
        return await handler(event, data)
