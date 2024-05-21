from openai import AsyncOpenAI
from tgbot.config import Config


def setup_gpt(config: Config) -> AsyncOpenAI:
    client = AsyncOpenAI(api_key=config.tg_bot.gpt_token)  # just create GPT client instance and return it;
    # will be used in bot.py and later in middleware
    return client
