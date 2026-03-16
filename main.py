import streamlit as st

st.set_page_config(page_title="E-Modul Interaktif", layout="wide", initial_sidebar_state="expanded")

# =========================
# DATA SEMUA HALAMAN (URUTAN SESUAI TAMPILAN)
# =========================
# Format: (file_path, judul_tampilan, nama_bab)
halaman_data = [
    # Management
    ("pages/bab_1/b1_1.py", "Latihan 1 - Fundamental of Management", "Management"),
    ("pages/bab_1/b1_2.py", "Latihan 2 - Leadership", "Management"),
    ("pages/bab_1/b1_3.py", "Latihan 3 - Function and Skills", "Management"),
    ("pages/bab_1/b1_4.py", "Latihan 4 - Motivation", "Management"),
    ("pages/bab_1/b1_5.py", "Latihan 5 - Week 3", "Management"),
    ("pages/bab_1/b1_6.py", "Latihan 6 - Week 4", "Management"),
    ("pages/bab_1/b1_7.py", "Latihan 7 - Week 4", "Management"),
    # Marketing
    ("pages/bab_2/b2_1.py", "Latihan 1", "Marketing"),
    ("pages/bab_2/b2_2.py", "Latihan 2", "Marketing"),
    # Management lagi
    
    # Marketing lagi
    ("pages/bab_2/b2_3.py", "Latihan 3", "Marketing"),
    ("pages/bab_2/b2_4.py", "Latihan 4", "Marketing"),
    ("pages/bab_2/b2_5.py", "Latihan 5", "Marketing"),
    ("pages/bab_2/b2_6.py", "Latihan 6", "Marketing"),
    # Management terakhir
    
]

# =========================
# GENERATE OBJEK st.Page DAN KELOMPOKKAN PER BAB
# =========================
pages_by_bab = {}       # dict: {nama_bab: list_of_page_objects}
all_materi_pages = []   # list urut semua halaman (untuk st.navigation)

for file, title, bab in halaman_data:
    page_obj = st.Page(file, title=title)
    all_materi_pages.append(page_obj)
    
    if bab not in pages_by_bab:
        pages_by_bab[bab] = []
    pages_by_bab[bab].append(page_obj)

# =========================
# HALAMAN KHUSUS (COVER)
# =========================
cover = st.Page("pages/cover.py", title="Home", icon=":material/home:")

# =========================
# NAVIGATION (HIDDEN)
# =========================
contents = {
    "": [cover],
    "_materi": all_materi_pages,   # semua halaman materi dalam satu section
}
pg = st.navigation(contents, position="hidden")

# =========================
# SIDEBAR CUSTOM
# =========================
with st.sidebar:
    st.page_link(cover, label="Home", icon=":material/home:")
    st.divider()
    st.markdown("### Table of Contents")

    # Tampilkan expander per bab (urutan bab sesuai kemunculan pertama di data)
    bab_list = list(pages_by_bab.keys())  # ["Management", "Marketing"] (urutan sesuai data)
    for i, bab in enumerate(bab_list):
        with st.expander(bab, expanded=(i == 0)):   # expanded hanya bab pertama
            for page in pages_by_bab[bab]:
                st.page_link(page)

# =========================
# RUN PAGE
# =========================
pg.run()