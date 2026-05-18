from pathlib import Path

from tools.base import BaseTool
from verifier.policy_engine import PolicyEngine


class WriteFileTool(BaseTool):

    name = "write_file"

    def __init__(self):
        self.policy = PolicyEngine()

    def execute(self, path: str, content: str):

        allowed = self.policy.verify_path(path)

        if not allowed:
            return {
                "status": "error",
                "message": "unsafe path"
            }

        full_path = Path(path)

        full_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "success",
            "path": path
        }