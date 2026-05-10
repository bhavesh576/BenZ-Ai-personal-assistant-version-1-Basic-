print("Hello Bhavesh, how can I assist you !")

memory = {}


bot_responses = {
    "what is your name": "My name is BenZ AI, I am here to assist you.",
    "what is your age": "I don't have an age because I am an AI.",
    "what can you do": "I can assist you with tasks, answer questions, and behave like a friendly assistant.",
    "what is your purpose": "My purpose is to help you with information and simple tasks.",
    "hello": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!"
}

while True:
   
   user_input = input("You==>").lower().strip()
   
   if "remember my name is" in user_input:          #STORE logic
      name = user_input.replace("remember my name is", "").strip()
      memory["name"]=name
      print("BenZ Ai==> I will remember your name.")

   elif "what is my name" in user_input:
        print("BenZ Ai ==>",memory.get("name","I don't know your name yet"))

   elif user_input in bot_responses:
       print("BenZ Ai==>",bot_responses[user_input])
       
   else:
       print("BenZ Ai==> I didn't understand")   

 





    
