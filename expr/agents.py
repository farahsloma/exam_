from models import*
from prompts import *
from dotenv import load_dotenv
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import os
load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini',temperature=0.0,api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1")
embedding = HuggingFaceEmbeddings(model = 'sentence-transformers/all-MiniLM-L6-v2')
vdb = Chroma(persist_directory='diet_food',embedding_function=embedding)

def rewritten_query_agent(state:State)->dict: 
    query = state.get('query')
    chat_history = state.get('messages')
    messages = [SystemMessage(content=REWRITTER_PROMPT),
                HumanMessage(content=query_rerwitten_extand(query,chat_history))]
    try:
        responce = llm.invoke(messages)
        rewritten_query = responce.content
        return{
            'rewritten_query' : rewritten_query
        }
    except Exception as e:
        print(f'Error in rewritten query agent : {e}')
        return None
    

def retrieval_query_agent(state:State)->dict:
    rerwitten_query = state.get('rewritten_query')
    retriver = vdb.as_retriever(search_kwargs = {'k':3})
    results = retriver.invoke(rerwitten_query)
    return{
        'content' : results
    }

def responce_query_agent(state:State)->dict:
    rewritten_query = state.get('rewritten_query')
    chat_history = state.get('messages')
    content = state.get('content')
    responce = [SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=System_extand(rewritten_query,chat_history,content))]
    try:
        message = llm.invoke(responce)
        result = message.content
        return {
            'response_query' : result
        }
    except Exception as e:
        print(f'error in response agent : {e}')
        return None



  