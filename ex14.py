from sys import argv

script, user_name = argv
prompt = "> "

print (f"Hi {user_name}, I'm the script {script} ")
print("I'd like to ask you a few questions.")
likes = input(f"Do you like me {user_name}? {prompt}") 

lives = input(f"Where do you live {user_name}? {prompt}")

computer = input(f"What type of computer do you have? {prompt}") 
print("")

print (f"""Alright so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice""" )