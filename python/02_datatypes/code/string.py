# Create a string "PythonIsFun" and print: First character , Last character ,Characters from index 2 to 6
 
str = "PythonIsFun"

print(f"first char : {str[0]}");
print(f"last char : {str[-1]}");
print(f"2 to 6 index: {str[2:7:1]}")

# Convert a string "openai" into bytes using encode() and back to string using decode

name = "jeet" ;
encoded_str = name.encode("UTF-8");
print(f"encoded str : {encoded_str}");
decoded_str = encoded_str.decode("UTF-8");
print(f"Decoded str : {decoded_str}")

# string are immutable
a= "heee" ;
b= "haa" ;

b=b+"haa"

print(id(a));
print(id(b));