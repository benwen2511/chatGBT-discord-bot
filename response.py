import json
import openai
from asgiref.sync import sync_to_async
from get_token import get_token


openai.api_key = get_token("openai_api_key")


async def get_response(message,aiMsg='') -> str:
    promptMsg = f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever but sometimes sarcastic as well\nAI:{aiMsg}\nHuman:{message}\nAI:"
    
    response = await sync_to_async(openai.Completion.create)(
        model="text-davinci-003",
        prompt=promptMsg,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    responseMessage = response.choices[0].text
    return responseMessage

async def get_img(message):
    response = openai.Image.create(
    prompt=message,
    n=1,
    size="1024x1024"
)
    image_url = response['data'][0]['url']
    return image_url
