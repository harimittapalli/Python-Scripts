def bin_search(arr: list, element: int, starting_i:int, ending_i:int, *args, **kwargs):

    if ending_i >= starting_i :
        mid = starting_i + (ending_i - starting_i)//2

        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return bin_search(arr, element, starting_i, mid-1)
        else:
            return bin_search(arr, element, mid+1, ending_i)

    return element


if __name__ == "__main__":
    arr = [int(w) for w in input("enter the list of numbers seperated by space :").split(' ')]
    element = int(input("enter the element to be found in array: "))

    print(bin_search(arr, element, 0, len(arr)-1))