import openai

API_KEY = open("my_key.txt" , "r").read()
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
	model = "gpt-3.5-turbo",
	messages = [
		{"role": "user", "content": "blahblah"}
	]
)

print(response)