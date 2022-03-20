# n=input()
# nn=int(n*2)
# nnn=int(n*3)
# print("{} + {} + {} = {} ".format(n,nn,nnn,int(n)+nn+nnn))

# x,op,y=int(input()),input(),int(input())

# if op=='+':
#     print("{}".format(x),op,"{} = {}".format(y,x+y)) 
# elif op=='-':
#     print("{}".format(x),op,"{} = {}".format(y,x-y))
# elif op=='*':
#     print("{}".format(x),op,"{} = {}".format(y,x*y))
# elif op=='/':
#     print("{}".format(x),op,"{} = {}".format(y,x/y))


eq=input()
print(eval(eq))