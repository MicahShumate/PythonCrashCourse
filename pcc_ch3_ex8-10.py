dinnerGuests = ['Bob the Builder', 'J.R. Tolkein', 'John']
message = "I would be honored if you would join me for dinner, "

print (message + dinnerGuests[0])
print (message + dinnerGuests[1])
print (message + dinnerGuests[2])

#print (message + dinnerGuests)

print (message, *dinnerGuests, sep=', ')
print()
#dinnerGuestsPopped = dinnerGuests.pop(1)
print ('Unfortunately, it looks like ' + dinnerGuests.pop(1) +' will not be able to make it.')
print()
dinnerGuests.insert(1, 'C.S. Lewis')
print()
print (message + dinnerGuests[0])
print (message + dinnerGuests[1])
print (message + dinnerGuests[2])



#Found a larger table so we are inviting more people
print()
print('Good news folks, we have a larger table!')
dinnerGuests.insert(0, 'Davy Crocket')
dinnerGuests.insert(2, 'Napoleon')
dinnerGuests.append('Pope Francis')

#Need to re-invite everyone to dinner
print()
print (message + dinnerGuests[0])
print (message + dinnerGuests[1])
print (message + dinnerGuests[2])
print (message + dinnerGuests[3])
print (message + dinnerGuests[4])
print (message + dinnerGuests[5])
print()
print (message, *dinnerGuests, sep=', ')



#Looks like the table won't arrive in time for dinner. Tryouts! 
print()
print('Looks like the table will only fit two of you, time to battle to the death...')
print('Sorry, ' + dinnerGuests.pop(2) + ' it appears that you have died')
print('Sorry, ' + dinnerGuests.pop(4) + ' it appears that you have died')
print('Sorry, ' + dinnerGuests.pop(0) + ' it appears that you have died')
print('Sorry, ' + dinnerGuests.pop(1) + ' it appears that you have died')

#two survived
print()
print('Some good news for you two though, ', dinnerGuests[0], ' and', dinnerGuests[1], ' have survived. You are welcome to join me for dinner!')


del dinnerGuests[0:2]
print(dinnerGuests)