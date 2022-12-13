# String- is a sequence of array of textual data.in pyhton anyhting enclosed betweeen single  or double quotes is String
name="abcd"
name1='b'
print(name + name1)
# for multiple line strings- we can use ''' .....  '''
m=''' hi
hello 
hey'''
print(m)
# one can access parts of string by sing its index whixh starts from zero
# square brackets can be used to acces elements of string  syntax-   name_of_string[number_of_index]
print(name[2]) 
# for multiline strings we use a for loop 
# syntax:-
 #  (for character in string_name:
    # code)
for character in m:
        print(character)