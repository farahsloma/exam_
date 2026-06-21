from models import *
from workflow import*
from dotenv import load_dotenv

load_dotenv()

inital_state = State({
    'query' : 'tell me about keto diet',
    'message' : [],
    'rewritten_query':None,
    'content': None,
    'response_query' : None
    
})
workflow = workflow()
results = workflow.run(inital_state)
print(f'Rewrriten_Query: {results.get('rewritten_query')}')
print('=' * 50)
print(f'Response: {results.get('response')}')
print('='*50)