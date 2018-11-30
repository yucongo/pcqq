from pcqq.QQGlobal import qqGlobal
from pcqq.TXProtocol import txProtocol
from pcqq.util.QQTea import  qqTea
from pcqq.util.Util import util
class SendPacket:
    _seq=0x3635
    Command=b''
    Sequence=0
    data=b''
    SecretKey=b''
    def __init__(self,qqUser):
        self.Version=qqGlobal.QQClientVersion
        self.qqUser=qqUser
        self.SecretKey=qqUser.QQPacket0825Key
    def PutHeader(self):
        self.data+=qqGlobal.QQHeaderBasicFamily
        self.data+=txProtocol.CMainVer
        self.data+=self.Command
        self.data+=util.shortToBytes(self.Sequence)
        self.data+=(self.qqUser.qq).to_bytes(8,byteorder='big')
    def SendPACKET_FIX(self):
        self.data+=txProtocol.XxooA
        self.data+=txProtocol.DwClientType
        self.data+=txProtocol.DwPubNo
        self.data+=txProtocol.XxooD
    def WriteData(self):
        self.PutHeader()
        body=self.getBody()
        print(body)
        body=qqTea.encrypt(body,self.SecretKey)
        print(body)
        body+=self.data
        self.data+=qqGlobal.QQHeader03Family
        return self.data
    def GetNextSeq(self):
        self._seq+=1
        self._seq &= 0x7FFF
        if self._seq==0:
            self._seq+=1
        return self._seq
    def getBody(self):
        return b''


