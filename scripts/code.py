import random  #יצירת המחרוזת הרנדומלית
def create_quartet():
    nok= ["A","G","T","C"]
    word = ''.join(random.choices(nok, k=4))
    return word

def find_cows(sub_rand, sub_gussed): # ספירת הפספוסים
    cows=0
    lanph=len(sub_gussed)
    for i  in range (lanph):
        if sub_gussed[i] in sub_rand:
            cows +=1
    return cows
     
def find_bulls(rand_str, gussed_str): # ספירת הבול פגיע
    file_a=open('results/chat', 'w')
    sub_gussed =""
    sub_rand=""
    bulls=0
    for i in range (4):
        if gussed_str[i]==rand_str[i]:
            bulls+=1
        else:
            sub_gussed += gussed_str[i]
            sub_rand+=rand_str[i]
    cows=find_cows(sub_rand, sub_gussed)
    print ("Bulls= ",bulls)
    file_a.write("Bulls= "+ str(bulls) +"\n" )
    print("Cows=",cows)
    file_a.write("Cows= "+str(cows)+"\n" )
    return bulls

file_a=open('results/chat', 'w') # משתנים הדרושים
rand_str=create_quartet()
bulls=0
attempts=0
nok= ["A","G","T","C"]
while bulls!=4:  # יצירת לולאת הנסיונות
    gussed_str=input("Please try to guess a four DNA combination composed from A,T,C,G : ")
    if len(gussed_str)!=4 or not all(letter in nok for letter in gussed_str) :
        print("you need to guss only 4 letters and omly noklotidim, try again")
        gussed_str=input("Please try to guess a four DNA combination composed from A,T,C,G  : ")
    file_a.write("Please try to guess a four DNA combination composed from A,T,C,G : "+gussed_str+"\n" )
    bulls=find_bulls(rand_str, gussed_str)  
    attempts+=1
print("You guessed after", attempts,"attempts")