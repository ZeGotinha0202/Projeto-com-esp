from data_pipeline import load_dataset
import tensorflow as tf

# Configurações
batch_size = 32
epochs = 50
num_classes = 1  # Ajuste o número de classes conforme necessário

# Carrega o dataset
train_dataset = load_dataset(r'C:\Users\Felipe Almeida\Desktop\tfrecord_output\dataset.tfrecord')

# Configura o pipeline de dados
train_dataset = train_dataset.batch(batch_size).prefetch(tf.data.AUTOTUNE)

# Defina o modelo aqui
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(224, 224, 3)),  # Certifique-se de que o input shape está correto
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')  # Aqui num_classes deve ser o número total de classes
])

# Compile o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # Utilize sparse_categorical_crossentropy se os rótulos forem inteiros
              metrics=['accuracy'])

# Treine o modelo
model.fit(train_dataset, epochs=epochs)

# Debug: verifique o formato das imagens e rótulos
for image, labels in train_dataset.take(1):
    print("Image shape:", image.shape)
    print("Labels shape:", labels.shape)  # Ajuste conforme a forma dos rótulos
