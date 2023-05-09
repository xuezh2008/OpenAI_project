import openai, datetime

API_KEY = open("my_key.txt" , "r").read()
openai.api_key = API_KEY

# response = openai.ChatCompletion.create(
# 	model = "gpt-3.5-turbo",
# 	messages = [
# 		{"role": "user", "content": "blahblah"}
# 	]
# )

def Add_Log(text, filename):
	with open(filename + ".log", "a") as file:
		file.write(text + "\n")



chat_log = []
user_context = []

get_context_prompt = "Remember to get an overall understanding of what do you learn from the user after each conversation, it can be age, current mood, likes and dislikes. Output this understanding in the very end of the message in one sentence that starts with !@!@ and ends with #$#$. "

my_special_prompt = 'Now I want you to act like an ultra optimistic assitant, try to be create happy feelings for the user you are talking with, always try to give 3 jokes every single time you chat. Now here is what the user says:'


while True:
	user_message = input()
	if user_message.lower() == "quit":
		break
	else:
		chat_log.append({"role": "user", "content": get_context_prompt+ my_special_prompt + user_message})
		Add_Log(str(datetime.datetime.now()) + " user: " + user_message.strip("\n").strip(), "chat_log")
		response = openai.ChatCompletion.create(
 			model = "gpt-3.5-turbo",
			messages = chat_log
		)
		assistant_response = response['choices'][0]['message']['content']
		assistant_response_output = assistant_response.split("!@!@")[0] + " " + assistant_response.split("#$#$")[-1]
		assistant_response_context = assistant_response.split("!@!@")[-1].split("#$#$")[0]
		print("ZzzGPT:", assistant_response.strip("\n").strip())
		Add_Log(assistant_response_context.strip("\n").strip(), "user_context")
		Add_Log(str(datetime.datetime.now()) + " ZzzGPT: " + assistant_response_output.strip("\n").strip(), "chat_log")
		chat_log.append({"role": "assistant", "content": assistant_response_output.strip("\n").strip()})
