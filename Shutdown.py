def shutdown():
  if user_input.lower()=="yes":
    print("Shutting down the computer")
  elif user_input.lower()=="no":
    print("Abort shut down")
  else:
    print("Sorry!")
user_input=input("Do you want to shut down?[yes/no]=")
shutdown()