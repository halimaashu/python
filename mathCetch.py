#  in python we can write is match case but is js its same logic but syntax is defarence 

x=int(input("Enter a number up to 4 and down to 1: "))
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case _:
        print("Not limited number Sorry try again")