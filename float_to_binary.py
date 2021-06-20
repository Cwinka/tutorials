import struct

def binary(num):

    binaries = [bin(i) for i in struct.pack('!d', num)]
    stripped_binaries = [s[2:] for s in binaries]
    padded = [s.rjust(8, '0') for s in stripped_binaries]
    layout = ''.join(padded)
    third_layout = [layout[0], layout[1:12], layout[13:]]
    return ' '.join(third_layout)

print(binary(40.0))
