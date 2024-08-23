import os
import shutil
import random

# Diretório das imagens
source_dir = r'C:\Users\Felipe Almeida\Downloads\CriarHaarcascade\imagens\comMascara'
# Diretórios das classes
class1_dir = os.path.join(source_dir, 'classe1')
class2_dir = os.path.join(source_dir, 'classe2')

# Cria as pastas para as classes se não existirem
os.makedirs(class1_dir, exist_ok=True)
os.makedirs(class2_dir, exist_ok=True)

# Lista de imagens
image_list = os.listdir(source_dir)
image_list = [img for img in image_list if os.path.isfile(os.path.join(source_dir, img))]

# Embaralha a lista de imagens
random.shuffle(image_list)

# Divide as imagens em duas partes
split_index = len(image_list) // 2
class1_images = image_list[:split_index]
class2_images = image_list[split_index:]

# Move as imagens para as pastas apropriadas
for image_name in class1_images:
    src_path = os.path.join(source_dir, image_name)
    dst_path = os.path.join(class1_dir, image_name)
    shutil.move(src_path, dst_path)
    print(f'Movido {image_name} para {class1_dir}')

for image_name in class2_images:
    src_path = os.path.join(source_dir, image_name)
    dst_path = os.path.join(class2_dir, image_name)
    shutil.move(src_path, dst_path)
    print(f'Movido {image_name} para {class2_dir}')

print("Organização concluída.")
