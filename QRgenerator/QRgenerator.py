import qrcode
from PIL import Image

# Pedir al usuario el enlace a convertir
link = input("Introduce el enlace: ")

# Crear el objeto QR
qr_object = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Añadir los datos al objeto QR
qr_object.add_data(link)
qr_object.make(fit=True)

# Crear una imagen a partir del objeto QR
qr_img = qr_object.make_image(fill_color="black", back_color="white")
qr_img.save("qr_code.png")

# Mostrar el código QR generado
img = Image.open("qr_code.png")
img.show()