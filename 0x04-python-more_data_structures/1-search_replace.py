def search_replace(my_list, search, replace):
    if not my_list :
        return
    else:
        new = []
        new = my_list.copy()
        for i, j in enumerate(my_list):
            if j == search:
                new[i] = replace
        return (new)
