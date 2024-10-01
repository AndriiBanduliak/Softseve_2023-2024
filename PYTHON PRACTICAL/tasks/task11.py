# type your code here
def logger(func):
    def wrapper(*args, **kwargs):
        # Convert all positional and keyword arguments to strings for logging
        args_list = [str(arg) for arg in args]
        kwargs_list = [str(v) for v in kwargs.values()]
        
        # Combine args and kwargs into one list for printing
        all_args = args_list + kwargs_list
        
        # Print function execution message with arguments
        print(f"Executing of function {func.__name__} with arguments {', '.join(all_args)}...")
        
        # Execute the original function and return the result
        return func(*args, **kwargs)
    return wrapper

@logger
def concat(*args, **kwargs):
    # Concatenate all positional and keyword arguments into a single string
    result = ''.join(map(str, args)) + ''.join(map(str, kwargs.values()))
    return result
    
    
@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)