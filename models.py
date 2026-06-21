from typing import Optional,Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    query:str
    messages : Annotated[list, add_messages]
    rewritten_query:Optional[str]
    content:Optional[list[str]]
    response_query : Optional[str]
    
