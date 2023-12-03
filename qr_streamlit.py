import streamlit as st
from PIL import Image
import qrcode



# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Page Title',page_icon=':skull_and_crossbones:', )


with st.container():
    st.title('QR Code Generator')
    st.write('K1.Adili')
    st.write('##')
    st.subheader('Write your Text at below and press Ctrl+Enter')


with st.container():
    col1, col2 = st.columns((2,1))
    
    with col1:
        txt = st.text_area(
        "Type your text",
        value="Keyvan Adili",
        height=250
        )


        st.write(f'You wrote {len(txt)} characters.')

        if st.button('Generate'):
            pass
            # st.code(myuuid)

        # img = qrcode.make(input('Text: '))
        img = qrcode.make(txt)
        type(img)  # qrcode.image.pil.PilImage
        img.save("qr.png")
    
    
    with col2:
        image = Image.open('qr.png')
        st.image(image, caption='Scan with Mobile')
    st.write('---')
