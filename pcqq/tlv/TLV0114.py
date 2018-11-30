from pcqq.TXProtocol import txProtocol
from pcqq.util.Util import util
class TLV0114:
    def __init__(self):
        self.Command=b'\x01\x14'
        self.Name="SSO2::TLV_DHParams_0x114"
        self.WSubVer=b'\x01\x02'
    def Get_Tlv(self,qqUser):
        data=b''
        data+=self.WSubVer
        data+=util.shortToBytes(len(txProtocol.BufDhPublicKey))
        data+=txProtocol.BufDhPublicKey
        data=util.shortToBytes(len(data))+data
        data=self.Command+data
        return data
tlv0114=TLV0114()