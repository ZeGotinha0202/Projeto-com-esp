import cv2
import os

drawing = False
ix, iy = -1, -1
bounding_boxes = []

def draw_bounding_box(event, x, y, flags, param):
    global ix, iy, drawing, img, bounding_boxes

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        bounding_boxes.append((ix, iy, x, y))
        cv2.imshow('image', img)

def save_bounding_boxes(image_path, boxes):
    image_name = os.path.basename(image_path)
    txt_file = image_name.split('.')[0] + '.txt'

    with open(txt_file, 'w') as f:
        for box in boxes:
            ix, iy, x, y = box
            f.write(f"{ix},{iy},{x},{y}\n")

    print(f"Bounding boxes salvas em: {txt_file}")

def process_images_in_folder(folder_path):

    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png') or f.endswith('.jpg')]

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print(f"Abrindo {image_file}")

        global img
        img = cv2.imread(image_path)

        if img is None:
            print(f"Erro ao carregar a imagem: {image_file}")
            continue

        global bounding_boxes
        bounding_boxes = []

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_bounding_box)

        while True:
            cv2.imshow('image', img)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('s'):
                save_bounding_boxes(image_path, bounding_boxes)
                break
            elif key == ord('q'):
                break

        cv2.destroyAllWindows()

folder_path = r'C:\Users\Felipe Almeida\Downloads\CriarHaarcascade\imagens\comMascara'

process_images_in_folder(folder_path)
