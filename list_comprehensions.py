#The big idea
#A list comprehension is just a for loop squeezed into one line that builds a list.
# in simple loop we did this 
for n in range(5):
    print(n*n)
    
    
#in list_comprehensions
squares = [n*n for n in range(5)]
print(squares)