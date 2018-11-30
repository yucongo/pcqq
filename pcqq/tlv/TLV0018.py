from pcqq.TXProtocol import txProtocol
from pcqq.util.Util import util
class TLV0018:
    def __init__(self):
        self.Command=b'\x00\x18'
        self.Name="SSO2::TLV_Ping_0x18"
        self.WSubVer=b'\x00\x01'
    def Get_Tlv(self,qqUser):
        data=b''
        data+=self.WSubVer
        data+=txProtocol.DwSsoVersion
        data+=txProtocol.DwServiceId
        data+=txProtocol.DwClientVer
        data+=util.intToBytes(qqUser.qq)
        data+=util.shortToBytes(txProtocol.WRedirectCount)
        data+=util.shortToBytes(0)
        data=util.shortToBytes(len(data))+data
        data=self.Command+data
        return data
tlv0018=TLV0018()