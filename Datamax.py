# data-max-internship-assignment

#Data Max Internship Assignment

## Contact Details
#<Johan> <`Bandilli> 
#<bandillijoan@live.com>


#Task: Write a program to solve the following problem:
#You wrote down the numbers from 1 to `n`, in order, on a whiteboard. 
#When you weren’t paying attention, a student erased one of the numbers.
#Can you find the missing number?

#Krijojm array me numrin e leemtneve 

arr = [1,2,3,4,5,6,7,9,10]
missing_elements = []

for ele in range(arr[0], arr[-1]+1):
    if ele not in arr:
        missing_elements.append(ele)

print(missing_elements)

