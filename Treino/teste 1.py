import numpy as np
import cv2


# Capturar a imagem da webcam (ou carregar uma imagem)
cap = cv2.VideoCapture(0)

while True:
    # Ler o quadro da webcam
    ret, frame = cap.read()

    # Converter a imagem para o espaço de cores HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir o intervalo de cores para detectar (ex: vermelho)
    lower_color = np.array([0, 120, 70])
    upper_color = np.array([10, 255, 255])

    # Criar uma máscara com base no intervalo de cores
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Filtrar a imagem original com a máscara
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Ajuste este valor conforme necessário
            # Desenhar um retângulo ao redor do contorno detectado
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar a imagem original e a imagem filtrada
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()
