# a function finally!
def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1, arg2))

# *args is strange!
def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))

def print_one(arg1):
    print("arg1: {}".format(arg1))

def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("first")
print_none()
