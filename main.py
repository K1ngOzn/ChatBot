import time
import os
import random
#line 53
colors=["\033[030m","\033[031m","\033[032m","\033[033m","\033[034m","\033[035m","\033[036m"]
color=random.choice(colors)
#operating system instructions
def c():
  os.system('clear')
age_required=[0]
negative=[0]
positive_credit_list=[0]
negative_credit_list=[0]
account=False
def options():
  print("\n________________________\nAdd Credits\n________________________\nSubtract Credits\n________________________\nMake A Credit Account\n________________________\nCheck Account\n________________________\nExit\n________________________\nMake A bank Account\n________________________\nAdd Age\n________________________\n________________________\n")
#
def minimum_age(age_required):
  numbers=["1","2","3","4","5","6","7","8","9","0"]
  value=False
  while value==False:
    minimum_age=input("What is your age?: ")
    f=0
    for age in minimum_age:
      if age in numbers:
        continue
      else:
        f+=1
    if f==0:
      minimum_age=int(minimum_age)
      age_required.append(minimum_age)
      value=True
    else:
      print("\ninvalid input")
  print("\n________________________")
def subtract(negative):
  numbers=["1","2","3","4","5","6","7","8","9","0"]
  value=False
  while value==False:
    subtract=input("Please input 0: ")
    f=0
    for credit in subtract:
      if credit in numbers:
        continue
      else:
        f+=1
    if f==0:
      subtract=int(subtract)
      negative.append(subtract)
      value=True
    else:
      print("\ninvalid input")
  print("\n________________________")
def add_credits(positive_credit_list):
  numbers=["1","2","3","4","5","6","7","8","9","0"]
  value=False
  while value==False:
    add_credits=input("How many credits do you want to add: ")
    f=0
    for credit in add_credits:
      if credit in numbers:
        continue
      else:
        f+=1
    if f==0:
      add_credits=int(add_credits)
      positive_credit_list.append(add_credits)
      value=True
    else:
      print("\ninvalid input")
  print("\n________________________")
#
def subtract_credits(negative_credit_list):
  numbers=["1","2","3","4","5","6","7","8","9","0"]
  value=False
  while value==False:
    subtract_credits=input("How many credits do you want to subtract?: ")
    f=0
    for credit in subtract_credits:
      if credit in numbers:
        continue
      else:
        f+=1
    if f==0:
      subtract_credits=int(subtract_credits)
      negative_credit_list.append(subtract_credits)
      value=True
    else:
      print("\ninvalid input")
  print("\n________________________")
name= input(f"{color}What is your name?: ")
print(f"Hello {name.title()}")
game=True
#Moving forward with options
while game==True:
  options()
  question=input("\nchoose an option: ")
  if question.lower()=="add credits":
    add_credits(positive_credit_list)
    print("Adding credits..........")
    time.sleep(1)
    print("25%.....................")
    time.sleep(1)
    print("50%.....................")
    time.sleep(1)
    print("75%.....................")
    time.sleep(1)
    print("99% almost done.........")
    time.sleep(1)
    print("\nwe have added your credits")
    print(sum(positive_credit_list)-sum(negative_credit_list))
    time.sleep(3)
    c()
  elif question.lower()=="subtract credits":
    subtract_credits(negative_credit_list)
    print("subtracting credits.....")
    time.sleep(1)
    print("25%.....................")
    time.sleep(1)
    print("50%.....................")
    time.sleep(1)
    print("75%.....................")
    time.sleep(1)
    print("99% almost done.........")
    time.sleep(1)
    print("\nwe have subtracted your credits")
    print(sum(positive_credit_list)-sum(negative_credit_list))
    time.sleep(3)
    c()
  elif question.lower()=="add age":
    minimum_age(age_required)
    print("Adding your age.....")
    time.sleep(1)
    print("25%.....................")
    time.sleep(1)
    print("50%.....................")
    time.sleep(1)
    print("75%.....................")
    time.sleep(1)
    print("99% almost done.........")
    time.sleep(1)
    print("\nWe have added your age")
    print(sum(age_required)-sum(negative))
    time.sleep(3)
    c()
  elif question.lower()=="________________________":
    subtract(negative)
    print("please type 0.....")
    time.sleep(1)
    print("25%.....................")
    time.sleep(1)
    print("50%.....................")
    time.sleep(1)
    print("75%.....................")
    time.sleep(1)
    print("99% almost done.........")
    time.sleep(1)
    print("\nWe have added your age")
    print(sum(age_required)-sum(negative))
    time.sleep(3)
  elif question.lower()=="make a bank account":
    while account==False:
      print("checking your age.....")
      time.sleep(1.5)
      print("33%.....................................")
      time.sleep(1.5)
      print("66%.....................................")
      time.sleep(1.5)
      print("99%.....................................")
      time.sleep(1.5)
      if sum(age_required)-sum(negative) >= 18:
        print("you are old enough to get an account")
        time.sleep(1.5)
        last_name=input("What is your last name?: ")
        time.sleep(1.5)
        print("Making you an account...................")
        time.sleep(1.5)
        print("36%.....................................")
        time.sleep(1.5)
        print("66%.....................................")
        time.sleep(1.5)
        print("99%.....................................")
        time.sleep(1.5)
        print("We made you an account")
        time.sleep(3)
        account=True
        c()
        break
      else:
        age=(18 - (sum(age_required) - 
 sum(negative)))
        print(f"you are not old enough to make an account\nyou need to be {age} more years older")
        time.sleep(4)
        c()
        break
  elif question.lower()=="make a credit account":
    while account==False:
      print("checking if you have enough credits.....")
      time.sleep(1.5)
      print("33%.....................................")
      time.sleep(1.5)
      print("66%.....................................")
      time.sleep(1.5)
      print("99%.....................................")
      time.sleep(1.5)
      if sum(positive_credit_list)-sum(negative_credit_list) >= 800:
        print("you have enough credits")
        time.sleep(1.5)
        last_name=input("What is your last name?: ")
        time.sleep(1.5)
        print("Making you an account...................")
        time.sleep(1.5)
        print("36%.....................................")
        time.sleep(1.5)
        print("66%.....................................")
        time.sleep(1.5)
        print("99%.....................................")
        time.sleep(1.5)
        print("We made you an account")
        time.sleep(3)
        account=True
        c()
        break
      else:
        need=(800 - (sum(positive_credit_list) - 
 sum(negative_credit_list)))
        print(f"you have non-sufficient credits\nyou need {need} more credits")
        time.sleep(4)
        c()
        break
    else:
      time.sleep(1)
      print("Our status shows you arleady have an account\nYou can check your account")
      time.sleep(3)
      c()
  elif question.lower()=="check account":
    print("Searching for account: ")
    time.sleep(2)
    print("1%.....................")
    time.sleep(2)
    print("49%....................")
    time.sleep(2)
    print("73%....................")
    time.sleep(2)
    print("100%...................")
    time.sleep(2)
    while account==True:
      print("Getting your information")
      time.sleep(2)
      print("25%....................")
      time.sleep(2)
      print("50%....................")
      time.sleep(2)
      print("75%....................")
      time.sleep(2)
      print("98%...................")
      time.sleep(2)
      if sum(positive_credit_list)-sum(negative_credit_list) >= 800:
        print(f"Name: {name.title()}\nlast_name: {last_name.title()}\ncredits: {sum(positive_credit_list)-sum(negative_credit_list)}")
        time.sleep(3)
        c()
        break
      else:
        need=(800 - (sum(positive_credit_list) - 
 sum(negative_credit_list)))
        print(f"\nyour account got blocked due to non-sufficient funds\nIn order to get it back get back you need {need} more credits")
        time.sleep(4)
        c()
        break
    else:
      print("\nyou don't have an account yet, Create an account")
      time.sleep(3)
      c()
      break
  elif question.lower()=="exit":
    time.sleep(2)
    c()
    break
  else:
    print("\nThat is a invalid option")
    time.sleep(1)
    c()
print(f"Thank you {name.title()} for choosing our bank\n\nHope you have a good day")