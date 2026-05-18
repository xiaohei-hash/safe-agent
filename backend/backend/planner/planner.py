from planner.task import Task


class Planner:

    def create_plan(self, user_input: str):

        tasks = []

        if "create file" in user_input:

            tasks.append(
                Task(
                    tool="write_file",
                    args={
                        "path": "workspace/test.txt",
                        "content": "hello runtime queue"
                    }
                )
            )

        return tasks