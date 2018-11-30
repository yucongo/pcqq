import hashlib
import struct, ctypes
import os
class QQTea:
    def md5(self,bytes):
        return hashlib.md5(bytes).hexdigest().encode('utf-8')
    def md5_str(self,text):
        str=''
        for h in self.md5(text.encode()):
            str+="%02X" %(h)
        return str
    def xor8B(self,a, b):
        '''
        XOR operation between two 8B bytes.
        '''
        length = 8
        arr_a = bytearray(a[:length])
        arr_b = bytearray(b[:length])
        for i in range(length):
            arr_a[i] ^= arr_b[i]
        return bytes(arr_a) if isinstance(a, bytes) else arr_a
    def encipher(self,v, k):
        '''
        TEA coder encrypt 64 bits value, by 128 bits key,
        QQ uses 16 round TEA.
        http://www.ftp.cl.cam.ac.uk/ftp/papers/djw-rmn/djw-rmn-tea.html .
        '''
        n=16  #qq use 16
        delta = 0x9e3779b9
        k = struct.unpack('!LLLL', k[0:16])
        y, z = map(ctypes.c_uint32, struct.unpack('!LL', v[0:8]))
        s = ctypes.c_uint32(0)
        for i in range(n):
            s.value += delta
            y.value += (z.value << 4) + k[0] ^ z.value+ s.value ^ (z.value >> 5) + k[1]
            z.value += (y.value << 4) + k[2] ^ y.value+ s.value ^ (y.value >> 5) + k[3]
        r = struct.pack('!LL', y.value, z.value)
        return r
    def encrypt(self,v, k):
        """
        Encrypt function for QQ.
        v is the message to encrypt, k is the key
        fill char is randomized (which is 0xAD in old version)
        the length of the final data is filln + 8 + len(v)
        The message is encrypted 8 bytes at at time,
        the result is:
        r = encipher( v ^ tr, key) ^ to   (*)
        `encipher` is the QQ's TEA function.
        v is 8 bytes data to be encrypted.
        tr is the result in preceding round.
        to is the data coded in perceding round (v_pre ^ r_pre_pre)
        For the first 8 bytes 'tr' and 'to' is filled by zero.
        """
        vl = len(v)
        #filln = (8 - (vl + 2)) % 8
        filln = (6 - vl) % 8
        v_arr = (
            bytes(bytearray([filln | 0xf8])),
            os.urandom(filln + 2),  # random char * (filln + 2)
            v,
            b'\0' * 7,
        )
        v = b''.join(v_arr)
        tr = to = b'\0' * 8
        r = []
        for i in range(0, len(v), 8):
            o = self.xor8B(v[i:i+8], tr)
            tr = self.xor8B(self.encipher(o, k), to)
            to = o
            r.append(tr)
        r = b''.join(r)
        return r
qqTea=QQTea()