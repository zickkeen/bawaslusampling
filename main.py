import streamlit as st
hide_menu = """
<style>
#MainMenu{
  visibility:hidden;
}
</style>
"""
def main():
  st.title("App Jumlah Sampling Bawaslu")
  st.subheader("Aplikasi Sederhana Perhitungan Jumlah Sampling")
  st.markdown(hide_menu,unsafe_allow_html=True)
  clicked_menu_item = st.menu_items(['Item 1', 'Item 2', 'Item 3'], expanded=True, floating=True, emphasized_items=[0])
  menu = ["Home","About"]
  choice = st.sidebar.selectbox("Menu",clicked_menu_item)

  if choice == "Home":
    st.subheader("Home")
  else:
    st.subheader("About")

st.write("""
#Aplikasi Krejie Morgan
# Ini adalah Aplikasi Sederhana Penghitungan Jumlah Sampling Dalam Verifikasi Partai Politik Pemilu Tahun 2024""")

chikuadrat = 3.84
populasi = st.number_input("masukan populasi",format="%.0f")
galatpendugaan = 0.05
proporsi = 0.5
sampel = st.button("Hitung Sampel")

# results = st.write('hasil')

if (bool(populasi)):
    results = (chikuadrat * populasi * proporsi * (1-proporsi)) / ((populasi - 1) * (galatpendugaan**2) + chikuadrat * proporsi *(1-proporsi))
    st.write("Jumlah Sampel Verifikasi Faktualnya adalah", round(results))
elif(populasi == 0):
  st.write("Populasi Masih kosong")
else:
    st.write("Data gagal diproses")

def footer():
  st.write("test")