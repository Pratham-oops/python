name="ash,gary"
print(name[0:3]) #here the end index whcih here is 3 specifies that the string will be printed till 2 and three wouldn't be included .Thus mterms till n-1 are printed
print(len(name))#here len is a function which dteremines the characters in a string
len1=len(name)
print("name is a",len1,"letter word.")
print(name[:3])
print(name[0,-3]) #here the complier interprets the -3 as "len(name)-3"
print(name[-3,-1])

