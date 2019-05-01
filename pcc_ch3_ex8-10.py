#Exercise 3-8 which focuses on sorting lists for the first time.
seeingTheWorld = ['ireland', 'england', 'japan', 'france', 'israel']
print(seeingTheWorld)
print()
print(sorted(seeingTheWorld))
print()
print(seeingTheWorld)

print()
seeingTheWorld.reverse()
print(seeingTheWorld)
print()
seeingTheWorld.reverse()
print(seeingTheWorld)
print()

seeingTheWorld.sort()
print(seeingTheWorld)

print()
seeingTheWorld.sort(reverse=True)
print(seeingTheWorld)

#Exercise 3-9 which focuses on measuring the length (len) of lists from previous exercise
print()
dinnerGuests = ['Bob the Builder', 'J.R. Tolkein', 'John']
#len(dinnerGuests) - This didn't work since I am not actually working in python
print(len(dinnerGuests))
print()

#Exercise 3-10 - Create a master list and use every function from this chapter on it

statesAmerica = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
print(statesAmerica)

print()
print(statesAmerica[3].title())
print()

statesAmerica[-1] = 'Britain'
print(statesAmerica)
print()

statesAmerica.append('Paris')
print(statesAmerica[-1])
print()

statesAmerica.insert(0, 'South Michigan')
print(statesAmerica[0])
print()

print('Unfortunately, it looks as if ' + statesAmerica.pop(2) + ' is no longer a state...')
print()
print(statesAmerica)
print()

statesAmerica.remove('Paris')
print()

statesAmerica.sort()
print(statesAmerica[-1])
print()

statesAmerica.reverse()
print(statesAmerica)
