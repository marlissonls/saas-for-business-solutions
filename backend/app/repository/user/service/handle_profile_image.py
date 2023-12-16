from PIL.Image import open as pillow_read_image
from fastapi import UploadFile
from os.path import dirname, exists
from os import makedirs, remove
from io import BytesIO

class FileTypeNotSupportedError(Exception):
    pass

APP_SOURCE = f'{dirname(dirname(dirname(dirname(dirname(__file__)))))}'
PROFILE_IMAGES_PATH = f'{APP_SOURCE}\profile_images'


if not exists(PROFILE_IMAGES_PATH):
    makedirs(PROFILE_IMAGES_PATH)


def save_profile_photo(profile_image_name: str, profile_image: UploadFile) -> None:
    
    image_type = profile_image.filename.split('.')[-1]

    supperted_image_types = ["jpeg", "jpg", "png", "gif", "svg", "webp", "bmp", "tiff", "ico"]

    if image_type.lower() not in supperted_image_types:
        raise FileTypeNotSupportedError

    profile_image_path = f'{PROFILE_IMAGES_PATH}\{profile_image_name}'

    profile_image_file = pillow_read_image(BytesIO(profile_image.file.read()))

    if profile_image_file.mode != 'RGB':
        profile_image_file = profile_image_file.convert('RGB')

    profile_image_file.save(profile_image_path, format='jpeg')



def delete_profile_photo(profile_photo_name: str) -> None:

    profile_photo_path = f'{PROFILE_IMAGES_PATH}\{profile_photo_name}.jpeg'

    remove(profile_photo_path)
