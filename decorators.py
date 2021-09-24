#1st we want to creat a decorator function with 1 parameter that can be any function
def outside_function(sample_function):
#hear we want to defind another function in that we will use input parrameter function
    def inside_function(*a,**b):
        print("before excuting the function")
        print(*a,**b)
        sample_function(*a,**b)
        print("after excuting the function")
    #after that we want to return the function otherwise it won't call the function
    return inside_function
#we defind the decorator function now we see how to use that function in another  function
@outside_function
def cal(a,b,c):
    print((a*b)*c)
#now call the function
cal(5,2,5)

