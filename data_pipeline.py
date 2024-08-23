import tensorflow as tf


def _parse_function(proto):
    # Define o formato do seu dataset TFRecord
    keys_to_features = {
        'image/height': tf.io.FixedLenFeature([], tf.int64),
        'image/width': tf.io.FixedLenFeature([], tf.int64),
        'image/filename': tf.io.FixedLenFeature([], tf.string),
        'image/source_id': tf.io.FixedLenFeature([], tf.string),
        'image/encoded': tf.io.FixedLenFeature([], tf.string),
        'image/format': tf.io.FixedLenFeature([], tf.string),
        'image/object/bbox/xmin': tf.io.FixedLenFeature([1], tf.float32),
        'image/object/bbox/xmax': tf.io.FixedLenFeature([1], tf.float32),
        'image/object/bbox/ymin': tf.io.FixedLenFeature([1], tf.float32),
        'image/object/bbox/ymax': tf.io.FixedLenFeature([1], tf.float32),
        'image/object/class/text': tf.io.FixedLenFeature([1], tf.string),
        'image/object/class/label': tf.io.FixedLenFeature([1], tf.int64),
    }
    parsed_features = tf.io.parse_single_example(proto, keys_to_features)

    # Decodifique a imagem
    image = tf.image.decode_image(parsed_features['image/encoded'], channels=3, expand_animations=False)
    image = tf.image.resize(image, [224, 224])  # Ajuste o tamanho conforme necessário
    image = tf.cast(image, tf.float32) / 255.0  # Normaliza a imagem para o intervalo [0, 1]

    # Obtenha o rótulo
    label = tf.cast(parsed_features['image/object/class/label'], tf.int32)

    # Remove a dimensão extra do rótulo (se necessário)
    label = tf.squeeze(label, axis=0)

    return image, label


def load_dataset(filename):
    # Cria um dataset a partir do arquivo TFRecord
    dataset = tf.data.TFRecordDataset(filename)
    dataset = dataset.map(_parse_function)
    return dataset
