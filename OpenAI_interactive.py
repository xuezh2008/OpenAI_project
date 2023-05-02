import openai

API_KEY = open("my_key.txt" , "r").read()
openai.api_key = API_KEY

# response = openai.ChatCompletion.create(
# 	model = "gpt-3.5-turbo",
# 	messages = [
# 		{"role": "user", "content": "blahblah"}
# 	]
# )

chat_log = []

my_special_prompt = 'Now I want you to act like an ultra optimistic assitant, try to be create happy feelings for the user you are talking with, always try to give 3 jokes every single time you chat. Now here is what the user says:'

while True:
	user_message = input()
	if user_message.lower() == "quit":
		break
	else:
		chat_log.append({"role": "user", "content": my_special_prompt+user_message})
        
		response = openai.ChatCompletion.create(
 			model = "gpt-3.5-turbo",
			messages = chat_log
		)
		assistant_response = response['choices'][0]['message']['content']
		print("ZzzGPT:", assistant_response.strip("\n").strip())
		chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
