#In [1]
import os
print(os.getcwd())

#In [2]
import os
os.chdir('..')#相対パス
print(os.getcwd())
os.chdir('/home/jovyan/binder')# 絶対パス
print(os.getcwd())

#In [3]
print('using os.listdir')
for name in os.listdir():
    if os.path.isfile(name):
        print(f'file:{name}')
    else:
        print(f'dir: {name}')

print('using os.scandir')
for entry in os.scandir():
    if entry.is_file():
        print(f'file: {entry.name}')
    else:
        print(f'dir: {entry.name}')

#In [4]
os.mkdir('foo')#カレントディレクトリにfooディレクトリを作成
os.mkdir('foo/bar/baz')#エラー

#In [5]
os.makedirs('foo/bar/baz')
os.chdir('foo?bar/baz')
print(os.getcwd())
os.chdir('../../..')
print(os.getcwd())

#In [6]
os.system('echo foo > foo/foo.txt')
os.remove('foo/foo.txt')

#In [7]
os.rmdir('foo/bar/baz')# foo/barディレクトリにあるbazディレクトを削除
print(os.listdir('foo/bar'))# bazディレクトが削除されたことを確認

os.mkdir('foo/bar/baz')# foo/bar/bazディレクトリを再作成
os.removedirs('foo/bar/baz')# foo. bar. bazの３つのディレクトリを削除
os.chdir('foo')# fooディレクトリがないので例外となる

#In [8]
os.makedirs('foo/bar/baz')
os.system('echo foo > foo/foo.txt')
os.system('echo bar > foo/bar/bar.txt')
os.system('echo baz > foo/bar/baz/baz.txt')
os.rmdir('foo/bar/baz')

#In [9]
os.removedirs('foo/bar/baz')

#In [10]
os.remove('foo/bar/baz/baz.txt')
os.rmdir('foo/bar/baz')
print(os.listdir('foo/bar'))

#In [11]
os.remove('foo/bar/bar.txt')
os.removedirs('foo/bar')
print(os.listdir())
print(os.listdir('foo'))

#In [12]
os.mkdir('aaa')
os.mkdir('xxx')
os.system('echo aaa > aaa/aaa.txt')
os.system('echo xxx > xxx/xxx.txt')

os.rename('aaa/aaa.txt', 'xxx/aaa.txt')# [aaa/aaa.txt]を[xxx/aaa.txt]に変更
os.rename('xxx/aaa.txt', 'aaa/bbb.txt')# [xxx/aaa.txt]を「aaa/bbb.txt]に変更
os.rename('aaa/bbb.txt', 'xxx/xxx.txt')# [xxx/xxx.txt]はすでに存在している

#In [13]
os.renames('xxx/xxx.txt', 'aaa/bbb/bbb.txt')#成功
os.rename('aaa/bbb/bbb.txt', 'xxx/yyy/yyy.txt')#例外

#In [14]
os.makedirs('top/aaa/bbb')
os.makedirs('top/xxx/yyy')
os.system('echo aaa > top/aaa/aaa.txt')
os.system('echo bbb > top/aaa/bbb/bbb.txt')
os.system('echo xxx > top/xxx/xxx.txt')
os.system('echo yyy > top/xxx/yyy/yyy.txt')

#In [15]
for dirpath, dirnames, filenames in os.walk('top', topdown=True):
    print(f'now in {dirpath}')
    print(f'dirs in {dirpath}: {dirnames}')
    print(f'files in {dirpath}: {filenames}')

#In [16]
for dirpath, dirnames, filenames in os.walk('top', topdown=False):
    print(f'now in {dirpath}')
    print(f'dirs in {dirpath}: {dirnames}')
    print(f'files in {dirpath}: {filenames}')

#In [17]
path1 = 'foo'
path2 = 'bar'
filename = 'baz.txt'

print(os.path.join(path1, path2, filename))

#In [18]
path1 = 'foo'
path2 = 'bar'
filename = 'baz.txt'

print(os.path.join(path1,path2, filename))