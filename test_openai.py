import openai
import requests

API_KEY = open("my_key.txt" , "r").read()
openai.api_key = API_KEY

#-----------------testing Chat API-----------------
response_chat = openai.ChatCompletion.create(
	model = "gpt-3.5-turbo",
	messages = [
		{"role": "user", "content": "provide a more detailed prompt for Dall-E based on this: an ultra happy assistant"}
	]
)

response_chat_text = response_chat['choices'][0]['message']['content']

with open("test_openai_prompt.log", "a") as file:
		file.write(response_chat_text + "\n")


#-----------------testing DallE API-----------------
response_img = openai.Image.create(
	prompt = response_chat_text,
	n = 1,
	size = "256x256"
)

image_url = response_img['data'][0]['url']

img = requests.get(image_url)

with open('test_openai_ultra_happy_assistant.jpg', 'wb') as f:
	f.write(img.content)