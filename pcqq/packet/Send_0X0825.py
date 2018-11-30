from pcqq.packet.SendPacket import SendPacket
from pcqq.QQGlobal import QQCommand
from pcqq.tlv.TLV0018 import tlv0018
from pcqq.tlv.TLV0309 import tlv0309
from pcqq.tlv.TLV0036 import tlv0036
from pcqq.tlv.TLV0114 import tlv0114
class Send_0X0825(SendPacket):
    def __init__(self,qqUser):
        super(Send_0X0825,self).__init__(qqUser)
        self.Sequence=self.GetNextSeq()
        self.Command=b'\x08\x25'
    def PutHeader(self):
        super().PutHeader()
        self.SendPACKET_FIX()
        self.data+=self.SecretKey
    def getBody(self):
        byt=b''
        byt+=tlv0018.Get_Tlv(self.qqUser)
        byt+=tlv0309.Get_Tlv(self.qqUser)
        byt+=tlv0036.Get_Tlv(self.qqUser)
        byt+=tlv0114.Get_Tlv(self.qqUser)
        return byt