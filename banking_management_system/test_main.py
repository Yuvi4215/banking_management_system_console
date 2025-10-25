import qrcode
import shutil
from io import StringIO
import sys

# --- Your UPI link ---
upi_link = (
    "upi://pay?"
    "pa=7775090578@ybl&"
    "pn=YUVRAJ%20RAJENDRAKUMAR%20VARMA&"
    "mc=0000&"
    "mode=02&"
    "purpose=00"
)

# --- Create smaller QR ---
qr = qrcode.QRCode(version=2, border=1)
qr.add_data(upi_link)
qr.make(fit=True)

# --- Capture QR output as text ---
old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()
qr.print_ascii()
sys.stdout = old_stdout

qr_text = mystdout.getvalue().splitlines()

# --- Get terminal width ---
terminal_width = shutil.get_terminal_size().columns

# --- Print each line centered ---
for line in qr_text:
    print(line.center(terminal_width))
