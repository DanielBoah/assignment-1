my_list=["apple","banana","cherry","date","banana"]
print(f"Initial List: {my_list}")
#del operation
del my_list[2]
print(F"After del my_list[2]:{my_list}")
#append operation
my_list.append("grape")
print(f"After my_list.append('grape') :{my_list}")
#extend operation
my_list.extend(["kiwi","lemon"])
print(f" after my_list.extend(['kiwi','lemon']) :{my_list} ")
#insert operation
my_list.insert(1,"orange")
print(f"After my_list.insert(1,'orange') : {my_list}")
#pop opertion
popped_item=my_list.pop()
print(f"After pop(): {my_list},popped item:{popped_item}")
#remove operation
my_list.remove("banana")
print(f"After my_list.remove('banana'): {my_list}")
#revers operation
my_list.reverse()
print(F"after reverse():{my_list}")
#sort operation
my_list.sort()
print(f"After sort():{my_list}")
#TUPLES
#access tuple items
my_tuple=("red","green","blue","green","yellow")
print(f"ELemnt at index 0:{my_tuple[0]}")
print(f"Elements from index 1 to 3 :{my_tuple[1:4]}")
#attempt to change tuple
my_tuple[0]="purple"
print(f"Attempt to change: {my_tuple}")
#loop through a tuple
print(f"looping through a tuple")
for item in my_tuple:
    print(item)
#count operation
green_count=my_tuple.count("green")
print(f"count of 'green':{green_count}")
#index operation
blue_index=my_tuple.index("blue")
print(f"index of 'blue':{blue_index}")
#length of a tuple
tuple_length=len(my_tuple)
print(f"Tuple length:{tuple_length}")

#SETS DATA STRUCTURE
my_sets={"apple","banana","cherry","date"}
my_sets.add("grape")
#remove operation
my_sets.remove("banana")
#length of set
set_length=len(my_sets)
print(f"length of set :{set_length}")
#item in x operation(membership operation)
is_cherry_in_set="cherry"in my_sets
print(f"is 'cherry' in my set ? :{is_cherry_in_set}")
#checking mango in my set
is_mango_in_set="mango" in my_sets
print(f"is 'mango' in my set ?:{is_mango_in_set}")
#pop operation
popped_set_item=my_sets.pop()
print(f"After pop():{my_sets},popped item: {popped_set_item}")
#clear operation
my_sets.clear()
print(F"After clear():{my_sets}")

#DICTIONARIES STRUCTURES
my_dictionary={"brand":"Ford","Model":"Mustang","year":1964,"color":"red"}
print(f"initial Dictionary: {my_dictionary}")
#acees keys and items
all_keys=my_dictionary.keys()
print(f"All keys:{list(all_keys)}")
#add and changing dictionary items
my_dictionary["engine"]="V8"
print(f"After 'engine':{my_dictionary}")
my_dictionary["colour"]="blue"   
print(f"After changing 'color':{my_dictionary}")
#remove from dictionary item
removed_year=my_dictionary.pop("year")
print(f"After pop('year'):{my_dictionary},Removed year :{removed_year}")
#remove using del
del my_dictionary["brand"]
print(f"After del my_dictionary['brand]:{my_dictionary}")
#length of dictionary
dictionary_length=len(my_dictionary)
print(f"length of the 'dictionary': {dictionary_length}")
#clear operation 
my_dictionary.clear()
print(F"After clear(): {my_dictionary}")