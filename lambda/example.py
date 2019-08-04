
#convert list of string to ints and power each by 2
num_list = ["1","2","3","4"]
result = list(map(lambda x:int(x)**2,num_list))
print(result)

#increment each child list element by 1
list_of_lists = [[3,2,1],[1,7,5],[9,-2,11,6]]
result = list(map(lambda child_list:list(map(lambda x :x+1,child_list)),list_of_lists ))
print(result)


#iterate over list of lists and for each child list leave only even elements
list_of_lists = [[3,2,1],[1,7,5],[9,-2,11,6]]
result = list(map(lambda child_list : list(filter(lambda x : x % 2 == 0,child_list)) ,list_of_lists))
print(result)


import functools

#combine child list to one list
list_of_lists = [[3,2,1],[1,7,5],[9,-2,11,6]]
result = functools.reduce(lambda x,y : x + y,list_of_lists)
print(result)

#iterate over list of lists and for each list leave only even elements and the return one lists containing all of them , use example #3
list_of_lists = [[3,2,1],[1,7,5],[9,-2,11,6]]
result = functools.reduce(lambda x,y : x + y , list(map(lambda child_list : list(filter(lambda x : x % 2 == 0,child_list)) ,list_of_lists)))
print(result)

'''
filter the list with the  condition of  being greter than 10 and being even.After that divide each element by 2.Reduce the whole list 
to a number which is the sum of the elements in the list.
'''
my_list = [1,22,18,7,11,13,8,14]
#use map,filter,reduce methods
#print the result


