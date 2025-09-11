def  is_prim(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
print(is_prim(11))
#---------------------------------------------------
def calculator(a, b, operation):
    operations={"add":a+b,
               "subtract":a-b,
               "multiply":a*b,
               "divide":a/b}
    return operations.get(operation)
print(calculator(5,3,"add"))
print(calculator(5,3,"subtract"))
print(calculator(5,3,"multiply"))
print(calculator(5,3,"divide"))