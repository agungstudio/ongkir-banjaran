import streamlit as st
import pandas as pd

st.title("Cek Deploy Berhasil!")
st.write("Halo! Jika kamu melihat tulisan ini, berarti aplikasi Streamlit sudah online.")

st.info("Sekarang kita tinggal update kodenya pelan-pelan.")

# Test Data Frame
df = pd.DataFrame({
    'Barang': ['TV', 'Kulkas', 'AC'],
    'Harga': [100, 200, 300]
})
st.dataframe(df)
