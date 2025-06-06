# Method - 2 to make the QRCode of our choice!!
import qrcode
from PIL import Image

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
data = "https://nptel24cs19s35780068630789867.netlify.app/"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("nptel24cs19s35780068630789867.jpg")