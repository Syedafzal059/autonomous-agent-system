from .base_tool import BaseTool

class CalculatorTool(BaseTool):
    name= "calculator"
    description = "Perform mathematical calculations"

    def run(self, input_text: str) -> str:
        try:
            result = eval(input_text)
            return str(result)
        except Exception:
            return "Error in calculation"