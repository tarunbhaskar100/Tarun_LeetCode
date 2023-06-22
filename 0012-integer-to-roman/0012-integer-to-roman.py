class Solution:
    def intToRoman(self, num: int) -> str:
        out=''
        # d = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        intg = [1000,500,100,50,10,5,1]
        rom = ['M','D','C','L','X','V','I']
        for i in range(len(rom)):
            s = str(num)[0]
            p = num//intg[i]
            
            # print(s,p,num)
            if s == '4' and p == 4:
                out = out + rom[i]+rom[i-1]
                num = num%intg[i]
            elif s == '9' and p == 1:
                # print(rom[i])
                out = out+ rom[i+1]+rom[i-1]
                num = num%intg[i+1]
            else:
                out = out+rom[i]*p
                num = num%intg[i]
        return out