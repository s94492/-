import random

star= int(input("請輸入數字起始值:"))
end=  int(input("請輸入數字結束值:"))
comnum= random.randint(star,end)
x=5

while x>0 :
    usernum = int(input("請輸入數字:"))

    if usernum >= star and usernum <= end :
        x = x - 1
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
    else:
        print("請輸入",star,"~",end,"的數字")

print ("遊戲結束")