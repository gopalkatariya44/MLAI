def nested_list_to_flat_list(_list):
    for i in _list:
        if type(i) == list:
            for j in i:
                if type(j) == str:
                    print('', end='   ')
                    print(j)
                else:
                    print(j)
        else:
            if type(i) == int:
                print(i)
            else:
                print('  ', i)

nested_list = [1, "2", 3, 
              ['a', 'b', 'c'], 
              4, 5, 6, 
              ['d', 'e', 'f'], 
              7, 'g', 8, 'h', 
              [9, 10, 'i', 'j'], 
              11, 'k']

nested_list_to_flat_list(nested_list)