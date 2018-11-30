import socket
from pcqq.TXProtocol import txProtocol
class ReceiveData:
    Data = b'',
    DataLength = 0,
    From = ''
    def __init__(self,Data,DataLength,From):
        self.Data=Data
        self.DataLength=DataLength
        self.From=From
class SocketService:
    def __init__(self,qqUser):
        self._qqUser=qqUser
        self._host=socket.gethostbyname('sz6.tencent.com')
        txProtocol.DwServerIP=self._host
        self._port=txProtocol.WServerPort
        self._udpServer=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udpServer.bind(('',8888))
    def receiveData(self):
        data,addr=self._udpServer.recv(1024)
        return ReceiveData(data,len(data),addr)
    def sendData(self,bytes):
        self._udpServer.sendto(bytes,(self._host,self._port))
    def close(self):
        self._udpServer.close()