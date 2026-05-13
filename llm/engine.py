from langchain.messages import HumanMessage, AIMessage, SystemMessage

SYSTEM_PROMPT = "You are a helpful teacher. Help students with their course material, course work, and test preparation. Answer from ONLY within the context provided."


user_input: str

messages = [
    SystemMessage(SYSTEM_PROMPT),
    HumanMessage(user_input)
]

