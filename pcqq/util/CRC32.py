class CRC32:
    _crc16Table = b''
    _crc32Table = b''
    _crc32Table2 = b''
    def MakeCRC16Table(self):
        if len(self._crc16Table) > 0:
            return
        list=[]
        for num in range(0,256):
            num2 = num
            for i in range(0, 8):
                if num2 % 2 == 0:
                    num2 = num2 >> 1
                else:
                    num2 = (num2 >> 1) ^ 33800
            list.append(num2)
        self._crc16Table=bytes(list)
    def MakeCRC32Table(self):
        if len(self._crc32Table)>0:
            return
        for num in range(0,256):
            num2 = num
            for i in range(0, 8):
                if num2 % 2 == 0:
                    num2 >>= 1
                else:
                    num2 = (num2 >> 1) ^ 3988292384
            self._crc32Table.append(num2)
    def UpdateCRC16(self,byte,seed):
        return self._crc16Table[(seed&255)^byte]^(seed>>8)
    def UpdateCRC32(self,byte,seed):
        return self._crc16Table[(seed&255)^byte]^(seed>>8)
    def CRC16(self,bytes):
        self.MakeCRC16Table()
        num=65535
        for byte in bytes:
            num=self.UpdateCRC16(byte,num)
        return num