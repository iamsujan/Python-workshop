dict = { 1: 2, 3: 4, 5: 6}
a = input("Enter a key to check : ")
_key = int(a)

if _key in dict:
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')