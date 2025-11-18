import random
def nrm_key_gen():
    return random.randint(1,25)
class enc:
    conv=[]
    strr=''
    def __init__(self,ch,k):
        self.ch=ch
        self.k=k
    def gtdgvl(self):
        for i in self.ch:
            self.conv.append(ord(i)-ord('a'))
        return self.conv
    def adkvl(self,con):
        for i in range(0,len(self.conv)):
            self.conv[i]=self.k+con[i]
        return self.conv
    def gtchvl(self,uncon):
        for i in range(0,len(uncon)):
            self.strr+=chr(ord('a')+self.conv[i])
        return self.strr
    def subkvl(self,uncon):
        for i in range(0,len(uncon)):
            self.conv[i]=uncon[i]-self.k
        return self.conv
    
def caesar_chiper(plnt,key):
    e1=enc(plnt,key)
    con=e1.gtdgvl()
    print("Digit value of your plain text is : ",con)
    print("Your sceret key is : ",e1.k)
    encon=e1.adkvl(con)
    print("your digit Value after adding is : ",encon)
    ct=e1.gtchvl(encon)
    print("Your cipher text is : ",ct)
    uncon=e1.subkvl(encon)
    print("Your digit value after subtracting key value is : ",uncon)
    tt=e1.gtchvl(uncon)
    pt=tt.replace(ct,'')
    print("Your plain text is : ",pt)

class enc1():
    def __init__(self,plntxt,key1,key2):
        self.plntxt=plntxt
        self.key1=key1
        self.key2=key2   


# key=nrm_key_gen()
# print("Enter your plain text")
# caesar_chiper(input(),key)