# def mod_inv(k,m=26): #needed to calc the modular inverse of a number under dec of affine cipher 
#     def euclid_algo(a,b):
#         if b==0:
#             return a,1,0
#         gcd,x1,y1=euclid_algo(b,a%b)
#         x,y=y1,x1-(a//b)*y1
#         return gcd,x,y
#     gcd,x,_=euclid_algo(k,m) #ignoring y , as thts not needed for the calulations 
#     return x%m

# print(mod_inv(6))

# import random
# def constraint_key_gen():
#     return random.randrange(1,27,2)

# print(constraint_key_gen())


# def subkvl(dcn,ky2):
#     conv2 = [(22*(i-ky2))%26 for i in dcn]
#     return conv2

# dcn=[13,13,13]
# ky=6
# print(subkvl(dcn,ky))
# #gotta fix this decyprtion

# match type:
#     case 1:
#         print("Your sceret key is : ",key1,"\n")
#         c_chiper(plntxt,key1)
#     case 2:
#         key2=int(input())
#         if key2 == 0 :
#             key2=constraint_key_gen()
#         print(f"Your sceret key is : {key1} , {key2} \n ")
#         a_chiper(plntxt,key1,key2)
#     case 3:
#         print(f"Your sceret key is : {key1} \n")
#         v_chiper(plntxt,key1)
#     case 4:
#         dec_c_chiper(plntxt,key1)
#     case 5:
#         key2=int(input())
#         dec_a_chiper(plntxt,key1,key2)
#     case 6:
#         dec_v_chiper(plntxt,key1)

# pt=[12,10,9,2,5]
# key=23
# bi_txt=''.join(format(i,'08b')for i in pt)
# print(bi_txt)
# bi_ky=format(key,'08b')
# print(bi_ky)
# xor=''.join('1'if b1!=b2 else '0'for b1,b2 in zip(bi_txt,bi_ky))
# print(xor)
# un=[xor[i:i+8]for i in range(0,len(xor),8)]
# con=''.join(chr(int(b,2)) for b in un)
# print(con)

# def mod_inv(self, k, m=26): #needed to calc the modular inverse of a number under dec of affine cipher
#     def euclid_algo(a, b):
#         if b == 0:
#             return a, 1, 0
#         gcd, x1, y1 = euclid_algo(b, a % b)
#         x, y = y1, x1 - (a // b) * y1
#         return gcd, x, y
#     gcd, x, _ = euclid_algo(k, m) #ignoring y , as thts not needed for the calulations
#     if gcd != 1:
#         raise ValueError(f"Key {k} is not invertible modulo {m}. Choose a different key.")
#     return x % m