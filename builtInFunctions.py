print(eval("5+3")) # eval - used for single line executions

#exec - used for mutiple line execution
execute = 'print("hi")'
print(exec(execute))

num = 5

print(float(num)) # type cast to flot

print(int(num)) # type cast to int

print(str(num)) # type cast to string

print(dir(num)) # shows all functions associated with respect to the variable

print(abs(-20)) # returns positive value of a number

print(bool(5)) # returns true or false
print(bool(0))
print(bool(None))

print(help(num.__abs__)) # help gives definition of the function