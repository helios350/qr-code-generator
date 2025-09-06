import qrcode
import streamlit as st
from io import BytesIO

st.title("QR Code Generator by helios350")

data = st.text_input("Enter text or URL:")
if st.button("Generate QR"):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format="PNG")
    st.image(buf, caption="Generated QR Code")
    st.download_button("Download QR", buf.getvalue(), "qr.png", "image/png")