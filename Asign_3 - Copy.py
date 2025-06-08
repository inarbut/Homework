def skip():
  print(''.join(("-"*100 + "\n") for i in range(7)))
#Elementary level
#Task 1

list1 = [17, 3, 10, 7, 2]
print(sum(list1))

#Task 2

print(min(list1))

#Task 3

print(list1[::-1])

#Task 4

print("\n".join(map(str, [i for i in list1 if i%2!=0])))


# #Task 5

print((lambda x: [k*x for k in list1])(int(input("Enter a number: "))))

#Easy level

skip()

# #Task 1

list1 = [12, 85, -47, 36, 59, -63, 20, -74, -29, 8, -91, 41, 77, -99, 3, 15, 68, 24, -50, 61]
print((lambda x: [i for i in list1 if i>x])(int(input("Enter a number: "))))

# #Task 2

print(sum([i for i in list1 if i>0])/len([i for i in list1 if i>0]))

# #Task 3

print((lambda x: max(i for i in list1 if i<x))(int(input("Enter a number: "))))

# #Task 4

print((lambda x: sum(i for i in list1 if i%x==0))(int(input("Enter a number: "))))

# #Task5

print([i**2 for i in list1])

# #Task 6

print([i for i in list1 if i>0])

# #Task 7

listS = ['tzgmc', 'afolj', 'xkqte', 'qmrpz', 'twsmv', 'iknue', 'nvzai', 'jxgby', 'dcnqw', 'yroex', 'sbjez', 'uvdlf', 'tzkhp', 'htiyx', 'cbfxa', 'vztak', 'qyabl', 'loscv', 'pkotz', 'fgnrb']
print((lambda x: [i for i in listS if i[:len(x)]==x])(input("Enter a string: ")))

# #Task 8

print((lambda x: sum(list1[:x]))(int(input("Enter of how many numbers: "))))

# #Task 9

listP = ['wgwwgw', 'asdaw', 'saf', 'aksfk', 'slsosls', 'sosal']
print([i for i in listP if i[::-1]==i])

# #Task 10

print((lambda x: [True if i%x==0 else False for i in list1])(int(input("Enter a number: "))))

#Medium level

skip()

#Task 1

list1 = [12, 85, -47, 36, 59, -63, 20, -74, -29, 8, -91, 41, 77, -99, 3, 15, 68, 24, -50, 61, 59]
print((lambda x,y: [i for i in list1 if i%x==0 and i%y!=0])(int(input("Enter a number it should be divided by: ")), int(input("Enter a number it should not be divided by: "))))

# #Task2
listSC = [['cjwqg', 'byspkuq', 'dxm'], 
 ['pvruaj', 'twqob', 'upge', 'ld'], 
 ['zaulihs', 'zvng', 'yxvhknb'], 
 ['dqd', 'pdebsrkjv', 'lrth', 'hpw'], 
 ['saq', 'zltie', 'vmonnbmy']]
print([k for i in listSC for k in i])


# #Task 3
listS = [
    "apple",
    "banana",
    "cherry",
    "dragonfruit",
    "elepphant",
    "forest",
    "grape",
    "honey",
    "island",
    "jungle"
]

#print((lambda x: [''.join(k.upper() if k==x else k for k in list(i)) for i in listS])("pp"))
print((lambda x, y: ''.join([x.split(y)[i]+y.upper() if i!=len(x.split(y))-1 else x.split(y)[i] for i in range(len(x.split(y)))]))("IddKiddwhad", 'dd'))



#Task 4
print(sorted(list1, reverse=True))
print(sorted(sorted(list1, reverse=True), key=list1.count, reverse=True))

#Task 5
list1 = [1, 2, 3, 4, 5, 6]
list2 = [-1, 9, 28, -3, 0, 1]
print((lambda x, y: x+y if len(x+y)>7 else None)(list1, list2))

#Task 6
dic = {
  "user_002": {
    "transactions": [
      {
        "details": {
          "transaction_id": "TXN10001",
          "amount": 132.50,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-04-12T10:18:45",
          "status": "completed",
          "category": "books"
        },
        "bank_noise": {
          "bank_code": "BANK_US_003",
          "terminal_id": "TRM2025",
          "merchant_name": "ReadMore Bookstore"
        }
      },
      {
        "details": {
          "transaction_id": "TXN10002",
          "amount": 77.30,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-07-05T11:25:33",
          "status": "pending",
          "category": "transport"
        },
        "bank_noise": {
          "bank_code": "BANK_US_006",
          "terminal_id": "TRM1175",
          "merchant_name": "CityTransit HQ"
        }
      },
      {
        "details": {
          "transaction_id": "TXN10003",
          "amount": 289.99,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-09-03T15:42:10",
          "status": "completed",
          "category": "furniture"
        },
        "bank_noise": {
          "bank_code": "BANK_EU_010",
          "terminal_id": "TRM2114",
          "merchant_name": "HomeStyle EU"
        }
      },
      {
        "details": {
          "transaction_id": "TXN10004",
          "amount": 63.25,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-10-29T21:09:01",
          "status": "failed",
          "category": "travel"
        },
        "bank_noise": {
          "bank_code": "BANK_US_007",
          "terminal_id": "TRM1399",
          "merchant_name": "SkyFly Agency"
        }
      },
      {
        "details": {
          "transaction_id": "TXN10005",
          "amount": 198.60,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2025-01-10T07:33:28",
          "status": "completed",
          "category": "sports"
        },
        "bank_noise": {
          "bank_code": "BANK_CA_006",
          "terminal_id": "TRM3410",
          "merchant_name": "ProGear Sports Toronto"
        }
      }
    ]
  }
}

print((lambda x: sum([i["details"]["amount"] for i in x["user_002"]["transactions"]]))(dic))

#Task 7
print((lambda x: [True if i>0 else i for i in x])([-1, 9, 28, -3, 0, 1]))

#Task 5, 6, 7
#################################################################

#Task 8
print((lambda x: len([k for k in listS if len(k)>x]))(int(input("Enter a length: "))))

#Task 9
listS1 = [k for i in listSC for k in i]
print((lambda x, mini, maxi: [x.append(maxi[i]) if (i>=len(mini)) else (None if (x.append(mini[i])==None and x.append(maxi[i])==None) else None) for i in range(len(maxi))] and x)([], min(listS1, listS, key=len), max(listS1, listS, key=len)))
#print((lambda x: [x.insert(i, ) for i in range(len(min(listS1, listS, key=len)))] and x)(x=max(listS1, listS, key=len)))

#Task 10
print((lambda x, y: [i*y for i in list1 if i>x])(int(input("Enter of what number should it be greater: ")), int(input("Enter by what number to multiply: "))))


# 5 -об'єднати частини списків на основі умов
# 6 - sum all values by a key
# 7 - replace if element>3, set to true

