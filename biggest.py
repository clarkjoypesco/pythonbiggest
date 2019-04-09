# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def bigger(x,y):
    if x > y :
        return x
    return y

def biggest(x,y,z):
    return bigger(bigger(x,y),z)
    


# def biggest(x,y,z):
#     if x > y and x > z:
#         return x
#     if y > z:
#         return y
#     return z


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 7)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(6, 7, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9