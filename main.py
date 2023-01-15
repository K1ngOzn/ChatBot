def dash():
  print("-------------------------------")


print("Welcome to Erik's Shop")
name = input("what is you name?: ")
dash()
print(f"Hello {name}")
print("what can i help you in?")
question = input("-Prices\n-Locations\n-Store Hours\n-Products\n-Exit\n\n")
question.lower()
while question.lower(
) == "prices" or "locations" or "store hours" or "products" or "exit":
  if question.lower() == "prices":
    print(
      "We have afordable prices for the average consumer and offer 10% discounts on the weekends"
    )
    dash()
    question = input(
      "choose something else\n-Prices\n-Locations\n-Store Hours\n-Products\n-Exit\n"
    )
  elif question.lower() == "locations":
    print(
      "We have 10,000 stores located around the U.S and have many stores near your 10 mile radius"
    )
    dash()
    question = input(
      "choose something else\n-Prices\n-Locations\n-Store Hours\n-Products\n-Exit\n"
    )
  elif question.lower() == "store hours":
    print("Our store is open from 6:00AM to 12:00PM all week")
    dash()
    question = input(
      "choose something else\n-Prices\n-Locations\n-Store Hours\n-Products\n-Exit\n"
    )
  elif question.lower() == "products":
    print(
      "We have fresh produce and food items in our stores whith the most trusted brands"
    )
    dash()
    question = input(
      "choose something else\n-Prices\n-Locations\n-Store Hours\n-Products\n-Exit\n"
    )
  elif question.lower() == "exit":
    break
  else:
    print(
      "We can not answer your question right now, but you could call our store number for further questions"
    )
    dash()
    question = input(
      "choose something else\n-Prices\n-Locations\n-Store Hours\n-Available Products\n-Exit\n"
    )
print(f"Thank you {name} for visiting Erik's Shop\nHope to see you soon")