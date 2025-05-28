import random
'''
1 for  snake
-1 for water
0 for gun
'''
ai =random.choice([1,-1,0])
me=input("enyter a choice")
options_dic={"snake":1,"water":-1,"gun":0}
reversed_options_dic={1:"snake",-1:"water",0:"gun"}
you=options_dic[me]
print(f"you chose {reversed_options_dic[you]}   and ai chose {reversed_options_dic[ai]}")

if you ==ai:
    print("It's a tie")
else:
    if(ai==-1 and me==0) or (ai==0 and me==1) or (ai==1 and me==-1):
        print("You lose")
    else:
        print("You win")