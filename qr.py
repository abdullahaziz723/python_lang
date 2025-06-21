import qrcode

# 1. Encode a simple text message
message = "Hello pipi yeh lo QR code! pglu"
qr = qrcode.QRCode(
    version=1,
    # error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(message)
qr.make(fit=True)

# 2. Create an image from the QR code
img = qr.make_image(fill_color="blue", back_color="white")

# 3. Show or save the QR code
img.show()               # Shows the QR code
img.save("my_qr.png")    # Saves the QR code as an image
