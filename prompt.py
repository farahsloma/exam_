REWRITTER_PROMPT=f""" you are a Nutritionist. your task is to rewrite the user query to make it more effective for information retrieval 
Guidelines:
preserves the original intent of the query
make the query more specific and detailed
use natural language and complete sentence
"""
def query_rerwitten_extand(user_input:str,chat_history:str)->str:
    chat_history_str = ""
    if chat_history:
        for msg in chat_history:
            if hasattr(msg,'content'):
                chat_history_str +=f'{msg.content}'
            else:
                chat_history_str += f'{str(msg)}'
    prompt = f"""
    User Query : {user_input}
    Chat History : {chat_history_str}
    Rerwirtten Query :
    """
    return prompt

SYSTEM_PROMPT = """
        you are an assistant. Your task is to assist the user in finding information and answering questions.
"""
def System_extand(user_query:str, chat_history:str,content: str)-> str:
    prompt = f"""
    User Query : {user_query}
    Chat History : {chat_history}
    Content : {content}
    please provid a helpful response based on the above information

"""
    return prompt