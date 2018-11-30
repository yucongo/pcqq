from pcqq.util.Util import util
class TXProtocol:
    BufTgtgtKey =util.randomKey()
    BufTgtgt =b''
    BufComputerId =b'\x77\x98\x00\x0B\xAB\x5D\x4F\x3D\x30\x50\x65\x2C\x4A\x2A\xF8\x65'
    BufServiceTicketHttp=b''
    DwServerIP='61.151.226.190'
    WServerPort=8000
    CMainVer=b'\x37'
    CSubVer=b'\x09'
    XxooA=b'\x03\x00\x00'
    XxooD=b'\x30\x00\x00\x00'
    XxooB=b'\x01'
    DwClientType=b'\x00\x01\x01\x01'
    DwPubNo=b'\x00\x00\x68\x1C'
    DwSsoVersion=b'\x00\x00\x04\x53'
    DwServiceId=b'\x00\x00\x00\x01'
    DwClientVer=b'\x00\x00\x15\x85'
    WRedirectCount=0
    RedirectIP=[]
    CPingType=b'\x01'
    BufDhPublicKey=bytes([0x02, 0x78, 0x28, 0x16, 0x7C, 0x9E, 0xF3, 0xB7, 0x5A, 0x7B, 0x5A, 0xEF, 0xA2, 0x30, 0x10, 0xEC, 0x0C, 0x46,
                          0x87, 0x70, 0x76, 0x31, 0xA7, 0x88, 0xEA])
txProtocol=TXProtocol()