from app.repository.user.exceptions import FileTypeNotSupportedError
from PIL.Image import open as pillow_read_image
from fastapi import UploadFile
from os.path import dirname, exists
from os import makedirs
from io import BytesIO


PROFILE_IMAGES_PATH = f'{dirname(dirname(dirname(dirname(dirname(__file__)))))}\profile_images'


if not exists(PROFILE_IMAGES_PATH):
    makedirs(PROFILE_IMAGES_PATH)


def save_profile_image(profile_image_name: str, profile_image: UploadFile) -> None:
    
    image_type = profile_image.filename.split('.')[-1]

    supperted_image_types = ["jpeg", "jpg", "png", "gif", "svg", "webp", "bmp", "tiff", "ico"]

    if image_type.lower() not in supperted_image_types:
        raise FileTypeNotSupportedError(f'Image type ".{image_type}" not supported.')

    profile_image_path = f'{PROFILE_IMAGES_PATH}\{profile_image_name}'

    profile_image_file = pillow_read_image(BytesIO(profile_image.file.read()))

    if profile_image_file.mode != 'RGB':
        profile_image_file = profile_image_file.convert('RGB')

    profile_image_file.save(profile_image_path, format='jpeg')



def get_profile_image(im_name: str) -> bytes:
    with open(f'{PROFILE_IMAGES_PATH}/{im_name}.jpeg', "rb") as image_file:
        image_bytes = image_file.read()

    return image_bytes