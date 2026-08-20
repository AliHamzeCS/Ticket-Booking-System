from colorama import Fore, Style, init
init()

# Decorator Function        
def decorator_func(title): 
    def actual_decorator(func): 
        def wrapper(*args, **kwargs): 
            print(f'{Fore.MAGENTA}-{title}-{Style.RESET_ALL}\n')
            result = func(*args, **kwargs)
            input('\nPress Enter to continue...')
            return result
        return wrapper
    return actual_decorator