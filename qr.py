import qrcode
# Data to encode
data =qrcode.make("https://polite-queijadas-0aa65d.netlify.app/") 

data.show()



data = ['abdillah', 'aziz', '723']
# Create QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

