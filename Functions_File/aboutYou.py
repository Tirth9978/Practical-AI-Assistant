
def tellMeAboutYou():
     with open("Name.txt", "r") as file:
          first_line = file.readline().strip() 
     return first_line
