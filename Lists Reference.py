#!/usr/bin/env python
# coding: utf-8

# # Lists
# - ordered sequence
# - multiple data elements
# - multiple data types
# - mutable
# - iterable

# ## Creating a list

# #### using [ ]

# In[1]:


list1 = [1, 3, 6.8, True, 9]
print('list1: ' , list1)
print("type(list1): " , type(list1))


# #### using list( )

# In[2]:


list2 = list((1, 3, 'dawn', 6, 8, 'dusk', 9))
print('list2: ' , list2)
print("type(list2): " , type(list2))


# ##### using range()

# In[3]:


#giving and printing the range and its type
list_range = range(20)
print('list_range: ' , list_range)
print("type(list_range): " , type(list_range))

#converting the range into list
list3 = list(list_range)
print("List from range: ", list3)
print(type(list3))


# ## Nested Lists
# - lists wihin the list
# - Many elements
# - Multiple data types

# In[4]:


nest_li = [12, 3.4, 'apple', ['Universe', ['Stars', 'Satellite']], 'Direction', [True, 0.9]]
print('Nested list:' , nest_li)
print("type of nested list: " , type(nest_li))
print("Length of the outer list: ", len(nest_li))


# ## Accessing Elements
# - Syntax:
#           
#       list_name [index_outer_list] [index_inner_list1]...[index_inner_list_n]

# In[5]:


print('list1[2]: ', list1[2])
print('list2[5]: ', list2[5])
print('list3[14]: ', list3[14])


# In[6]:


print('Nested list:',nest_li)
print('nest_li[5]: ', nest_li[5])
print('nest_li[5][1]: ', nest_li[5][1])
print('nest_li[3][1]:',nest_li[3][1])
print('nest_li[3][1][1]: ', nest_li[3][1][1])


# ## Slicing

# In[7]:


A = [41, 45, 89, 82, 'dg', 'kjh', 'gfhgf', '45h', '4hk', 54]
print("List A : ", A)
print('len(A): ', len(A))


# In[8]:


print(A[3 : 8]) 
print(A[ : 5])
print(A[6 : ])
print(A[4 : len(A)])
print(A[3 : 20])


# In[9]:


print(A[-4 : ])
print(A[-2 : -6 : -1])
print(A[-1 : -5])        #this will not give any result
print(A[-1 : -5 : -1])   #we have give negative step size for the above 
print(A [-8 : -1 : -1])
print(A[-1 : -8 : -1])


# ### Lists Mutability

# In[10]:


#lists are mutable
print('Orignal List:', A)
print('ID of original list: ', id(A))

A[3] = 100
print('Modified List:', A)
print('ID of list after change: ', id(A))


# ## Adding Elements to the list

# ### append() function
# - Syntax
#         
#         list_name.append(element)
# - appends the specified element at the last index of the list
# - takes one parameter to be added
# - could be one element or one nested list

# In[11]:


print("Original List:" , A)
print('Length of original list: ', len(A))

#appending one element to the list
A.append('cat12')
print("List after appending " , A)
print('Length of list, now: ', len(A))


# In[12]:


#append function is used to add only one element in the list at the end , it cannot add more than one element
A.append(3, 6, 'Multiple')      #this will give us error
print("Modified list :", A)
print('Length of list, now: ', len(A))


# ### extend() function
# - Syntax
# 
#        List_name.extend([element1, element2, ..., element n])
# - extends the list with the specified elements at the last index

# In[13]:


print("Original List: " , A)
print('Length of list, now: ', len(A))

#extend function is used to add multiple elements in the list at the end
A.extend(['rabbit','ball'])
print('List After extending' , A )
print('Length of list, now: ', len(A))


# ### insert() function
# - Syntax
#    
#       List_name.insert(index, element)
# - inserts the specified element at the particular index and shifts all the other elements at the successive index values 

# In[14]:


print("Original List: " , A)

#insert function is used to insert any element at a specific index
A.insert(3,"apple")
print('List After inserting: ' , A )


# In[15]:


# inserting a nested list as one element
print("Original List:" , A)

A.insert(7,['Dog','puppy'])
print("Modified List:" , A )


# # Deleting Elements from list

# ### remove() function
# - Syntax
#  
#      list_name.remove(element)
# - Removes the specified element from the list

# In[16]:


print("Original List:" , A)

A.remove(100)
print("\nList after removing 100 :" , A )

A.remove(['Dog' , 'puppy'])
print("\nList after removing ['Dog' , 'puppy']:" , A )


# ### pop() function
# - Syntax
# 
#       list_name.pop(index = optional)
# - by default, it will remove the element at the last index, like in a stack
# - pop() function gives the popped element as the output which can also be stored in some variable for further use.

# In[17]:


print("Original List: " , A)

#it will remove the last element
A.pop()
print("After:" , A )


# In[18]:


#by giving index value it will remove that specific element
popped_value = A.pop(7)
print('popped_value: ', popped_value)
print('List:',A)


# In[19]:


# using the popped value again to insert in the list
A.append(popped_value)


# In[20]:


print(A)


# ### del function
# - Syntax 
# 
#       del list_name[index]
# - deletes the elements of the specified index
# - useful to delete a slice of the list
# - can also delete the instance of the list

# In[21]:


print('List: ', A)
del A[3]
print('After deleting:', A)

del A[3 : 5]
print('After deleting A[3 : 5]:', A)


# In[22]:


#it will delete the list
del A
print(A) #this will give error as our list A is deleted


# ## Sorting

# ##### using sort() function

# In[24]:


L = [12,3,40, 590, 454, 89, 7678]
print("Original List: ", L)

#sorting list -it will be automatically sorted to ascending order
L.sort()
print("List after sort(): ", L)


# In[25]:


L = [12,3,40, 590, 454, 89, 7678]
print("Original List: ", L)

#sorting list in descending order
L.sort(reverse = True)

print("\nList after sorting in descendig order: ", L)


# ##### using sorted() function

# In[26]:


L = [12,3,40, 590, 454, 89, 7678]
print("Original List: ", L)

#sorting the list using sorted() function
print("\nsorted(L): ", sorted(L))

#sorted function will no change the original list
print("\nList after sorted(L): ", L)


# In[30]:


alphabets = ['a', 'u', 'd' , 'g' , 'o' , 'c' , 'm' , 'q']
print("List is :", alphabets)
print("\nSorted list :", sorted(alphabets))
print("\nList is :", alphabets)


# In[31]:


#sorting in ascending order
(alphabets.sort())
print(alphabets)

#sorting in descending order
(alphabets.sort(reverse = True))
print(alphabets)


# In[32]:


# Sorting of strings takes place in lexographically(dictionary format)
str = ["my", "mine", "you", "your", "us", "our"]
str.sort()
str


# ###### Priority for ascending order on the basis of first character:
# - numbers < capital letters < small letters

# In[33]:


str_num = ["1my","A" ,"mine3",'$D', '@w' ,"You", "your", "us", "ou2r"]
str_num.sort()
str_num


# ### Some methods of list

# In[34]:


#this will give the index of the element
str_num.index('us')


# In[35]:


#this will clear all the elements of the list and give empty list
str_num.clear()
str_num


# In[38]:


#this is used to make the copy of list
str_num=[2,4,6,8,2,10]
str_num2 = str_num.copy()
str_num2


# In[39]:


#this will count the occurance of the element
str_num.count(2)

Operators : + and *
# In[41]:


#joining two lists
a = [1,2,3,4]
b=[4,5,6]
new_list=a+b
print(new_list)


# In[44]:


#checking if the item exists in list or not
print(7 in new_list)
print(3 in new_list)


# In[48]:


#this is how to take a list from the user
#eval function will convert the input into a list if we use [] brackets
List =eval(input('Enter a list:'))
print(type(List))
print(List)


# In[ ]:




