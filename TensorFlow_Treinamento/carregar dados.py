import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Diretórios das imagens
train_dir = r'C:\Users\Felipe Almeida\Downloads\CriarHaarcascade\imagens'
val_dir = r'C:\Users\Felipe Almeida\Downloads\CriarHaarcascade\imagens'

# Gerador de dados para treinamento e validação
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

validation_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)
