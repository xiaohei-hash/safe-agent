from planner.planner import Planner

from runtime.runtime_manager import RuntimeManager
from runtime.worker import process_task


class AgentOrchestrator:

    def __init__(self):

        self.planner = Planner()
        self.manager = RuntimeManager()

    def run(self, user_input: str):

        tasks = self.planner.create_plan(user_input)

        created_tasks = []

        for task in tasks:

            runtime_task = self.manager.create_task(
                task.tool,
                task.args
            )

            process_task(runtime_task)

            created_tasks.append(runtime_task)

        return {
            "queued_tasks": created_tasks
        }