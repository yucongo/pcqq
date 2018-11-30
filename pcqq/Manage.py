from pcqq.packet.Send_0X0825 import Send_0X0825
from pcqq.SocketService import SocketService
from pcqq.QQUser import QQUser
class Manage:
    def __init__(self,qqUser,socketService):
        self.qqUser=qqUser
        self.socketService=socketService
    def start(self):
        socketService.sendData(Send_0X0825(self.qqUser).WriteData())
if __name__ == '__main__':
    qqUser=QQUser(0,'')
    socketService=SocketService(qqUser)
    manage=Manage(qqUser,socketService)
    manage.start()
