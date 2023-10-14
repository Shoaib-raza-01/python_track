# decorators are a concept where a function is passes to a function as a parameter 
# this is done to add extra functionality to the existing function without touching the function 

def div(a,b):
    print(a/b)

def smart_div(func):

    def inner_func(i,j):
        # add the extra functionality here
        if i<j:
            i,j = j,i
        # return here the function taken as parameter with updated values
        return func(i,j)
    
    return inner_func

# calling the new defined function with the existing function as parameter
divide = smart_div(div)
divide(2,4)