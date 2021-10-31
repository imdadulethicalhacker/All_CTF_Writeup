# Transformation
### Points: 20

## Category
#### Reverse Engineering

## Question
#### I wonder what this really is... [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
### Hint
>#### You may find some decoders online



## Solution 
### Download the [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc) file and look at the txt file. 
```base
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽
```
### Then go to this [CyberChef](https://gchq.github.io/CyberChef/#recipe=Magic(3,true,false,'picoctf')&input=54Gp5o2v5I2U5Jm744S25b2i5qW0542f5qWu542044y05pGf5r2m5by45b2k45Sy5oy25oi54429) page, paste the code, and choose the magic option to acquire the flag. 
![pico](a/1.png)

## Flag
`picoCTF{16_bits_inst34d_of_8_d52c6b93}`