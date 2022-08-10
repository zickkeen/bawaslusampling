import streamlit as st

st.header("Aplikasi Perhitungan Sampel Parpol")

chikuadrat = 3.84
populasi = st.number_input("Masukan Populasi",format="%.0f")
galatpendugaan = 0.05
proporsi = 0.5
sampel = st.button("Hitung Sampel")

if (bool(populasi)):
    results = (chikuadrat * populasi * proporsi * (1-proporsi)) / ((populasi - 1) * (galatpendugaan**2) + chikuadrat * proporsi *(1-proporsi))
    st.write("Jumlah Sampel Verifikasi Faktual: ", round(results))
    interval = populasi / results
    st.write("dengan interval: ", round(interval))
    
elif(populasi == 0):
  st.write("Populasi Masih kosong")
else:
    st.write("Data gagal diproses")