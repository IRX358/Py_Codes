#=========================1==========================
# trns=[100, -50, 200, -30, 500, -10]
# mnydep,mnywthdr=[],[]
# for i in trns : mnydep.append(i) if i>0 else mnywthdr.append(i)
# # print(f"Total deposits : {sum(mnydep)}\n Total withdrawls : {sum(mnywthdr)}\n Final Balance : {(sum(mnydep))-(sum(mnywthdr))}")

#=========================2==========================
# slrs = [25000, 30000, 40000, 35000, 50000, 28000]
# nwSlrs=[]
# for s in slrs : nwSlrs.append(int(s+s*0.1)) if s<30000 else nwSlrs.append(s)
# # print(f"Inital Salaries list : {slrs}\nUpdated Salaries list : {nwSlrs}")

#=========================3==========================
# store={"phone":30,"laptop":50,"keyboard":40,"speaker":20,"charger":60}
# str_lst={1:"phone",2:"laptop",3:"keyboard",4:"speaker",5:"charger"}
# def buyPrdts():
#     print("\nWelcome to IR Electronics ")
#     for indx,prdts in enumerate(store,1):
#         print(indx," -> ",prdts)
#     prchs=int(input("Enter the product number you want to purchase: "))
#     quan=int(input("Enter the quantity you want to purchase: "))
#     store[str_lst[prchs]]-=quan
#     if store[str_lst[prchs]] == 0 : del store[str_lst[prchs]]
# # buyPrdts()
# # print(store)

#=========================4==========================
para = "Today’s Cloud computing technology has been emerged to manage large data sets efficiently and due to rapid growth of data, large scale data processing is becoming a major point of information technique. The Hadoop Distributed File System (HDFS) is designed for reliable storage of very large data sets and to stream those data sets at high bandwidth to user applications. In a large cluster, hundreds of servers both host directly attached storage and execute user application tasks. By distributing storage and computation across many servers, the resource can grow on demand while remaining economical at every size. MapReduce has been widely used for large-scale data analysis in the Cloud. Hadoop is an open source implementation of MapReduce which can achieve better performance with the allocation of more compute nodes from the cloud to speed up computation; however, this approach of “renting more nodes isn’t cost effective in a pay-as-you-go environment  Data mining is the process of finding correlations or patterns among fields in large data sets and building up the knowledge-base, based on the given constraints. The overall goal of data mining is to extract knowledge from an existing dataset and transform it into a human understandable structure for further use. This process is often referred to as Knowledge Discovery in data sets (KDD). It encompasses data storage and access, scaling algorithms to very large data sets and interpreting results. The data cleansing and data access process included in data warehousing facilitate the KDD process."

# punches =['.',',','!','?',';',':']
# for mark in punches: para=para.replace(mark,"")
# wrds = para.lower().split()
# wrd_freq={}
# for wrd in wrds:
#     if wrd in wrd_freq:
#         wrd_freq[wrd]+=1
#     else:
#         wrd_freq[wrd]=1
# top5=sorted(wrd_freq.items(),key=lambda x:x[1],reverse=True)[:5]
# # print("Top 5 most frequent words : ")
# # for wrd,freq in top5:
#     # print(f"{wrd} : {freq}")

#=========================5==========================
# Skill01=['python','java','rust','html','css','javaScript','golang','flask','mangoDb','Django']
# Skill02=['flask','node.js','ruby','bootstrap','react','javaScript','mangoDb','sqlLite','fastApi']
# skl01set,skl02set=set(Skill01),set(Skill02)
# print(f"\nSkill set from company 01 : {skl01set}\n")
# print(f"Skill set from company 02 : {skl02set}\n")
# print(f"Common skills among both the companies : {skl01set.intersection(skl02set)}\n")
# print(f"Uinque skills to company 01 : {skl01set-skl02set}\n")
# print(f"Uinque skills to company 02 : {skl02set-skl01set}\n")

#=========================6==========================
# emps=[(201,'IR',35800),(203,'SN',50500),(205,'NI',75000),(207,'PV',45000),(209,'TJ',76000)]
# srtEmps=sorted(emps,key=lambda x:x[2],reverse=True)
# print("\n",srtEmps,"\n")

#=========================7==========================
# pat=[303,481,558,865,457,425,457,558,303,658,658,452,475,220,658]
# patID=[]
# [patID.append(x) for x in pat if x not in patID]
# print("\nUnique Patient IDs : ",patID,"\n")


#=========================8==========================
# cks=275
# bxs=12
# lft=cks%12
# print("No. of boxes full packed are : ",int((275-lft)/12))
# print("No. of cookies left out are : ",lft)

#=========================9==========================
# emps = [
#     {"ex": 3, "sl": 35000},
#     {"ex": 1, "sl": 45000},
#     {"ex": 5, "sl": 30000}
# ]
# for emp in emps : 
#     if emp['ex']>2 and emp['sl']<40000 :
#         print(f"The Employee eligible is working from : {emp['ex']} and was getting paid : {emp['sl']}")

#=========================10==========================
# temPre = [
#     {"tmp": 108, "prsr": 180},
#     {"tmp": 98, "prsr": 201},
#     {"tmp": 105, "prsr": 198}
# ]
# for tp in temPre  : 
#     if tp['tmp']>100 or tp['prsr']>200 :
#         print(f"The factory is closed cuz of tempreture : {tp['tmp']}C and the pressure was : {tp['prsr']}PSI")

#=========================11==========================
# stds={"std1":100,"std2":100,"std3":100,"std4":100,"std5":100,"std6":100,"std7":100,"std8":100,}
# print("Students in the class : ",stds)
# while True:
#     s=input("Type in the student name as shown : ")
#     print("The number of credits this student has is : ",stds[s])
#     c=int(input("Enter 1 to register to a new course \nor\n Enter 0 to say you have completed a course : "))
#     stds[s]=stds[s]-5 if c==1 else stds[s]+10
#     print("The updated credits are : ",stds[s])
#     p=int(input("Enter 1 to continue \nor\n Enter 0 to exit : "))
#     if p==1:
#         continue
#     else:
#         break

#=========================12==========================
# a1,a2=5,10
# print(f"Before swap:\nnum 1: {a1}\nnum 2 :{a2}")
# a1 = a1 ^ a2
# a2 = a1 ^ a2
# a1 = a1 ^ a2
# print(f"Before swap:\nnum 1: {a1}\nnum 2 :{a2}")

#=========================13==========================
# print("Welcome to the Parking lot money matters")
# t=int(input("Enter the time , for how long was ur vehicle here (enter in mins) : "))
# if t<=30:
#     print("Its free for you , go enjoy")
# elif t<=120:
#     print("Please Pay Rs.20 in the counter")
# else:
#     t-=120
#     t/=60
#     mny=20+(int(t)*10)
#     print(f"Please Pay Rs.{mny} in the counter")

#=========================14==========================
# def calculate_emi(principal,rate,tenure):
#     Mrate = (rate / 100) / 12
#     Mtenure = tenure * 12
#     emi = (principal * Mrate * (1 + Mrate)*Mtenure) / ((1 + Mrate)*Mtenure - 1)
#     return round(emi, 2)

# p,t,r = 100000,5,12
# print(f"Sample Principal: {p}\nTenure: {t}\nRate: {r}")
# emi = calculate_emi(p,r,t)
# print(f"Monthly EMI: {emi}")

#=========================15==========================
# def AppDis(price,discount):
#     return (price-(price*(discount/100)))
# p,d=24000,30
# print(f"Sample Price : {p}\nDiscount : {d}")
# final_price=AppDis(p,d)
# print("Final Price after applying discount is : ",final_price)

#=========================16==========================
# def cal_od_fns(dd, fn):
#     odFn = dd * fn
#     return round(odFn, 2)
# dd = 10  
# fn = 0.5  
# odFn = cal_od_fns(dd, fn)
# print(f"Sample fine amount : {fn} and due days : {dd}")
# print(f"Overdue fine: ₹{odFn}")

#=========================17==========================
# amt=int(input("Enter the Bill amount : "))
# dis=amt*0.1 if amt>=500 else amt*0.05
# print(f"The discounted price is : {int(amt-dis)}")

#=========================18==========================
# unt=int(input("Enter the units of Electricity consumed : "))
# pr=0
# if unt>300:
#     unt-=300
#     pr+=((2*100)+(3*200))
#     pr+=unt*5
# elif unt>=101 and unt<=300:
#     unt-=100
#     pr+=2*100
#     pr+=3*unt
# else:
#     pr+=2*unt
# print("The amount to be paid for the bill is : ",pr)
#=========================19==========================
# ag=int(input("Enter your age for movie ticket : "))
# if ag<=12:
#     tkt=100
# elif ag>12 and ag<=18:
#     tkt=150
# elif ag>18 and ag<=60:
#     tkt=250
# else:
#     tkt=120
# print("The price for your ticket is : ",tkt)
#=========================20==========================
# sig=input("Enter the color of signal u can see : ").lower()
# if 'd' in sig:
#     print("Stop")
# elif 'o' in sig:
#     print("Wait")
# else:
#     print("Go")

#====================================> ANOTHER SET OF CODES <==========================================================

# transactions = [100, -50, 200, -30, 500, -10] 
# total_deposit = sum(t for t in transactions if t > 0) 
# total_withdrawal = sum(-t for t in transactions if t < 0) 
# final_balance = sum(transactions)
# print("Total Deposit:", total_deposit) 
# print("Total Withdrawal:", total_withdrawal) 
# print("Final Account Balance:", final_balance) 

# salaries = [25000, 30000, 40000, 35000, 50000, 28000]
# updated_salaries = [int(s * 1.10) if s < 30000 else s for s in salaries] 
# print("Updated Salaries:", updated_salaries)

# stock = {"apple": 10, "banana": 5, "orange": 8, "mango": 3}
# purchases = {"apple": 4,"banana": 5,"mango": 2} 
# for item in purchases:
#     if item in stock:
#         stock[item] = stock[item] - purchases[item] 
# for item in list(stock):
#     if stock[item] <= 0: del stock[item]
# print("Updated Stock:") 
# print(stock)

# paragraph = """Your paragraph goes here. Replace this text with any paragraph you want to analyze."""
# words = paragraph.lower().split() 
# freq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1
# top_5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
 
# for word, count in top_5: print(f"{word}: {count}")

# company1_skills = {"Python", "SQL", "Excel", "Communication", "Teamwork"} 
# company2_skills = {"Python", "Java", "Excel", "Leadership", "Creativity"} 
# common_skills = company1_skills & company2_skills
# unique_skills = company1_skills ^ company2_skills 
# print("Common Skills:")
# print(common_skills) 
# print("\nUnique Skills:") 
# print(unique_skills) 

# employees = [(101, "Alice", 75000), (102, "Bob", 50000),(103, "Charlie", 120000),(104,
# "David", 90000)]
# sorted_employees = sorted(employees, key=lambda x: x[2], reverse=True) 
# for emp in sorted_employees:
#     print(emp)

# patient_ids = [101, 102, 103, 101, 104, 102, 105]
# unique_ids = []
# for pid in patient_ids:
#     if pid not in unique_ids: 
#         unique_ids.append(pid)
# print(unique_ids)

# total_cookies = 275
# cookies_per_box = 12
# full_boxes = total_cookies // cookies_per_box 
# remaining_cookies = total_cookies % cookies_per_box 
# print("Full boxes packed:", full_boxes)
# print("Remaining unpacked cookies:", remaining_cookies)

# employees = [("Amit", 3, 35000),("Nitish ", 1, 30000),("Rahul", 4, 45000),("Irfan ", 2,
# 38000),("Kiran", 5, 39000)]
# print("Employees eligible for bonus:") 
# for emp in employees:
#     name = emp[0] years = emp[1] salary = emp[2]
#     if years > 2 and salary < 40000: 
#         print(name)
# temperature = 105
# pressure = 190
# if temperature > 100 or pressure > 200: 
#     print("Machine will shut down.")
# else:
#     print("Machine is operating normally.")

# credits = 100
# courses_registered = 3
# courses_passed = 2
# credits = credits - (courses_registered * 5) 
# credits = credits + (courses_passed * 10) 
# print("Final Credit Balance:", credits) 

# a = 15
# b = 27
# a = a ^ b
# b = a ^ b a = a ^ b
# print("After swapping:") 
# print("a =", a)
# print("b =", b)


# parking_time = 150
# hours = parking_time / 60 
# if parking_time <= 30:
#     bill = 0
# elif hours <= 2: 
#     bill = 20
# else:
#     extra_hours = hours - 2
#     bill = 20 + int(extra_hours) * 10 
# print("Parking Time:", parking_time, "minutes" ) 
# print("Total Bill: ₹", bill)

# def calculate_emi(principal, rate, tenure): 
#     monthly_rate = rate / (12 * 100) 
#     months = tenure * 12
#     emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
#     return round(emi, 2)
# emi = calculate_emi(500000, 7.5, 10) 
# print("Monthly EMI: ₹", emi) 

# def apply_discount(price, discount): 
#     final_price = price - (price * discount / 100) 
#     return round(final_price, 2)
# print("Final Price: ₹", apply_discount(1000, 20))


# def calculate_fine(days_delayed): 
#     fine = 0
#     if days_delayed <= 0: 
#         return 0
#     if days_delayed <= 5:
#         fine = days_delayed * 2 
#     elif days_delayed <= 10:
#         fine = (5 * 2) + (days_delayed - 5) * 5 
#     else:
#         fine = (5 * 2) + (5 * 5) + (days_delayed - 10) * 10 
#         return fine
# print(calculate_fine(3)) 
# print(calculate_fine(7)) 
# print(calculate_fine(15)) 

# def calculate_final_bill(amount): 
#     if amount >= 500:
#         discount = 0.10 * amount 
#     else:
#         discount = 0.05 * amount 
#     final_bill = amount - discount 
#     return final_bill
# print("Final bill for ₹400:", calculate_final_bill(400)) 
# print("Final bill for ₹800:", calculate_final_bill(800)) 

# def calculate_electricity_bill(units): 
#     bill = 0
#     if units <= 100: 
#         bill = units * 2
#     elif units <= 300:
#         bill = (100 * 2) + (units - 100) * 3 
#     else:
#         bill = (100 * 2) + (200 * 3) + (units - 300) * 5 
#     return bill
# print("Bill for 80 units:", calculate_electricity_bill(80)) 
# print("Bill for 150 units:", calculate_electricity_bill(150)) 
# print("Bill for 350 units:", calculate_electricity_bill(350)) 


# def ticket_price(age): 
#     if age < 12:
#         return 100 
#     elif age <= 18: 
#         return 150
#     elif age <= 60: 
#         return 250
#     else:
#         return 120
# print("Ticket price for age 8:", ticket_price(8))
# print("Ticket price for age 15:", ticket_price(15)) 
# print("Ticket price for age 30:", ticket_price(30)) 
# print("Ticket price for age 65:", ticket_price(65)) 

# def traffic_signal(color): 
#     color = color.lower() 
#     if color == "red":
#         return "Stop"
#     elif color == "yellow": 
#         return "Wait"
#     elif color == "green": 
#         return "Go"
#     else:
#         return "Invalid signal color!" 
# print(traffic_signal("Red")) 
# print(traffic_signal("Yellow")) 
# print(traffic_signal("Green")) 
# print(traffic_signal("Blue"))
