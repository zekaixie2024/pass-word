import random
import string
s = string.digits + string.ascii_letters
v = random.sample(s, 5)
# sample为在字符串中随机选k个字符
print(''.join(v))
