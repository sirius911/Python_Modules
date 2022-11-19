from generator import generator

print(">> text = \"Le Lorem Ipsum est simplement du faux texte.\"\n\
>> for word in generator(text, \" \"):\n\
...\tprint (word)")
text = "Le Lorem Ipsum est simplement du faux texte."

for word in generator(text, " "):
    print (f"\033[92m{word}\033[0m")

print("\n>> for word in generator(text, \" \",option = \"shuffle\"):\n\
...\tprint (word)")
for word in generator(text, " ",option = "shuffle"):
    print (f"\033[92m{word}\033[0m")

print("\n>> for word in generator(text, \" \",option = \"ordered\"):\n\
...\tprint (word)")
for word in generator(text, " ",option = "ordered"):
    print (f"\033[92m{word}\033[0m")

print("\n>> text = \"Lorem Ipsum Lorem Ipsum\"\n\
>> for word in generator(text, \" \",option = \"unique\"):\n\
...\tprint (word)")
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, " ",option = "unique"):
    print (f"\033[92m{word}\033[0m")

print("\n>> text = 1.0\n\
>> for word in generator(text, \".\"):\n\
...\tprint (word)")
text = 1.0
for word in generator(text, "."):
    print (f"\033[92m{word}\033[0m")

print("\n>> for word in generator(\"abcd efgh\", 5):\n\
...\tprint (word)")
for word in generator("abcd efgh", 5):
    print (f"\033[92m{word}\033[0m")

print("\n>> for word in generator(\"abcd efgh\", \" \", \"badOption\"):\n\
...\tprint (word)")
for word in generator("abcd efgh", " ", "BadOption"):
    print (f"\033[92m{word}\033[0m")

print("\n>> for word in generator(\"abcd efgh\", \" \", 0):\n\
...\tprint (word)")
for word in generator("abcd efgh", " ", 0):
    print (f"\033[92m{word}\033[0m")