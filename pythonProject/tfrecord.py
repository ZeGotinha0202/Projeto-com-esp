import tensorflow as tf
import os
import cv2
import io
from PIL import Image

# Função para converter as coordenadas em formato TFRecord
def create_tf_example(image_path, label_path):
    # Ler a imagem
    img = cv2.imread(image_path)
    height, width, channels = img.shape

    # Converter a imagem para bytes
    with tf.io.gfile.GFile(image_path, 'rb') as fid:
        encoded_image_data = fid.read()

    # Criar um objeto Image do PIL para obter o formato da imagem
    encoded_image = Image.open(io.BytesIO(encoded_image_data))
    image_format = encoded_image.format.lower().encode('utf-8')  # Formato da imagem (jpeg, png)

    # Ler o arquivo .txt para extrair as bounding boxes
    xmins = []  # Lista para as coordenadas xmin
    xmaxs = []  # Lista para as coordenadas xmax
    ymins = []  # Lista para as coordenadas ymin
    ymaxs = []  # Lista para as coordenadas ymax
    classes_text = []  # Nomes das classes
    classes = []  # IDs das classes

    with open(label_path, 'r') as f:
        for line in f.readlines():
            data = line.strip().split(',')
            xmin, ymin, xmax, ymax = list(map(float, data[:4]))
            class_name = 'target'  # Substitua pelo nome da classe
            class_id = 1  # ID da classe, geralmente começando de 1

            # Normalizar as coordenadas (entre 0 e 1)
            xmins.append(xmin / width)
            xmaxs.append(xmax / width)
            ymins.append(ymin / height)
            ymaxs.append(ymax / height)
            classes_text.append(class_name.encode('utf-8'))
            classes.append(class_id)

    # Criar o exemplo TFRecord
    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': tf.train.Feature(int64_list=tf.train.Int64List(value=[height])),
        'image/width': tf.train.Feature(int64_list=tf.train.Int64List(value=[width])),
        'image/filename': tf.train.Feature(bytes_list=tf.train.BytesList(value=[os.path.basename(image_path).encode('utf-8')])),
        'image/source_id': tf.train.Feature(bytes_list=tf.train.BytesList(value=[os.path.basename(image_path).encode('utf-8')])),
        'image/encoded': tf.train.Feature(bytes_list=tf.train.BytesList(value=[encoded_image_data])),
        'image/format': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_format])),
        'image/object/bbox/xmin': tf.train.Feature(float_list=tf.train.FloatList(value=xmins)),
        'image/object/bbox/xmax': tf.train.Feature(float_list=tf.train.FloatList(value=xmaxs)),
        'image/object/bbox/ymin': tf.train.Feature(float_list=tf.train.FloatList(value=ymins)),
        'image/object/bbox/ymax': tf.train.Feature(float_list=tf.train.FloatList(value=ymaxs)),
        'image/object/class/text': tf.train.Feature(bytes_list=tf.train.BytesList(value=classes_text)),
        'image/object/class/label': tf.train.Feature(int64_list=tf.train.Int64List(value=classes)),
    }))

    return tf_example

# Função para gerar o arquivo TFRecord
def create_tfrecord(output_path, image_folder, label_folder):
    writer = tf.io.TFRecordWriter(output_path)

    # Varrer as imagens na pasta
    for image_file in os.listdir(image_folder):
        if image_file.endswith('.png') or image_file.endswith('.jpg'):
            image_path = os.path.join(image_folder, image_file)
            label_path = os.path.join(label_folder, image_file.split('.')[0] + '.txt')

            if not os.path.exists(label_path):
                print(f"Label {label_path} não encontrado, pulando...")
                continue

            tf_example = create_tf_example(image_path, label_path)
            writer.write(tf_example.SerializeToString())

    writer.close()
    print(f"Arquivo TFRecord salvo em: {output_path}")

# Caminhos para as imagens e labels
image_folder = r'C:\Users\Felipe Almeida\Downloads\CriarHaarcascade\imagens\comMascara'
label_folder = r'C:\Users\Felipe Almeida\Desktop\Tentativa 3162\pythonProject\Labels'
output_path = r"C:\\Users\\Felipe Almeida\\Desktop\\dataset.tfrecord"

# Criar o TFRecord
create_tfrecord(output_path, image_folder, label_folder)
