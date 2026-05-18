from fastapi import APIRouter
from pydantic import BaseModel

from llm.ollama_client import OllamaClient

from ws.manager import manager

import asyncio

router = APIRouter()

llm = OllamaClient()


class ChatRequest(BaseModel):

    message: str


@router.post("/chat")
async def chat(req: ChatRequest):

    await manager.broadcast({
        "type": "task_running",
        "task": "llm_reasoning"
    })

    response = llm.generate(
        req.message
    )

    await asyncio.sleep(1)

    await manager.broadcast({
        "type": "task_completed",
        "task": "llm_reasoning"
    })

    return {
        "response": response
    }