from struct import unpack
from math import ceil, floor
from threp.static import frame_search_range, frame_correct_retry

def unsigned_int(_bytes, pointer):
    return unpack('I', _bytes[pointer:pointer + 4])[0]

def unsigned_char(_bytes, pointer):
    return unpack('B', _bytes[pointer:pointer + 1])[0]

def float_(_bytes, pointer):
    return unpack('f', _bytes[pointer:pointer + 4])[0]

def bin32(num):
    return f'{bin(num)[2:]:>32}'.replace(' ', '0')

def bin16(num):
    return f'{bin(num)[2:]:>16}'.replace(' ', '0')

class Ref:
    def __init__(self, value):
        self.value = value

def entry(file):
    buffer = bytearray(0x100000)
    with open(file, 'rb') as f:
        _buffer = f.read()
        buffer[:len(_buffer)] = _buffer
    return buffer

# 根据长度获取正确的帧数
def true_frame(llength):
    frame = floor(llength / (6 + 1/30))
    if frame * 6 + ceil(frame / 30) == llength:
        return frame
    # 暴搜，，，
    for i in range(frame - frame_search_range, frame + frame_search_range):
        if i * 6 + ceil(i / 30) == llength:
            return i
    raise Exception("Can't correct the frame length")

def correct_true_frame(llength):
    for _ in range(frame_correct_retry):
        try:
            return true_frame(llength)
        except Exception:
            # 一直加65536，直到能够获取正确的帧数
            llength += 65536
    raise Exception("Can't correct the frame length")