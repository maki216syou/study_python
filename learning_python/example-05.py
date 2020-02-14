# macの場合は¥ではなく\を使う

print('It\'s')

print("\"Deep Insider\" is...")

print("1行目\n2行目")

code_point = ord("a")
oct_code = oct(code_point)
hex_code = hex(code_point)
print(oct_code)
print(hex_code)

print("\141")
print("\x61")

s = '''
これはトリプクオート文字列です。改行も自由に記述できます。
シングルクオートの三重引用符の間なら、
ダブルクオートの三重引用符"""も入れられます（逆も可）。
エスケープシーケンス\n\tも含められます。
'''

print(s)

raw_str = r'C:\Users\deepinseider\Documents\work\data.txt'
print(raw_str)
raw_str

x = 1
y = 100
result = f'{x} + {y} = {x + y}'
print(result)

user_input = input('input some number:')
int_value = int(user_input)
result = str(int_value) + ' * 2 = ' + str(int_value * 2)
print(result)

