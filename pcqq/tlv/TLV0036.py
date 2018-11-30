from  pcqq.util.Util import util
class TLV0036:
    def __init__(self):
        self.Command=b'\x00\x36'
        self.Name="SSO2::TLV_LoginReason_0x36"
        self.WSubVer=b'\x00\x02'
    def Get_Tlv(self,qqUser):
        data=b''
        data+=self.WSubVer
        data+=util.shortToBytes(1)
        data+=util.shortToBytes(0)
        data+=util.shortToBytes(1)
        data+=util.shortToBytes(0)
        data+=util.shortToBytes(0)
        data+=util.shortToBytes(0)
        data+=util.shortToBytes(0)
        data+=util.shortToBytes(0)
        data=util.shortToBytes(len(data))+data
        data=self.Command+data
        print(data)
        return data
tlv0036=TLV0036()