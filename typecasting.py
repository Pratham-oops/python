# typecasting- the  process of converting one data type into another
a=1
b=2 
print(a+b)
a="1"
b="2"
print(a+b)
print(int(a)+int(b)) # explicit conversion- the conversion in which user demands the compiler to forcefully convert into one data type into another data type
                       # syntax  for explicit data type-      required_data_type(name of the variable
#  implicit conversion-According to different data type levels ,the interepreter convertsconverts the lower level data type into another data type on its own in order to prevent the data loss
c=1
d=3.999 # for example- double>float>long int>int(data type levels)
print(c+d)                     