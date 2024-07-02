""" Module : Traitement d'images """

try:
    import numpy as np
except ImportError as import_exception:
    raise ImportError("La bibliothèque Numpy n'est pas installée. Veuillez l'installer avant d'exécuter cette fonction.") from import_exception

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


def load(load_path: str) -> np.ndarray:
    """
    Charge une image à partir de son path.

    Paramètres :
    load_path (str): Chemin de l'image à charger.

    Retourne :
    np.ndarray: L'image chargée sous forme d'un tableau numpy.
    
    Lève :
    ImageLoadError: Si le chargement de l'image échoue.
    """
    try:
        loaded_image = cv2.imread(load_path)
        if loaded_image is None:
            raise ImageLoadError(f"Erreur lors du chargement de l'image : {load_path}")
        return loaded_image
    except Exception as e:
        raise ImageLoadError(f"Erreur lors du chargement de l'image : {str(e)}") from e

def convert(image_to_convert: np.ndarray) -> np.ndarray:
    """
    Convertit une image en nuances de gris.

    Paramètres :
    image_to_convert (np.ndarray): L'image à convertir, tableau numpy à 3 dimensions.

    Retourne :
    np.ndarray: L'image convertie en nuances de gris.

    Lève :
    ImageConvertError: Si la conversion échoue.
    """
    try:
        gray_image = cv2.cvtColor(image_to_convert, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    except Exception as e:
        raise ImageConvertError(f"Erreur lors de la conversion de l'image : {str(e)}") from e

def threshold(image_to_threshold: np.ndarray, threshold=127) -> np.ndarray:
    """
    Applique un seuillage à une image.

    Paramètres :
    image_to_threshold (np.ndarray): L'image à seuiller.
    threshold (int): Valeur de seuil (0-255).

    Retourne :
    np.ndarray: L'image seuillée.

    Lève :
    ImageThresholdError: Si l'application du seuil échoue.
    """
    try:
        if image_to_threshold.ndim == 2:  # Image en niveaux de gris
            _, thresholded_image = cv2.threshold(image_to_threshold, threshold, 255, cv2.THRESH_BINARY)
            return thresholded_image
        elif image_to_threshold.ndim == 3:  # Image en couleur
            gray_image = cv2.cvtColor(image_to_threshold, cv2.COLOR_BGR2GRAY)
            _, thresholded_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
            return cv2.cvtColor(thresholded_image, cv2.COLOR_GRAY2BGR)
        else:
            raise ValueError("Format d'image non pris en charge : doit être 2D (niveaux de gris) ou 3D (couleur).")
    except Exception as e:
        raise ImageThresholdError(f"Erreur lors de l'application du seuil sur l'image : {str(e)}") from e

def save(image: np.ndarray, output_path: str):
    """
    Enregistre une image traitée.

    Paramètres :
    image (np.ndarray): L'image à enregistrer.
    output_path (str): Chemin de sortie pour enregistrer l'image.

    Lève :
    Exception: En cas d'erreur lors de l'enregistrement de l'image.
    """
    try:
        cv2.imwrite(output_path, image)
        print("Image traitée enregistrée avec succès :", output_path)
    except Exception as e:
        print(f"Erreur {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    image_path = "example_image.jpg"
    original_image = load(image_path)
    processed_image = threshold(convert(cv2.GaussianBlur(original_image, (5, 5), 0)))
    output_path = "processed_image.jpg"
    save(processed_image, output_path)
