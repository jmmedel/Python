

"""

Python - Searching Algorithms

Searching is a very basic necessity when you store data in different data structures. The simplest appraoch is to go across every element in the data structure and match it with the value you are searching for. This is known as Linear search. It is inefficient and rarely used, but creating a program for it gives an idea about how we can implement some advanced search algorithms.

Linear Search
In this type of search, a sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data structure.



"""

def linear_search(values, search_for):
    search_at = 0
    search_res = False

# Match the value with each data element	
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1

    return search_res

l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))
print(linear_search(l, 91))


"""

When the above code is executed, it produces the following result −

True
False


"""

