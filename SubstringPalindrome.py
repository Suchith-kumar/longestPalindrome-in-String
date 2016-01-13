'''
autor : Suchith Kumar
 
      To find the longest palindrome substring
'''
def Palindrome():
    inpp = input("enter string :") # "Catac112211ca"
    inp=inpp.lower()
    strln=len(inp)
    lenth=0
    maxlenth=0
    begin=0
    end=0
    for i in range(strln):
        if i+1 > (strln-1) :
            break
        else:
            for j in range(i+1,strln):
                strr=inp[i:j]           # substring creation
                if strr==strr[::-1]:    # check if substring is palindrome
                    lenth=len(strr)
                    if lenth>maxlenth :  # finding the maximum palindrome substring positions
                        maxlenth=lenth
                        begin=i
                        end=j
    print(inp[begin:end])
                    
        

if __name__ == "__main__":
    Palindrome()
