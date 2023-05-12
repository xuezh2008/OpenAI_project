import sys, os, logging
from langchain.llms import OpenAI
from langchain.chains import LLMRequestsChain, LLMChain
from langchain import PromptTemplate

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

API_KEY = open("my_key.txt" , "r").read()
os.environ['OPENAI_API_KEY'] = API_KEY

#def api_query():

template = """Between >>> and <<< are the raw search result text from google.
Extract the answer to the question '{query}' or say "not found" if the information is not contained.
Use the format
Extracted:<answer or "not found">
>>> {requests_result} <<<
Extracted:"""

PROMPT = PromptTemplate(
    input_variables=["query", "requests_result"],
    template=template,
)
chain = LLMRequestsChain(llm_chain=LLMChain(llm=OpenAI(temperature=0), prompt=PROMPT))
question = "competitive landscape in short-video industry"
inputs = {
    	"query": question,
    	"url": "https://www.google.com/search?q=" + question.replace(" ", "+")
}

response = chain(inputs)
print(response)


