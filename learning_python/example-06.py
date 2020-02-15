str_len = len('Hello World')
print(str_len)
msg = 'Good-bye World'
str_len = len(msg)
print(str_len)

msg = 'Hello'
print(msg[0])

print(msg[4])

print(msg[len(msg)-1])

print(msg[1:4])

print(msg[:3])

print(msg[2:])

print(msg[:])

print(msg[::2])

msg = 'Hello' "World"'''!
Good-bye'''""" World"""
print(msg)

world = 'World'
msg = 'Hello' + world
print(msg)

some_value = '1'
result = int(some_value) + 1
print(result)

print("a" * 5)

'Setagaya' in 'Sakura-Jousui, Setagaya-ku, Tokyo, Japan'

'Setagaya' in 'Yoyogi, Shibuya-ku, Tokyo, Japan'

'Setagaya' not in 'Sakura-Jousui, Setagaya-ku, Tokyo, Japan'

'Setagaya' not in 'Yoyogi, Shibuya-ku, Tokyo, Japan'

address = '東京都世田谷区桜上水'
ward = '世田谷区'

if (ward in address):
    print(address + 'は' + ward + 'にあります')
else:
    print(address + 'は' + ward + 'にはありません')

sample_str = 'find, rfind, index, rindex'
print(sample_str.find('index'))
print(sample_str.rfind('index'))
#print(sample_str.find('foo'))
print(sample_str.index('find'))
print(sample_str.index('find'))
#print(sample_str.index('foo'))

'abc def ghi'.split(' ')

#[26]
#'abc def ghi'.split('', 1)


alpha_list = 'abc def ghi'.split()
print(alpha_list)
alpha_str = ','.join(alpha_list)
print(alpha_str)

alpha_list = 'abc def ghi'.split()
print(alpha_list)
alpha_str = ''.join(alpha_list)
print(alpha_str)


data = 'abc, def, ghi'
data_list = data.split(',')
print(data_list)

sample_str =' sample '
print('begin:' + sample_str.strip() + ':end')
print('begin:' + sample_str.lstrip() + ':end')
print('begin:' + sample_str.rstrip() + ':end')
print(sample_str)

sample_str = '**++**sample**++**'
print(sample_str.strip('*'))
print(sample_str.strip('+*se'))


num = 'not a number'
user_input = input('input number: ')
if user_input.isdigit():   
    num = int(user_input)
#print(num)

sample_str='abc def GHI JKL'
print(sample_str.replace('abc','xyz'))
print(sample_str.swapcase())
print(sample_str.title())
print(sample_str.lower())
print(sample_str.upper())

sample_str ='this is a sanoke string'
print(sample_str.startswith('this'))
print(sample_str.endswith('string'))

smple_str = 'this is a sample string'
print(sample_str.startswith(('that', 'those')))
print(sample_str.endswith(('sample','ing')))

sample_str = 'Python'
print(sample_str.ljust(12, '+'))
print(sample_str.center(12, '*'))
print(sample_str.rjust(12))