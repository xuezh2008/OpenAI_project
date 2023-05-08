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


#-----------------testing DallE API: text -> image-----------------
response_img = openai.Image.create(
	prompt = response_chat_text,
	n = 1,
	size = "256x256"
)

image_url = response_img['data'][0]['url']

img = requests.get(image_url)

with open('test_openai_ultra_happy_assistant.jpg', 'wb') as f:
	f.write(img.content)


#-----------------testing DallE API: image -> text-----------------
from io import BytesIO
import base64

# Download image data from image_url
# img = requests.get(image_url)

image_data = base64.b64encode(img.content).decode('utf-8')

# Generate text based on the image
response_image_understanding = openai.Completion.create(
    engine="dall-e-2",
    prompt=f"Generate a description of this image: {image_url}",
    image=image_data,
    max_tokens=512,
    n=1,
    stop=None,
    temperature=0.5
)

# Extract generated text from response_image_understanding 
image_understanding_text = response_image_understanding .choices[0].text.strip()
print(image_understanding_text)
with open("test_openai_image_understanding.log", "a") as file:
		file.write(image_understanding_text + "\n")