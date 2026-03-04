#for i in range(1,21):
    #if i%3==0:
        #print(f"{i} is fizz")
    #elif i%5==0:
        #print(f"{i} is buzz")
   # else:
    #    i%3==0 and i%5==0
        #print(f"{i} is fizzbuzz")


str1="data science"
#print(str1[0])
#print(str1[1])
#for char in str1:
    #print(char)

dict={'name':'malleswari','city':'hyd','role':'developer'}
#print(dict['name'])
#for x in dict:
    #print(x)

#for i in range(1,11):
    #print(f"3*{i}={3*i}")






#26/02  forloop

# str1='SOMETHING IS FISHY'
# for element in str1:
#     print(element)
# x=1
# for char in str1:
#     print(char,str1[x])
#     x+=1


# str1="DATA"
# for char in str1:
#     print(f"{char}-HELLO")

# list1=[4,6,8,2,3,1,8,9]

# for i in list1:
#     print(f"square of {i} is {i**2}")



# list1=['shiva','karthik','karun','tejaswini','yamini','deepak','satwik']
# for element in list1:
#     print(f"{element} length is {len(element)}")


# nums=[3,5,7,8,2,4,6,10]
# x=0
# for i in nums:
#     print(f"{i*x}")
#     x+=1


# str1="BANANA"
# dict1={}
# for x in str1:
#     if x in dict1:
#         dict1[x]+=1
#     else:
#         dict1[x]=1
# print(dict1)

# str1='hello'
# op=str1.upper()
# print(op)


# str1='MALLESWARI'
# op=str1.lower()
# print(op)


# los=['apple','banana','SOME','hello','WELCOME','OOPS']

# # for char in los:
#     if char==char.upper():
#         print(char.lower())
#     else:
#         print(char.upper())


# op=[]
# for char in los:
#         if char==char.upper():
#           #print(char.lower())
#           op+=[char.upper()]
#         else:
#             # print(char.upper())
#             op+=[char.upper()]
# print(op)



# s1='soMeThINg'
# op=''
# for char in s1:
#      if char==char.upper():
#           op+=char.lower()
#      else:
#           op+=char.upper()
# print(op)






# for i in range(5,26):
#     print(i)

# sum=0
# for x in range(5,10):
#     sum+=x
# print(sum)

# num=int(input("enter any number : "))
# fact=1
# for x in range(1,num+1):
#     fact*=x
# print(fact)







ecommerce_data = [
    {
        "order_id": "O1001",
        "customer_name": "Ravi Kumar",
        "city": "Hyderabad",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "price": 799,
        "quantity": 2,
        "total_amount": 1598,
        "payment_method": "UPI",
        "order_status": "Delivered"
    },
    {
        "order_id": "O1002",
        "customer_name": "Sneha Reddy",
        "city": "Bangalore",
        "product": "Bluetooth Headphones",
        "category": "Electronics",
        "price": 1999,
        "quantity": 1,
        "total_amount": 1999,
        "payment_method": "Credit Card",
        "order_status": "Shipped"
    },
    {
        "order_id": "O1003",
        "customer_name": "Arjun Singh",
        "city": "Mumbai",
        "product": "Running Shoes",
        "category": "Fashion",
        "price": 2499,
        "quantity": 1,
        "total_amount": 2499,
        "payment_method": "Cash on Delivery",
        "order_status": "Processing"
    },
    {
        "order_id": "O1004",
        "customer_name": "Priya Sharma",
        "city": "Delhi",
        "product": "Smart Watch",
        "category": "Electronics",
        "price": 3499,
        "quantity": 1,
        "total_amount": 3499,
        "payment_method": "Debit Card",
        "order_status": "Delivered"
    },
    {
        "order_id": "O1005",
        "customer_name": "Kiran Patel",
        "city": "Chennai",
        "product": "Laptop Backpack",
        "category": "Accessories",
        "price": 1299,
        "quantity": 3,
        "total_amount": 3897,
        "payment_method": "UPI",
        "order_status": "Shipped"
    }
]

#tasks of the day
for x in ecommerce_data:
    # if x['price']>1000:
    #      print(x['customer_name'])
    # if x['payment_method']=='UPI':
    #       print(x['customer_name'],x['payment_method'])
    # if x ['quantity']>1:
    #       print(x['customer_name'])
    if x['category'] != 'Electronics':
        print(x['customer_name'])