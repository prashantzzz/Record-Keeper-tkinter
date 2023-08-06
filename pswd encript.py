pswd1='1512003pk*'  #contains pre filled password
#below are the replacements for each letter in such a manner so that same letters may form the same encrypted code, making it even harder to crack.
dict1={'1':'qm','2':'wn','3':'eb','4':'rv','5':'tc','6':'yx','7':'uz','8':'il','9':'ok','0':'pj',
       'q':'a1','w':'b2','e':'c3','r':'d4','t':'e5','y':'e6','u':'f7','i':'g8','o':'h9','p':'j1',
       'a':'k2','s':'l3','d':'m4','f':'n5','g':'o6','h':'p7','j':'q8','k':'r9','l':'s1','z':'t2',
       'x':'u3','c':'v4','v':'w5','b':'x6','n':'y7','m':'z8'}
allowed=['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s',
         'd','g','h','j','k','l','z','x','c','v','b','n','m']

encrypt=[]#for-storing-encrypted-pswd
#below-func-can-be-in-list-f0r-random.ch00se
def encryption(pswd):
    
    global encrypt
    encrypt=list(pswd)
    for i in encrypt:
        indx=encrypt.index(i)
        if i in allowed:
            encrypt[indx]=dict1.get(i)
encryption(pswd1)
print(encrypt)
            
