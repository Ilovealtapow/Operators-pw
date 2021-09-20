# # Python Prework 1-5

# # Question 1
# # Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# # The first line of the code has been defined as below.

# def hello_name(user_name):
#     print("Hello_" + user_name.upper())
# hello_name("username")

# # Another solution
# def hello_two(user_name):
#     print("hello " + user_name.upper() + "!")
    
# hello_two('Jordan')


# # Question 2
# # Print first 100 odd numbers in Python.
# odd_numbers = list(range(1, 100, 2))
# print(odd_numbers)

# # Another solution
# for value in range(1, 201, 2):
#     print(value)

# # Another solution- Iterating over list with conditional check.
# odd_nums = list(range(1, 101))

# for number in odd_nums:
#     if number % 2 != 0:
#         print(number)
#     else:
#         print("Even")


# # Question 3
# # Please write a Python function, max_num_in_list to return the max number of a given list.
# # The first line of the code has been defined as below.
# def max_num_in_list(a_list):
#     max = a_list[0]
#     for n in a_list:
#         if n > max:
#             max = n
#     return max
# max_num_in_list([2, 4, 7, 5, 15])

# # Another solution
# def max_in_list(a_list):
#     print(max(a_list))

# max_in_list([2,4,7,10,5,15])

# # Another solution
# def get_max(a_list):
#     a_list.sort()
#     print(a_list[-1])

# get_max([2,4,7,10,5,15])


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
# def is_leap_year(a_year):
#     if a_year % 4 == 0:
#         if a_year % 100 == 0:
#             if a_year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# is_leap_year(2400)

# # # Another solution
# # def is_leap_year(a_year):
# #     if a_year % 4 == 0 and a_year % 100 != 0:
# #         print(f'{a_year} is a leap year')
# #     elif a_year % 400 == 0:
# #         print(f'{a_year} is a leap year')
# #     else:
# #         a_year = False
# #         print(f'{a_year}')

# # is_leap_year(2040)


# # Question 5 ** DID NOT COMPLETE THIS QUESTION IN PREWORK**
# # Write a function to check to see if all numbers in list are consecutive numbers. 
# # For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# # The return should be boolean Type.
# # def is_consecutive(a_list):
# number_list_all = [[1,2,3,4,5,6,7,8], [1,2,4,5], [52, 63, 45, 678]]
# def is_consecutive(a_list):
#     number_check = min(a_list)
#     max_numner = max(a_list)
#     for number in a_list[1:]:
#         if number == max_numner:
#             return True
#         elif number == number_check+1:
#             number_check +=1
#         else:
#             return False
# for list in number_list_all:
#     print("Checking list..." + str(list))
#     print(is_consecutive(list))

# Another solution
# def is_consec(a_list):
#     min_num = min(a_list)
#     max_num = max(a_list)
#     consecutive = list(range(min_num,max_num+1))
#     if a_list == consecutive:
#         return True
#     else:
#         return False

# is_consec([1,2,3,4,5,6,7,8])

# looping by index
# [1,2,3,4,5,6,7,8]
# def consec(a_list):
#     for i in range(len(a_list)-1):
#         if a_list[1] + 1 != a_list[i+2]:
#             return False
#     return True
# consec([1,2,3,4,5,6,7,8])



