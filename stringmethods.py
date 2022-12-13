a="!!cYBorg ! !" #strings are immutable
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))# it removes any trailing characters like!,question mark etc which are present after the string
print(a.replace("CYBorg","Ace"))#it replaces all the strings in the given statements
print(a.split(" "))#it splits the given string at the specified instance and returns the separated strings as list items
b= "tex"
c="dance"
print(c.capitalize())#it converts the first letter in uppaercase and reamining all in lower case
print(b.center(50))#it aligns the text to center.here the number represents the length of string after center aligning the given text
print(a.endswith("!"))#it checks whether a given string ends whether a given string ends with a given character and returns true or flase as output
print(a.endswith("g",2,7))#here ny slicing the string we can also check for a given character in a string
print(a.count("!"))#it counts the no. of times a given character occurs
print(a.find("Y"))#it can used to find the index for a character in a string and if the character is not found it reurns a value -1
print(a.index("Y"))#it is also same as find but in case a given character is not found it generates an error
print(a.isalnum())#it returns true only if the entire string consists of alphabets and numbers if any other punctuations are present then it reurns false
print(a.isalpha())#it returns tru only if the string has alphabets and reurns false if any other numbers or punctuations are there
print(a.islower())#returns tue only if all letters are in lower case
print(a.isprintable())#returns true only if all characters in the string are printable and returns false if things like /n etc are present
print(a.isspace())#returns true only if spaces are present in string
print(a.istitle())#reurns true only if the first letter is capitalized
print(a.isupper())#returns true only if all characters are capitalized
print(a.startswith("!"))#returns true if the given string starts with the given character
print(a.swapcase())#changes lower to upper and upper to lower
print(b.title())#changes the first characters of the letters of the string to uppercase
