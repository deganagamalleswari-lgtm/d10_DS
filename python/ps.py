#sum of list
#  lst=[[1,2,3],[3,4,5],[1,3,2]]
# dict={}
# for x in range(len(lst)):
#     sum=0
#     for y in lst[x]:
#         sum+=y
#         dict[x]=sum
# print(dict)

# max=0
# for i in dict:
#     if dict[i]>max:
#             max=dict[i]
#             ind=i
# print(max,ind)

# print(f'max amount of list is{lst[ind]}')


#find duplicate numbers
# lst=[1,2,3,3,2,14,5,4,7]
# dict={}
# for x in (lst):
#     if x in dict:
#         dict[x]+=1
#     else:
#         dict[x]=1
# print(dict)
# dup=[]
# for i in dict:
#     if dict[i]>1:
#         dup.append(i)
# print(dup)



sentence='python is a powerful programming language'
word=''
lst=[]
for i in sentence:
    if i != '':
        word+=i
    else:
        lst.append(word)
        word=''
lst.append(word)
print(lst)
