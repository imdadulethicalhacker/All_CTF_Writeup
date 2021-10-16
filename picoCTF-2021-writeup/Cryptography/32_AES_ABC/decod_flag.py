from Crypto.Util.number import long_to_bytes, bytes_to_long
import math
import sys

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))

enc = open("body.enc.ppm", "rb")
otp = open("body.ppm", "wb")

txt = enc.read()
txt = txt.split(b"\n")
headers = b'\n'.join(txt[:3])
ct = b'\n'.join(txt[3:])
print(headers)
blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) // BLOCK_SIZE)]

dec = b""

prev_block = 0x0
cnt = 0
for b in blocks:
	cnt += 1
	print(cnt)
	num_b = bytes_to_long(b)
	block = long_to_bytes((num_b - prev_block) % UMAX)
	dec += block
	prev_block = bytes_to_long(b)

otp.write(b'\n'.join(headers.split(b" ")) + b'\n' + dec)