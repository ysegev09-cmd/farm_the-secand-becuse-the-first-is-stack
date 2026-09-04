import random 
def create_quartet():
    nok= ["A","G","T","C"]
    word = ''.join(random.choices(nok, k=4))
    return word

def find_cows(sub_rand, sub_gussed):
    cows=0
    lanph=len(sub_gussed)
    for i  in range (lanph):
        if sub_gussed[i] in sub_rand:
            cows +=1
     
    
def find_bulls(rand_str, gussed_str):
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



rand_str=create_quartet()
gussed_str=input("Enter gusset sequnce : ")
nok= ["A","G","T","C"]
if len(gussed_str)!=4 or not all(letter in nok for letter in gussed_str) :
    print("you need to guss only 4 letters and omly noklotidim, try again")
    gussed_str=input("Enter gusset sequnce : ")

 bulls=find_bulls(rand_str, gussed_str)  
