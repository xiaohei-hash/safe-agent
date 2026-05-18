from tools.registry import TOOLS

class ToolExecutor:

    def execute(self, tool_name: str, args: dict):

        tool = TOOLS.get(tool_name)

        if not tool:
            return {
                "status": "error",
                "message": "tool not found"
            }

        return tool.execute(**args)