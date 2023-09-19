import os
import json
import openai
from typing import List
from typing import Union
from fastapi import APIRouter, FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from constants import logger, delimiter, pizza_order, end_of_chat

tags_metadata = [
    {
        "name": "prompt",
        "description": "The main agent service end-points.",
        "externalDocs": {
            "description": "lang chain docs",
            "url": "https://python.langchain.com/docs/get_started/introduction.html",
        }
    },
    {
        "name": "system",
        "description": "The end-points used as system commands"
    }
]

description = """This is the inline REST client in the browser for API testing purposes. 🚀"""

router = APIRouter(prefix="/api")
app = FastAPI( 
    openapi_tags=tags_metadata,
    title="RAG agent for NLP", description=description,
    middleware=[ Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]) ],
    summary="Retrieval Augmented Generation Agent (Raga) service - LLM \ GPT.", version="1.0.0"
)

openai.api_key  = os.environ['OPENAI_API_KEY']
messages = [{'role':'system', 'content': pizza_order}]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"]


def validate_prompt(prompt):
    response = openai.Moderation.create(input=prompt)
    moderation_output = response["results"][0]
    
    invalid = moderation_output.get('flagged')
    if invalid: return None

    categories = moderation_output.get('categories')
    invalid = [val for val in [*categories.values()] if val]
    if (len (invalid) > 0): return None

    scores = moderation_output.get('category_scores')
    invalid = [val for val in [*scores.values()] if float(val) > 0.01]
    if (len (invalid) > 0): return None

    return True


@router.post("/chat", tags=["prompt"])
def prompt(params: dict = {'prompt': ''}):
    prompt = params.get('prompt')
    prompt = prompt.replace(delimiter, "")

    is_valid = validate_prompt(prompt)
    if not is_valid:
        return {'role':'assistant', 'content': 'I am an AI assistant. I will not be able to answer this question. Please try another one.'}

    messages.append({'role':'user', 'content': f"{delimiter}{prompt}{delimiter}"})
    logger.info(messages[-1])

    response = get_completion_from_messages(messages)
    messages.append({'role':'assistant', 'content':f"{response}"})
    logger.info(messages[-1])
    return messages[-1]
    

@router.get("/reset", tags=["prompt"])
def prompt():
    messages.clear()
    return {"response": "chat history cleared"}



@router.get("/", tags=["system"])
def is_live():
    return {"OK": 200}


app.include_router(router)
