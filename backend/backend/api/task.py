from fastapi import APIRouter

from runtime.runtime_manager import RuntimeManager

router = APIRouter()

manager = RuntimeManager()


@router.get("/tasks")
def get_tasks():

    return manager.get_all_tasks()