# 猜1 ~ 100 的數字
#重覆猜
# 猜對印出 猜對
#猜錯要告訴他 大還小
import random

#usernum = int(input("請輸入1~100的數字"))
comnum= random.randint(1,100)
x=5
while x>0 :
    x = x-1
    usernum = int(input("請重新輸入1~100的數字"))
    if usernum == comnum :
        print ("猜對了")
        break
    elif usernum < comnum :
        print("太小了喔!")
        if x>0 :
            print ("您還剩下",x,"次機會")
    elif usernum > comnum:
        print ("太大了喔!")
        if x > 0:
            print("您還剩下", x, "次機會")

print ("遊戲結束")