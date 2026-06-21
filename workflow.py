from models import*
from prompts import *
from agents import*
from langgraph.graph import START,END,StateGraph

class Workflow:
    def __init__(self):
        
        self.rewritten_query = rewritten_query_agent
        self.responce = responce_query_agent
        self.retrieval = retrieval_query_agent
        
    def build_model(self):
        graph = StateGraph(State)
        graph.add_node('rewritten_query_agent',self.rewritten_query)
        graph.add_node('responce',self.responce)
        graph.add_node('retrieval',self.retrieval)
       

        graph.add_edge(START,'rewritten_query_agent')
        graph.add_edge('rewritten_query_agent','retrieval')
        graph.add_edge('retrieval','responce')
        graph.add_edge('responce',END)

        return graph.compile()
    def run(self,inital_state:State):
        graph = self.build_model()
        result = graph.invoke(inital_state)
        return result