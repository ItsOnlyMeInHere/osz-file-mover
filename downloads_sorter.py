import os

print("Назовите папку:")
directory = str(input())

print("Введите имя пользователя (чтобы вас могли взломать)")
username = str(input())
parent_dir = os.path.join('C:/users/%s/downloads' % username)

qpath = os.path.join(parent_dir, directory)
os.mkdir(qpath)
print("Папка", qpath, " успешно создана") 

for file in os.listdir(parent_dir):
    if file.endswith(".osz"):
        src_path = os.path.join(parent_dir, file)
        dst_path = os.path.join(qpath, file)
        os.rename(src_path, dst_path)
print('Победа!')