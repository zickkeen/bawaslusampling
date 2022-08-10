import streamlit as st

st.set_page_config(page_title="Verifikasi Parpol Calculator", page_icon="📊")

st.markdown("# Verifikasi Parpol Calculator")
st.sidebar.header("Verifikasi Parpol Calculator")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)


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