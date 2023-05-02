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


# -------------Sample--------------
# hello
# ZzzGPT: there!

# Greetings and salutations! It's so wonderful to see you here today. You know, I was browsing through my favorite book of motivational quotes this morning, and I came across one that I think would be perfect for you: "Today is the perfect day to be happy!" Isn't that just wonderful?

# I'm thrilled to provide you with some amazing assistance today, and to make your day even brighter, I'll share with you three of my favorite jokes. Why did the tomato turn red? Because it saw the salad dressing! What did the grape say when it got stepped on? Nothing, it just let out a little wine! And last but not least, what did one hat say to another? You wait here, I'll go on ahead!

# Hahaha! I hope those jokes put a smile on your face. Now how may I assist you further today?