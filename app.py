# main.py
import streamlit as st
import time
from generate_label import get_label


def main():

    st.set_page_config(
        page_title="Aplikasi Kategori Berita | Klasifikasi Berita Kompas", page_icon="📺")

    col1, col2 = st.columns(2)

    with col1:

        st.image("assets/banner.png", use_column_width=True)

    with col2:
        st.subheader("Aplikasi Kategori untuk Berita")
        st.caption("Arshelia Romadhona | 200411100053")

    news_text = st.text_area(
        "Masukkan Isi Berita", key="input_text", height=250)

    if st.button("Cari Kategori"):
        if news_text:
            text = get_label(news_text)
            with st.expander('Tampilkan Hasil'):
                st.write('Berita yang anda masukkan termasuk dalam kategori: ')
                if text == "Health":
                    st.info(text, icon="🧑‍🏫")
                    url = "https://health.kompas.com/?source=navbar"
                    st.write(
                        'Baca juga berita terbaru terkait Health 🔎 [Berita edukasi hari ini](%s)'  %url)
                elif text == "Tekno":
                    st.info(text, icon="🚣")
                    url = "https://tekno.kompas.com/?source=navbar"
                    st.write(
                        'Baca juga berita terbaru terkait Teknologi 🔎 [Berita olahraga hari ini](%s)'  %url)
                elif text == "Bola":
                    st.info(text, icon="💸")
                    url = "https://bola.kompas.com/?source=navbar"
                    st.write(
                        'Baca juga berita terbaru terkait Bola 🔎 [Berita ekonomi hari ini](%s)'  %url)
        else:
            time.sleep(.5)
            st.toast('Masukkan teks terlebih dahulu', icon='🤧')


if __name__ == "__main__":
    main()
