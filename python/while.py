#peferect number
num=6
x=1
sum=0
while x<=num//2:
    if num%x==0:
        print(x)
        sum+=x
    x+=1
if sum==num:
    print('it is a perfect num')
else:
    print('it is not a perfect num')


# #perfect square
# num=15
# x=1
# while x<=num//2:
#     if x**x==num:
#         print('it is a perfect square')
#     else:
#         print('it is not perfect square')
#     x+=1

num=100
x=1
is_perfect_square=False
while x<=num//2:
    if x**x==num:
        is_perfect_square=True
    x+=1
if perfect_sqaure:
    print('it is perfect square')
else:
    print('it is not perfect square')