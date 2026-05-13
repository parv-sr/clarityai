from langchain.tools import tool, ToolRuntime
from langchain.messages import HumanMessage
from langgraph.types import Command
from typing import List
import psycopg2


class LLMTools:
    def __init__(self):
        pass

    @tool
    def get_last_user_message(self, runtime: ToolRuntime) -> str:
        """
        Gets the last user message
        """
        messages = runtime.state["messages"]
        for message in reversed(messages):
            if isinstance(message, HumanMessage):
                return message.content
        
        return "No user message found"
    
    @tool
    def set_user_name(self, new_name: str) -> Command:
        pass

    @tool
    def get_course_list(self) -> List[str]:
        """
        Get the full course list. No args required.
        """
        query = "SELECT course FROM public.course;"

