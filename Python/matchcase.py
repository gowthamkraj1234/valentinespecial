string="John Doe"
string_operation='changetoupper'
match string_operation:
    case 'reverse':
        print(string[::-1])
    case 'substring':
        print(string[0:4])
    case 'changetoupper':
        print(string.upper())
    case _:
        print("Requested Operation Unavailable")


some_list=[1,2,4,3,6,5,7,8,9]
list_operation='sort'
match list_operation:
    case 'even_odd':
        if len(some_list)%2==0:
            print(f"Length of the list before conversion is {len(some_list)} (EVEN)")
            some_list.append(10)
            print(f"Length of the list after conversion is {len(some_list)} (ODD)")
        else:
            print(f"Length of the list before conversion is {len(some_list)} (ODD)")
            some_list.append(10)
            print(f"Length of the list after conversion is {len(some_list)} (EVEN)")

    case 'append':
        some_list.append([11,12,13,14,15])
        print("After Append:",some_list)
    case 'sort':
        some_list.sort()
        print("Sorted list:",some_list)
    case _:
        print("Invalid Operation")