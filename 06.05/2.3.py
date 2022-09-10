a=input("string1:");
b=input("string2:");

def anagram(a,b):

    arra=split(a)
    arrb=split(b)
    arra.sort()
    arrb.sort()

    if (len(arra)==len(arrb)):

            if(arra==arrb):
                print ("True")
            else:
                ana=0;
                print ("False");

    else:
        print ("False");



def split(x):
    x=x.replace(' ','').lower()
    temp=[]
    for i in x:
        temp.append(i)
    return temp;


anagram(a,b)