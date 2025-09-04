import time as tm
from time import gmtime,strftime

def intro():
     s =int(strftime("%H"))
     str = ""
     if (s >= 6 and s < 12):
          # print("Good Morning Sir , How can I help you today")
          str = "Good Morning Sir"
     elif (s > 11 and s <= 17):
          # print("Good Afternoon Sir , How can I help you today")
          str = "Good Afternoon Sir"
     elif(s > 17 and s < 22):
          # print("Good Evening Sir , How can I help you today")
          str = "Good Evening Sir"
     else :
          str = "Good Night Sir"
     return str 
