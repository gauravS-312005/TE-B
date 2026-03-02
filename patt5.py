# ************pattern5 star pyramid*******
for i in range(1,5): #i ni range
    for j in range(1,8): #j ni range
        if j>=5-i and j<=3+i: ##############logic##########
            print("*",end='') #end bracause not change line
        else:
            print(" ",end='')
    print() #end of for loop of j to change line

  
