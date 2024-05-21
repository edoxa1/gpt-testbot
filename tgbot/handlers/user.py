from aiogram import Router
from aiogram.types import Message

from openai import AsyncOpenAI

from tgbot.filters.whitelist import WhitelistFilter


user_router = Router()
user_router.message.filter(WhitelistFilter())


@user_router.message()
async def ask_bro(message: Message, gpt: AsyncOpenAI):
    if '?!' not in message.text:  # filter messages where users need to ask GPT
        await message.answer("ask a question like 'explain this<b>?!</b>'")
        return

    response = await gpt.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "user",
                "content": f"Answer this question in any language:\n {message.text}"}
        ],
        max_tokens=1000,
    )

    await message.answer(text=f"{response.choices[0].message.content}\n\n"
                              f"<i>Tokens used: {response.usage.total_tokens}</i>")
