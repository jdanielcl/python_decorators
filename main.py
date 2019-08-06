def decorator_function(function_to_decorate):

    # args: arguments
    # kwargs: keyword arguments
    def inner_function(*args, **kwargs):
        print("before function call")
        function_to_decorate(*args, **kwargs)
        print("after function call")
    
    return inner_function

@decorator_function
def function_one(n,m):
    print(n+m)

@decorator_function
def function_two(n,m):
    print(n*m)


function_one(5,6)

#function_two()