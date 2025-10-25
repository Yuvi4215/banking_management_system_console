import qrcode
from io import StringIO
from core.utils.console_utils import print_content



def display_qrcode(amount,indentation=0.75):
    upi_link = (
        "upi://pay?"
        "pa=7775090578@ybl&"
        "pn=YUVRAJ%20RAJENDRAKUMAR%20VARMA&"
        "mc=0000&"
        "mode=02&"
        "purpose=00&"
        f"am={amount}"
    )

    qr = qrcode.QRCode(version=2, border=1)
    qr.add_data(upi_link)
    qr.make(fit=True)

    # Capture output
    buf = StringIO()
    qr.print_ascii(out=buf)
    
    qr_text = buf.getvalue().splitlines()

    for line in qr_text:
        print_content(line,"content",indentation)
    
if __name__=="__main__":
    display_qrcode(500)
