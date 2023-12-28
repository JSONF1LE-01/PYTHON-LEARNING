friends =["alex", "felipe", "steve", "keyla", "gary", "dany"]
#lists can be any value and it will be fine
print(friends[1])
#you can use negative number for index
print(friends[1:4])
#from 1 to 4 not including 4
#you can also change list values
friends[1] = "mike"
print(friends[1])
#LISTS FUNCTIONS
lucky_numbers = [2, 6, 3, 7, 8, 9, 10, 12,90]
Friends = ["keyla", "nagatoro", "paisen", "alex", "felipe", "aroldo", "kevin", "dany", "gary"]
#extend() function will alow you to append two list together
Friends.append("apolo")
Friends.extend(lucky_numbers)
print(Friends)
#insert(index, value you want to add)
Friends.insert(5, "creed")
print(Friends)
Friends.remove("paisen")
print(Friends)
#clear() removes everything from the list
#pop() removes the last element from a list
#index() gives you the index of the value you want
#count() counts the value that you select
#sort() will order the list in alfabetical order
#reverse() same as sort but in reverse
Friends2 = Friends.copy()
print(Friends2)