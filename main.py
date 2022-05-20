def multiples_and_greet(*numbers,**student):
    num=1
    for y in numbers:
       num*=y
       print (num)
    print (f"Hello {student}")