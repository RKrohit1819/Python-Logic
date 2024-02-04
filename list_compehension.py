# my_list=[]

# for i in range(1,21):
#     my_list.append(i)
    
# print(my_list)

# my_list = ["Even" if i%2 ==0 else "Odd"  for i in range (1,21)]
# print(my_list)

# my_list = [i for i in range (1,21) if i % 5 == 0]
# print(my_list)

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))


my_list = [i for i in range (start,end) if i %2==0 and i %3==0]
print(my_list)