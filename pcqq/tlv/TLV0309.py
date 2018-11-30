from pcqq.TXProtocol import txProtocol
from pcqq.util.Util import  util
class TLV0309:
    def __init__(self):
        self.Command=b'\x03\x09'
        self.Name="SSO2::TLV_Ping_Strategy_0x309"
        self.WSubVer=b'\x00\x01'
    def Get_Tlv(self,qqUser): #command+length+body
        data=b''
        ipList=txProtocol.DwServerIP.split('.')
        for s in ipList:
            data+=bytes([int(s)])
        data+=bytes([len(txProtocol.RedirectIP)])
        for bt in txProtocol.RedirectIP:
            data+=bt
        data+=txProtocol.CPingType
        data=util.shortToBytes(len(data))+data
        data=self.Command+data
        return data
tlv0309=TLV0309()