import uuid

from runtime.runtime_store import tasks


class RuntimeManager:

    def create_task(self, tool, args):

        task_id = str(uuid.uuid4())

        task = {
            "id": task_id,
            "tool": tool,
            "args": args,
            "status": "pending",
            "result": None
        }

        tasks[task_id] = task

        return task

    def update_task(self, task_id, status, result=None):

        if task_id not in tasks:
            return

        tasks[task_id]["status"] = status
        tasks[task_id]["result"] = result

    def get_task(self, task_id):

        return tasks.get(task_id)

    def get_all_tasks(self):

        return list(tasks.values())