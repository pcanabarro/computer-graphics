import cv2
import os

def detect_license_plate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 11, 17, 17)
    edges = cv2.Canny(blur, 30, 200)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            if 2 < aspect_ratio < 6:
                return (x, y, w, h)
    return None

def crop_and_resize(image, bbox, margin_ratio=0.4, output_size=(400, 200)):
    x, y, w, h = bbox
    x1 = max(int(x - w * margin_ratio), 0)
    y1 = max(int(y - h * margin_ratio), 0)
    x2 = min(int(x + w * (1 + margin_ratio)), image.shape[1])
    y2 = min(int(y + h * (1 + margin_ratio)), image.shape[0])
    cropped = image[y1:y2, x1:x2]
    return cv2.resize(cropped, output_size)

def process_dataset(input_folder="dataset", output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

    total = len(image_files)
    processed = 0

    for file_name in image_files:
        image_path = os.path.join(input_folder, file_name)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Erro ao carregar: {file_name}")
            continue

        bbox = detect_license_plate(image)

        if bbox:
            focused = crop_and_resize(image, bbox)
            save_path = os.path.join(output_folder, file_name)
            cv2.imwrite(save_path, focused)
            processed += 1
        else:
            print(f"Placa não detectada em: {file_name}")

    print(f"\n Finalizado: {processed}/{total} imagens processadas com sucesso.")

if __name__ == "__main__":
    process_dataset()
