import tensorflow as tf
import cv2
import numpy as np

# Carregar o modelo treinado
model = tf.keras.models.load_model('target_detection_model.h5')


def detect_and_draw_targets(image_path):
    # Carregar e pré-processar a imagem
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (150, 150))
    image_array = np.expand_dims(image_resized, axis=0) / 255.0

    # Fazer a previsão
    prediction = model.predict(image_array)
    class_index = (prediction > 0.5).astype(int)[0][0]

    # Definir as classes
    class_names = ['No Target', 'Target']
    label = class_names[class_index]

    # Adicionar o texto de previsão
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    font_color = (0, 255, 0)  # Verde
    font_thickness = 1
    text_size, _ = cv2.getTextSize(f'Prediction: {label}', font, font_scale, font_thickness)
    text_x = 10
    text_y = 30 + text_size[1]

    cv2.putText(image, f'Prediction: {label}', (text_x, text_y), font, font_scale, font_color, font_thickness)

    if class_index == 1:  # Se o alvo for detectado
        # Adicionar uma caixa delimitadora (exemplo simplificado)
        height, width, _ = image.shape
        start_point = (width // 4, height // 4)
        end_point = (3 * width // 4, 3 * height // 4)
        color = (0, 255, 0)  # Verde
        thickness = 2
        image = cv2.rectangle(image, start_point, end_point, color, thickness)

    # Mostrar o resultado
    cv2.imshow('Detected Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_and_draw_targets(r'C:\Users\Felipe Almeida\Downloads\images.jpg')
