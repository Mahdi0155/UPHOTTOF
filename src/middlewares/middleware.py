from aiogram import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Dict, Any, Awaitable

class SimpleMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], event: Update, data: Dict[str, Any]) -> Any:
        print("Middleware activated")
        return await handler(event, data)
