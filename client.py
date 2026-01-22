import streamlit as st
import requests

st.title("🍽️ **RESTORAN ONLINE**")
st.markdown("---")

try:
    menu = requests.get("http://localhost:5000/api/menu").json()
    st.success("✅ Server Terhubung!")
except:
    st.error("❌ Jalankan `python server.py` DULU!")
    st.stop()

st.sidebar.header("🛒 **PESANAN**")
pesanan = st.session_state.get("pesanan", [])

# Menu
st.subheader("**MENU RESTAURAN**")
for item in menu:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**{item['nama']}**")
        st.caption(f"Rp {item['harga']:,}")
    with col2:
        qty = st.number_input("Qty", 0, 10, 0, key=f"qty{item['id']}")
        if qty > 0:
            pesanan.append({"id": item['id'], "jumlah": qty})
            st.session_state.pesanan = pesanan

if pesanan:
    st.sidebar.write("**📋 Pesanan:**")
    total = 0
    for item in pesanan:
        nama = next((m['nama'] for m in menu if m['id'] == item['id']), '?')
        harga = next((m['harga'] for m in menu if m['id'] == item['id']), 0)
        subtotal = harga * item['jumlah']
        total += subtotal
        st.sidebar.write(f"{nama} x{item['jumlah']} = Rp{subtotal:,}")
    
    st.sidebar.markdown(f"**💰 TOTAL: Rp {total:,}**")
    if st.sidebar.button("✅ Pesan"):
        st.balloons()
        st.session_state.pesanan = []
        st.rerun()
else:
    st.sidebar.info("Keranjang kosong")
