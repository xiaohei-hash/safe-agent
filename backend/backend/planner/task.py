from dataclasses import dataclass


@dataclass
class Task:

    tool: str
    args: dict