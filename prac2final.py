list2=[7,-34,1.2,"Vihaan",48]
print("----------LIST----------")
print("First two elements : ",list2[0:2])
print("Last two elements : ",list2[3:])
print("First two elements thrice : ",list2[0:2]*3)
print("-----------List Functions---------")
list1=list(range(1,10))
print("List using range : ",list1)
list1.append(12)
list1.append(40)
list1.append(29)
list1.append(34)
print("After appending : ",list1)
list1.sort()
print("Ascending sort is : ",list1)
list1.reverse()
print("Descending sort is : ",list1)
list1.remove(8)
print("List after removing 8 : ",list1)
print("Total number of elements in list : ",len(list1),"\n",list1)
list1.append(5)
list1.append(12)
print("After appending : ",list1)
print("Occurance from the list of 5: ",list1.count(5)," 12: ",list1.count(12)," 2: ",list1.count(2))
print("Max Element : ",max(list1))
print("Min Element : ",min(list1))
print("Index of 6 : ",list1.index(6))

print("\n\n----------Tuple_Read Only List----------")
tp2=(-5,0.5,1,"Vihaan",48)
print("Tupple created is : ",tp2)
print("First two elements : ",tp2[0:2])
print("Last two elements : ",tp2[3:])
print("-----------Tuple Function---------")
tp1=tuple(range(1,10))
print("Tuple using range : ",tp1)
print("Length of tupple : ",len(tp1))
print("Smallest value in tuple : ",min(tp1))
print("Largest value in tuple : ",max(tp1))
print("Occurrence of 5's in tuple : ",tp1.count(5))
print("Occurrence of 15's in tuple : ",tp1.count(15))
print("Reverse sort of tuple : ",sorted(tp1,reverse=True))
print("Final tuple : ",tp1)

print("\n\n----------Dictionaries_key:Value pair----------")
d1={'Name':'Vihaan','Roll. No.':48,'Gender':'M'}
print("Keys from above dictonary : ",d1.keys())
print("Value from above dictonary : ",d1.values())
print("Keys and valus from above dictionary: ",d1.items())
d1.update({'College':'ACE'})
print("Updated list: ",d1)






