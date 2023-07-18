import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4) # QRCode changes the border, it's colour etc
qr.add_data("https://www.google.com/")
qr.make(fit=True)

img=qr.make_image(fill_color="red", back_color="white")
img.save("colourful_qrcode_wscube_20project_in_python_youtube.png")