name = input("what's your name: ")
print("that's a good name, " +name+"")
question = input(""+name+", would you like to know about our store hours, locations, available products, or prices, if so plese choose a topic: ")
if question == ('store hours'):
  print('Our store is open from 6:00AM to 12:00PM all week')
if question == ('locations'):
  print('We have 10,000 stores located around the U.S and have many stores near your 10 mile radius')
if question == ('available products'):
  print('We have fresh produce and food items in our stores whith the most trusted brands: ')
if question == ('prices'):
  print('We have afordable prices for the average consumer and offer 10% discounts on the weekends')
end = input('If you are satisfied with our answers plese type stop: ')
if end == ('stop'):
  print('have a good day, '+name+'')
else :
 print('We can not answer your question right now, but you could call our store number for further questions')
