"""
Equipe 7 BRASA Hacks 2020

Freezer Infinito
"""

import pyqrcode  

class QRcode:
    
    def qr_generator(data):

        link = "https://www.ze.delivery/"
        url = pyqrcode.create(link)
        _id = str(data[0])+str(data[1])+str(data[2])+str(data[3])+str(data[4])
        url.svg("QRcode_images/"+_id+"_url.svg", scale=8)
        url.show()