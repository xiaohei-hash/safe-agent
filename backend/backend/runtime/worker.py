import asyncio

from runtime.runtime_manager import RuntimeManager
from runtime.websocket_manager import manager as ws_manager

from agent.tool_executor import ToolExecutor

manager = RuntimeManager()
executor = ToolExecutor()


def emit(message):

    loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)

    loop.run_until_complete(
        ws_manager.broadcast(message)
    )

    loop.close()


def process_task(task):

    task_id = task["id"]

    try:

        manager.update_task(
            task_id,
            "running"
        )

        emit({
            "type": "task_running",
            "task": task
        })

        result = executor.execute(
            task["tool"],
            task["args"]
        )

        manager.update_task(
            task_id,
            "completed",
            result
        )

        emit({
            "type": "task_completed",
            "task_id": task_id,
            "result": result
        })

    except Exception as e:

        manager.update_task(
            task_id,
            "failed",
            str(e)
        )

        emit({
            "type": "task_failed",
            "task_id": task_id,
            "error": str(e)
        })