def countLetters(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count+=1
    return count

print(countLetters("banana", "a"))
print(countLetters("hello", "l"))
print(countLetters("world", "d"))

def repeater(string,integer):
    message = string*integer
    return message

print(repeater("hello",3))

def nameSwap(name1,name2):
    name1List = name1.split()
    name2List = name2.split()
    newName1 = name1List[0] + " " + name2List[1]
    newName2 = name2List[0] + " " + name1List[1]
    return newName1, newName2

print(nameSwap("Cashier Bot", "Jason Douglas"))
print(nameSwap("John Doe", "Jane Smith"))
print(nameSwap("Bob Ross", "Spongebob Squarepants"))