from .base_tool import BaseTool


class SearchTool(BaseTool):
    name = "search"
    description = "Search information from the web"

    def run(self, input_text:str)-> str:
        return f"Search result for: {input_text}"



"""
we can plug in 
    SerpAPI
    Tavily
    REal APIs
"""