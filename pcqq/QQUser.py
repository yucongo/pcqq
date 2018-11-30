from pcqq.util.QQTea import qqTea
from pcqq.util.Util import util
from pcqq.QQGlobal import LoginMode
from pcqq.TXProtocol import txProtocol
import time
import requests
class QQUser:
    _ua='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    QQPacket0825Key=util.randomKey()
    QQPacketRedirectionkey=util.randomKey()
    QQPacket00BaKey=util.randomKey()
    QQPacketTgtgtKey=util.randomKey()
    QQPacket00BaFixKey=b'0x69, 0x20, 0xD1, 0x14, 0x74, 0xF5, 0xB3,0x93, 0xE4, 0xD5, 0x02, 0xB3, 0x71, 0x1A, 0xCD, 0x2A'
    QQPacket0836Key1=util.randomKey()
    QQPacket00BaSequence=b'0x01'
    def __init__(self,qqNumber,qqPassword):
        self.qq=qqNumber
        self.setPassword(qqPassword)
        self.initialize()
    def setPassword(self,password):
        self.md51=qqTea.md5(password.encode())
    def md52(self):
        byteBuffer = self.md51+b'0'+bytearray(self.qq)
        byteBuffer = qqTea.md5(byteBuffer)
        return byteBuffer
    def initialize(self):
        self.IsLoggedIn = False
        self.LoginMode = LoginMode.normal
        self.IsUdp = True
    def getCookies(self):
        try:
            s=requests.session()
            address ="https://ssl.ptlogin2.qq.com/jump?pt_clientver=5593&pt_src=1&keyindex=9&ptlang=2052&clientuin="+str(self.qq)+"&clientkey="+util.ToHex(txProtocol.BufServiceTicketHttp)+"&u1=https:%2F%2Fuser.qzone.qq.com%2F417085811%3FADUIN=417085811%26ADSESSION="+str(round(time.time() * 1000))+"%26ADTAG=CLIENT.QQ.5593_MyTip.0%26ADPUBNO=26841&source=namecardhoverstar"
            s.get(address,headers={'User-Agent':self._ua})
            skey=s.cookies.get('skey',domain='http://qq.com')
            if skey is not None:
                if skey is not '':
                    self.QQSkey=skey
                    self.Bkn=util.GetBkn(skey)
                    self.QQGtk=util.GET_GTK(skey)
                    return True
        except:
            print('错误')
        return False
