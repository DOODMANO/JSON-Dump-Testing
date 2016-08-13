import json

filename = "dictori.dict"
choice = input("dump or load and print, 1 or 2, 3 to see empty current dictionary:\n")
#global diction
diction = {}
if choice == '1':
    diction = {'yummy': 150, 'pizza': 750}
    save = open(filename, 'w')
    json.dump(diction, save)
    save.close()
    print("dictionary was dumped")
elif choice == '2':
    try:
        load = open(filename, 'r')
        diction = json.load(load)
        load.close()
        print(diction)
    except IOError:
        print("file has to be saved first")
elif choice == '3':
    print(diction)
else:
    print("oops its not 1 2 or 3")

