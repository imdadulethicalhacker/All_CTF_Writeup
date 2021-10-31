
import hashlib
import base64


hash = hashlib.sha256(b'FRASER').hexdigest()
list = [4,5,3,6,2,7,1,8]


print("picoCTF{1n_7h3_|<3y_of_",end ='')

for i in list:
	print(hash[i], end = '')
print("}")	



