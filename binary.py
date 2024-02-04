def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Example usage
if __name__ == "__main__":
    # Sample Input 1
    N1 = 7
    target1 = 3
    A1 = [1, 3, 7, 9, 11, 12, 45]

    result1 = binary_search(A1, target1)
    print(result1)  # Output: 1

    # Sample Input 2
    N2 = 7
    target2 = 9
    A2 = [1, 2, 3, 4, 5, 6, 7]

    result2 = binary_search(A2, target2)
    print(result2)  # Output: -1
