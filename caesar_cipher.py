print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8  8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88  PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88  8b     aa aa    8I  88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8ii `"YbbdP"' `"8bbdP"Y8 88   
                                                           
                                                       
           ""             88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 
       'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
       'w', 'x', 'y', 'z']



def cipher(direction, text,shift):
    massage=''
    if(direction=="encrypt"):
        for i in text:
            index = alpha.index(i)
            index=index+shift
            massage=massage+alpha[index]
   
    elif(direction=="decode"):
        for i in text:
            index = alpha.index(i)
            index=index-shift
            massage=massage+alpha[index]
    return massage
b=True
while(b!=False):
    direction =input("type here what you do with your massage like encrypt or decode:-\n")
    text =input(f"type your massage for {direction}\n").lower()
    shift=int(input("type the shift number :-\n"))
    shift=shift%26
    print(cipher(direction,text,shift))

    rep = input("do you ucontinue this ? type yes or no\n")
    if rep=="no":
        print("thanks for use this servise see you soon")
        b=False

