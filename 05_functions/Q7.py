def sum_all(*args):
    f_value=0
    for i in args:
        f_value+=i
    return f_value

# or we can make the function as 

def sum_all_alt(*args):
    return sum(args)