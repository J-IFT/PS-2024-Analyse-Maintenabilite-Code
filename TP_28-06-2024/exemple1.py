import cv2

def load(image_path):
    try:
        image = cv2.imread(image_path)
        return image
    except Exception as e:
        print(f"Erreur lors du chargement de l'image : {e}")

def convert(image):
    try:
        height, width, _ = image.shape
        for i in range(height):
            for j in range(width):
                image[i, j] = (int(image[i, j, 0]) + int(image[i, j, 1]) + int(image[i, j, 2])) // 3
        return image
    except Exception as e:
        print(f"Erreur {e}")
        return None

def blur(image, kernel_size=(5, 5)):
    try:
        blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
        return blurred_image
    except Exception as e:
        print(f"Erreur {e}")
        return None

def threshold(image, threshold=127):
    try:
        height, width = image.shape
        for i in range(height):
            for j in range(width):
                if image[i, j] > threshold:
                    image[i, j] = 255
                else:
                    image[i, j] = 0
        return image
    except Exception as e:
        print(f"Erreur {e}")
        return None

def save(image, output_path):
    try:
        cv2.imwrite(output_path, image)
        print("Image traitée enregistrée avec succès :", output_path)
    except Exception as e:
        print(f"Erreur {e}")

def main():
    image_path = "example_image.jpg"
    original_image = load(image_path)

    image = threshold(convert(blur(original_image)))
    output_path = "processed_image.jpg"
    save(image, output_path)


main()
