# def bubble_sort(elements):
#     size = len(elements)
 
#     for k in range(2):
#         for i in range(size-1):
#             if elements[i] > elements[i+1]:
#                 tmp = elements[i]
#                 elements[i]  = elements[i+1]
#                 elements[i+1] = tmp
        
        
        
# if __name__ == '__main__':
#     elements = [5,9,2,1,67,34,88,34]
    
    
#     bubble_sort(elements)
#     print(elements)

# sorted all the elments 
# def bubble_sort(elements):
#     size = len(elements)
 
#     for i in range(size-1):
#         for j in range(size-1):
#             if elements[j] > elements[j+1]:
#                 tmp = elements[j]
#                 elements[j]  = elements[j+1]
#                 elements[j+1] = tmp
        
        
        
# if __name__ == '__main__':
#     elements = [5,9,2,1,67,34,88,34]
    
    
#     bubble_sort(elements)
#     print(elements)

# you can use this to sort strings too
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)
    
    
    