import streamlit as st

st.set_page_config(page_title="MODULE ALAT INSTRUMENT", page_icon=":microscope:")

st.title('MODULE CARA PENGGUNAAN ALAT INSTRUMENT')

menu = ["CHROMATHOGRAPHY GAS"]
choice = st.sidebar.selectbox("select a tool",menu)

if choice == "CHROMATHOGRAPHY GAS":
    st.title("CHROMATHOGRAPHY GAS Single Standart")
    st.write("CARA MENGGUNAKAN GAS CHROMATOGRAPHY :")
    st.write("1. Persiapan sampel: Sampel harus diolah dan di reduksi sesuai dengan matriksnya sebelum dimasukkan ke dalam kolom GC.")
    st.write("2. Inisialisasi kolom: Kolom GC harus dipersiapkan dengan memasukkan bahan pengisi kolom dan memastikan bahwa kolom tersebut dalam kondisi stabil.")
    st.write("3. Injeksi sampel: Sampel harus diinjeksikan ke dalam kolom dengan menggunakan injektor GC., Analisis: Setelah sampel dimasukkan, kolom akan memisahkan komponen-komponen dalam sampel dan membuang mereka melalui detektor. Detektor akan memantau setiap komponen dan menghasilkan grafik yang menunjukkan daerah elusi.")
    st.write("4. Interpretasi hasil: Hasil analisis harus diterjemahkan dan dianalisis untuk menentukan konsentrasi dan identifikasi komponen-komponen dalam sampel.")
    st.write(" Output yang dihasilkan dari alat Gas CHROMAHOGRAPHY, yaitu:")
    st.write("1. Luas Area.")
    st.write("2. Waktu Retensi.")
    st.write("3. Tinggi Peak.")
    st.write("=> PERHITUNGAN KADAR ANALIT :")
    st.write("KADAR ANALIT = Luas Area SPL * (persen larutan sampel x FP) / Luas Sampel STD")
    
    LuasAreaSPL = st.number_input("enter the Luas Area SPL:", min_value=0.0, step=0.1)
    LuasAreaSTD = st.number_input("enter the Luas Area STD:", min_value=0.0, step=0.1)
    PersenLarutanSPL = st.number_input("enter the PersenLarutanSPL:", min_value=0.0, step=0.1)
    FP = st.number_input("enter the FP:", min_value=0.0, step=0.1)
    
    if st.button("Calculate GC"):
        KADARANALIT = LuasAreaSPL*PersenLarutanSPL*FP/LuasAreaSTD
        st.write(f"Hasil KADAR ANALIT ADALAH {KADARANALIT:.2f} %")