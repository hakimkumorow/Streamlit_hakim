import streamlit as st
import pandas as pd

# TITLE
st.title("📝 Aplikasi Absensi Karyawan")

# HEADER
st.header("Sistem Absensi Kerja Kantor")

# SUBHEADER
st.subheader("Data Kehadiran Karyawan")

# TEXT (PARAGRAF)
st.write(
    "Aplikasi ini digunakan untuk mencatat dan menampilkan data kehadiran karyawan di lingkungan kantor. "
    "Data absensi membantu pihak manajemen dan karyawan dalam memantau kedisiplinan serta tingkat kehadiran kerja. "
    "Informasi disajikan secara sederhana dan mudah dipahami."
)

# CAPTION
st.caption("Data absensi hanya untuk keperluan internal perusahaan")

# CODE (POTONGAN CODE)
st.subheader("Contoh Perhitungan Persentase Kehadiran")
st.code("""
hadir = 22
total_hari_kerja = 24
persentase = (hadir / total_hari_kerja) * 100
print(persentase)
""")

# DATA DISPLAY - TABEL / DATAFRAME
st.subheader("Tabel Absensi Karyawan")

data = {
    "Nama Karyawan": ["Andi", "Hakim", "Aqsho", "Bang Il"],
    "Hadir": [22, 24, 20, 23],
    "Izin": [1, 0, 2, 1],
    "Alpha": [1, 0, 2, 0]
}

df = pd.DataFrame(data)
st.dataframe(df)

# DATA DISPLAY - CHART
st.subheader("Grafik Jumlah Kehadiran Karyawan")

st.bar_chart(df.set_index("Nama Karyawan")["Hadir"])
