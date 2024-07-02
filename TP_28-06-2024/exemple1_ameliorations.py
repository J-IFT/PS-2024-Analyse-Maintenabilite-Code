""" Module : Traitement d'images """

try:
    import numpy as np
except ImportError as import_exception:
    raise ImportError("La bibliothèque OpenCV (cv2) n'est pas installée. Veuillez l'installer avant d'exécuter cette fonction.") from import_exception

try:
    import cv2
except ImportError as import_exception:
    raise ImportError("La bibliothèque OpenCV (cv2) n'est pas installée. Veuillez l'installer avant d'exécuter cette fonction.") from import_exception


class ImageLoadError(Exception):
    """Exception levée lorsque le chargement de l'image échoue."""
class ImageBlurError(Exception):
    """Exception levée lorsque le floutage de l'image échoue."""
class ImageConvertError(Exception):
    """Exception levée lorsque la conversion de l'image échoue."""
class ImageThresholdError(Exception):
    """Exception levée lorsque l'application du seuil sur l'image échoue."""


def load(load_path: str) -> object:
    """
    Charge une image à partir de son path.

    Paramètre:
    path (str): Chemin de l'image a charger.

    Retourne:
    image: image sous forme d'objet.
    """
    loaded_image = cv2.imread(load_path)
    if loaded_image is None:
        raise ImageLoadError(f"Erreur lors du chargement de l'image : {load_path}")
    return loaded_image

def convert(image_to_convert):
    """
    Convertit une image en nuances de gris en calculant la moyenne des valeurs
    des canaux R, G et B pour chaque pixel et en les assignant à chaque canal.

    Paramètres:
    image_to_convert : L'image à convertir, sous forme d'un tableau numpy à 3 dimensions.

    Retourne:
    image: L'image convertie en nuances de gris. Retourne None si une erreur survient pendant la conversion.
    """
    try:
        height, width, _ = image_to_convert.shape
        for i in range(height):
            for j in range(width):
                gray_value = (int(image_to_convert[i, j, 0]) + int(image_to_convert[i, j, 1]) + int(image_to_convert[i, j, 2])) // 3
                image_to_convert[i, j] = [gray_value, gray_value, gray_value]
        return image_to_convert
    except Exception as convert_exception:
        raise ImageConvertError(f"Erreur lors de la conversion de l'image : {convert_exception}") from convert_exception

def blur(image_to_blur, kernel_size=(5, 5)):
    """
    Applique un flu gaussien à l'image donnée

    Paramètre:
    image_to_blur: image sous forme d'objet.
    kernel_size: 

    Retourne:
    image: image fl.
    """
    try:
        blurred_image = cv2.GaussianBlur(image_to_blur, kernel_size, 0)
        return blurred_image
    except Exception as blur_exception:
        raise ImageBlurError(f"Erreur lors de l'application du flou gaussien : {blur_exception}") from blur_exception

def threshold(image_to_threshold, threshold=127):
    """
    Applique un seuillage sur une image en convertissant chaque pixel en noir ou blanc en fonction d'un seuil spécifié.

    Paramètres:
    image_to_threshold: L'image à seuiller, sous forme d'un tableau numpy à 2 dimensions ou 3 dimensions.
    threshold (int): Valeur seuil (0-255). Les pixels avec une valeur supérieure à ce seuil seront convertis en 255 (blanc),
                     ceux avec une valeur inférieure ou égale seront convertis en 0 (noir).

    Retourne:
    np.ndarray: L'image seuillée avec des pixels noirs (0) et blancs (255). Retourne None si une erreur survient pendant le seuillage.
    """
    try:
        if np.ndim(image_to_threshold) == 2:  # Image en niveaux de gris
            height, width = image_to_threshold.shape
            for i in range(height):
                for j in range(width):
                    if image_to_threshold[i, j] > threshold:
                        image_to_threshold[i, j] = 255
                    else:
                        image_to_threshold[i, j] = 0
        elif np.ndim(image_to_threshold) == 3:  # Image en couleur
            height, width, _ = image_to_threshold.shape
            for i in range(height):
                for j in range(width):
                    if np.mean(image_to_threshold[i, j]) > threshold:
                        image_to_threshold[i, j] = [255, 255, 255]
                    else:
                        image_to_threshold[i, j] = [0, 0, 0]
        else:
            raise ValueError("Format d'image non pris en charge : doit être 2D (niveaux de gris) ou 3D (couleur).")

        return image_to_threshold

    except Exception as threshold_exception:
        raise ImageThresholdError(f"Erreur lors de l'application du seuil sur l'image : {threshold_exception}") from threshold_exception

def save(image, output_path):
    try:
        cv2.imwrite(output_path, image)
        print("Image traitée enregistrée avec succès :", output_path)
    except Exception as e:
        print(f"Erreur {e}")


image_path = "example_image.jpg"
original_image = load(image_path)

image = threshold(convert(blur(original_image)))
output_path = "processed_image.jpg"
save(image, output_path)
