import json

try:                  #Try block (attempt to read file)
    with open("memory.json", "r") as f:   #"r" = READ
        memory = json.load(f)
except:                  #Except block (if file is missing or error happens)
    memory[user_id]= {}

def save_memory():

    with open("memory.json","w") as f:   #"w" = WRITE
        json.dump(memory, f)           #dump = save data into file

print("Hello Bhavesh, how can I assist you !")

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
      save_memory()
      print("BenZ Ai==> I will remember your name.")

   elif "what is my name" in user_input:
        
        print("BenZ Ai ==>",memory.get("name","I don't know your name yet"))

   elif "save note" in user_input:       # save notes
       
       note = input("Enter your notes: ")

       if "notes" not in memory:
           memory["notes"] = []

       memory["notes"].append(note)
       save_memory()
       print("Notes saved successfully!")

   elif "delete notes" in user_input:
       
       note = input("Are you sure you want to delete all notes? (yes/No) :  ")

       if note.lower() in ["yes", "y"]:
           
           if "notes" in memory:
               del memory["notes"]
               save_memory()
               print("BenZ AI ==> Notes deleted successfully!")

           else:
               
               print("BenZ AI ==> No notes found.")

       elif note.lower() in ["no","n"]:
           
           print("BenZ AI ==> Deletion cancelled.")

       else:
           
           print("BenZ AI ==> Invalid input.")     

   elif "show notes" in user_input:
       if "notes" in memory and memory["notes"]:
           print("BenZ AI ==> your notes:")


   elif user_input in bot_responses:
       print("BenZ Ai==>",bot_responses[user_input])
       
   else:
       print("BenZ Ai==> I don't understand that.")   

 





    
