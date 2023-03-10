from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    ext = os.path.split(value.name)[1] #cover-image.png
    print(ext)
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if  ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension. Allowed extensions: "+ str(valid_extensions))

        