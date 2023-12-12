global_var = 10


def print_global():
    print("Global variable inside function:", global_var)


def modify_global():
    global global_var
    global_var += 5
    print("Modified global variable inside function:", global_var)


print_global()
modify_global()
print("Global variable outside function:", global_var)
