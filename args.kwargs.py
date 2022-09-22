def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)
    
def func2(arg1 = None, arg2 = None, arg3 = None):
    print(arg1, arg2, arg3)
    
args = [1, 2, 3]
kwargs = {"arg2" : 2, "arg1" : 1, "arg3" : 3}

func1(*args)
func2(*kwargs)
func2(**kwargs)