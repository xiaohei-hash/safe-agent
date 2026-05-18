class BaseTool:

    name = "base"

    def execute(self, **kwargs):
        raise NotImplementedError