class BaseTool:
    name: "base_tool"
    description = "Base tool"

    def run(self, input_text: str) ->str:
        raise NotImplementedError