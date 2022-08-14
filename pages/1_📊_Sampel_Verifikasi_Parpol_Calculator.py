from multiprocessing import Value
from turtle import onkeypress
import streamlit as st
import pickle

st.set_page_config(page_title="Verifikasi Parpol Calculator", page_icon="📊")

st.markdown("# Verifikasi Parpol Calculator")

class resulting:
  status = ""
  sampel = ""
  interval = ""

def hitungSampel(populate):
  chikuadrat = 3.84
  galatpendugaan = 0.05
  proporsi = 0.5
  result = resulting()
  if populate > 10:
    rsampel = (chikuadrat * populate * proporsi * (1-proporsi)) / ((populate - 1) * (galatpendugaan**2) + chikuadrat * proporsi *(1-proporsi))
    rinterval = populate / rsampel
    result.status = "sucsess"
    result.sampel = rsampel
    result.interval = rinterval
  else:
    result.status = "failed"
    result.sampel = 0
    result.interval = 0
  return result


populasi = ""
populasi = st.number_input("Masukan Populasi",format="%.0f")
hitunglah = st.button("Hitung Sampel", on_click=hitungSampel, args=[populasi])

if hitunglah or (0 != populasi):
  hasil = hitungSampel(populasi)
  st.write("Jumlah Sampel Verifikasi Faktual: ", round(hasil.sampel))
  st.write("dengan interval: ", round(hasil.interval))
