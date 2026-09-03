a = input("enter word: ")

reversed_word = ""

for i in a:
    reversed_word = i + reversed_word 

if reversed_word == a:
    print("yez")
else:   
    print(reversed_word)