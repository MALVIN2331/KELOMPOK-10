import streamlit as st

st.set_page_config(page_title="MODULE ALAT INSTRUMENT", page_icon=":microscope:")

st.title('MODULE CARA PENGGUNAAN ALAT INSTRUMENT')

menu = ["HIGH PEFORMANCE LIQUID CHROMATHOGRAPHY"]
choice = st.sidebar.selectbox("select a tool",menu)

if choice == "HIGH PEFORMANCE LIQUID CHROMATHOGRAPHY":
    st.title("HIGH PEFORMANCE LIQUID CHROMATHOGRAPHY Single Standart")
    st.write("CARA MENGGUNAKAN HIGH PEFORMANCE LIQUID CHROMATHOGRAPHY :")
    st.write("1. Persiapan sampel: Sampel yang akan dianalisis harus disiapkan terlebih dahulu, misalnya dengan cara pengambilan atau ekstraksi.")
    st.write("2. Persiapan fase gerak dan fase diam: Fase gerak adalah cairan yang digunakan untuk memompa sampel melalui kolom. Fase diam adalah bahan pengisi kolom yang memiliki sifat-sifat tertentu, seperti pori-pori dan ukuran butir yang dapat mempengaruhi pemisahan senyawa-senyawa dalam sampel.")
    st.write("3. Pengaturan aliran fase gerak: Aliran fase gerak harus dikalibrasi dengan baik, sehingga cairan dapat mengalir dengan kecepatan dan tekanan yang sesuai.")
    st.write("4. Injeksi sampel: Sampel yang telah disiapkan dimasukkan ke dalam alat HPLC melalui injektor.")
    st.write("5. Pemisahan senyawa: Sampel kemudian mengalir melalui kolom yang diisi dengan fase diam. Senyawa-senyawa dalam sampel akan terpisah berdasarkan sifat-sifatnya masing-masing.")
    st.write("6. Deteksi senyawa: Setelah senyawa-senyawa terpisah, mereka akan dideteksi oleh detektor yang terhubung dengan alat HPLC. Detektor ini biasanya menggunakan metode spektrofotometri atau elektrokimia untuk mendeteksi senyawa-senyawa tersebut.")
    st.write("7. Analisis data: Data hasil deteksi senyawa-senyawa diolah dan dianalisis untuk mengidentifikasi senyawa-senyawa yang terdapat dalam sampel dan konsentrasi masing-masing senyawa")
    st.write(" Output yang dihasilkan dari alat HIGH PEFORMANCE LIQUID CHROMATHOGRAPHY, yaitu:")
    st.write("1. Luas Area.")
    st.write("2. Waktu Retensi.")
    st.write("3. Tinggi Peak.")
    st.write("=>PERHITNGAN KADAR ANALIT")
    st.write("KADAR ANALIT = LUAS AREA SAMPEL * KONSENTRASI STANDAR / LUAS AREA STANDAR")
    
    LuasAreaSPL = st.number_input("enter the Luas Area SPL:", min_value=0.0, step=0.1)
    LuasAreaSTD = st.number_input("enter the Luas Area STD:", min_value=0.0, step=0.1)
    KonsentrasiSTD = st.number_input("enter the KONSENTRASI STANDAR:", min_value=0.0, step=0.1)
    
    if st.button("Calculate HPLC"):
        KADARANALIT = LuasAreaSPL*KonsentrasiSTD/LuasAreaSTD
        st.write(f"Hasil KADAR ANALIT ADALAH {KADARANALIT:.2f} %")