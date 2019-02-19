import base64


class ImageHelper:

    @staticmethod
    def read_image_as_base64_string(photo_uri):
        with open(photo_uri, "rb") as imageFile:
            return base64.b64encode(imageFile.read()).decode("utf-8")
