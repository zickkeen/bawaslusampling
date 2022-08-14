import streamlit as st
import dbcon as db

st.set_page_config(page_title="Sampel Data Excel", page_icon="📊")

st.markdown("# Sampel Data Excel")

# st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)

modeCari = st.selectbox('Pilih Mode',('NIK', 'NAMA'))
if modeCari is not None and modeCari == "NIK":
  nik = st.text_input("Masukkan NIK")
  if nik is not None and nik != "":
    conn = db.koneksi()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM dataDPB where NIK='{nik}'")
    hasil = cur.fetchall()
    if len(hasil) > 0:
      st.write("Data ditemukan atas nama: ", hasil[0][3])
    else:
      st.write("Data Tidak Ditemukan")
if modeCari is not None and modeCari == "NAMA":
  listKec = ["AMPELGADING","BANTUR","BULULAWANG","DAMPIT","DAU","DONOMULYO","GEDANGAN","GONDANGLEGI","JABUNG","KALIPARE","KARANGPLOSO","KASEMBON","KEPANJEN","KROMENGAN","LAWANG","NGAJUM","NGANTANG","PAGAK","PAGELARAN","PAKIS","PAKISAJI","PONCOKUSUMO","PUJON","SINGOSARI","SUMBERMANJING WETAN","SUMBERPUCUNG","TAJINAN","TIRTOYUDO","TUMPANG","TUREN","WAGIR","WAJAK","WONOSARI"]
  kec = st.selectbox('Kecamatan',listKec,index=2)
  nama = st.text_input("NAMA")
  if nama is not None and nama != "":
    conn = db.koneksi()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM dataDPB where NAMA_PEMILIH='%{nama}%' AND KECAMATAN='{kec}'")
    hasil = cur.fetchall()
    if len(hasil) > 0:
      st.write("Data ditemukan:")
      for row in hasil:
        st.write("- " + row[3])
    else:
      st.write("Data Tidak Ditemukan")