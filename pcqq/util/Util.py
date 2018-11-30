from pcqq.QQGlobal import qqGlobal
from pcqq.util.QQTea import qqTea
import random
class Util:
    def randomKey(self):
        key = []
        for i in range(0, qqGlobal.QQLengthKey):
            key.append(random.randrange(0,256))
        return bytes(key)
    def ToHex(self,bytes):
        str=''
        for h in bytes:
            str+="%02X" %(h)
        return str
    def GetBkn(self,skey):
        num=5381
        for i in range(0,len(skey)):
            num+=(num<<5)+int(skey.index(i,i+1))
        return str(num&0x7FFFFFFF)
    def GET_GTK(self,skey):
        arg = "tencentQQVIP123443safde&!%^%1282";
        list=[]
        num=5381
        list.append(172192)
        _bytes=skey.encode()
        for num2 in _bytes:
            list.append((num << 5) + num2);
            num = num2;
        strs=''
        for li in list:
            str+=str(li)
        strs+=arg
        return qqTea.md5_str(strs)
    def shortToBytes(self,short):
        return short.to_bytes(2,byteorder='big')
    def intToBytes(self,int_):
        return int_.to_bytes(4,byteorder='big')
util=Util()