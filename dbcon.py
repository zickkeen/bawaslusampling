import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
import streamlit as st

URI_SQLITE_DB = "db.sqlite3"

def koneksi():
  return sqlite3.connect(URI_SQLITE_DB)


def insertSqlite(dataQuery):
  conn = koneksi()
  conn.execute(f"INSERT INTO dataDPB (urut,nkk,nik,nama,tmpLahir,tglLahir,status,gender,alamat,rt,rw,disabilitas,desa) VALUES (" + dataQuery + ")")
  conn.commit()

def showData(tableName):
  conn = koneksi()
  return conn.execute(f"SELECT * FROM {tableName}")

def get_data(tableName):
  conn = koneksi()
  df = pd.read_sql("SELECT * FROM {tableName}", con=conn)
  return df

