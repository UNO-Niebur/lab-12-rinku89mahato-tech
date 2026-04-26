# SearchSortLab.py
# Name:Rinku Mahato
# Date:04/26/2026
# Assignment: Lab 13 – Searching and Sorting
#Part 4 – Reflection Questions
#Which list was easiest to sort? Why? Sorted list was the easiest to sort due to it needs very few swaps.
# Which list required the most work? Reverse list required the most work because random list is still partially correct in position.
# Why is sorting useful before searching? Sorting is useful for binary search.
# When might linear search still be useful? linear search is useful for unsorted data.

def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""
    
    # TODO: implement linear search
    for i in range(len(data)):
        if data[i] == target:
            return i
    
    return -1


def bubbleSort(data):
    """Sort the list using bubble sort and return the sorted list."""
    
    # TODO: implement bubble sort
    n = len(data)

    for pass_num in range(n-1):
        for i in range(n - 1 - pass_num):
            if data[i] > data [i + 1]:
                data[i], data[i + 1] = data [i +1], data[i]

    
    return data


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 10 in randomList:", linearSearch(randomList, 10))

    # Test sorting
    print("Sorted list:", bubbleSort(sortedList.copy()))
    print("Reversed list sorted:", bubbleSort(reversedList.copy()))
    print("Random list sorted:", bubbleSort(randomList.copy()))


if __name__ == "__main__":
    main()
