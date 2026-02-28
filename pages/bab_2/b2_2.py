import streamlit as st

soal_list = [
    # =========================
    # MULTIPLE CHOICE (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which statement best reflects the marketing concept?",
        "pilihan": [
            "Focusing on production efficiency above all else",
            "Aggressive selling regardless of customer needs",
            "Satisfying customer needs better than competitors",
            "Maximising short-term sales volume",
            "Reducing operational costs continuously"
        ],
        "jawaban_benar": "Satisfying customer needs better than competitors"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "In marketing, value is best described as:",
        "pilihan": [
            "The price paid by the customer",
            "The quality level of a product",
            "The customer’s perceived benefits relative to costs",
            "The company’s profit margin",
            "The brand reputation alone"
        ],
        "jawaban_benar": "The customer’s perceived benefits relative to costs"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is an example of a market offering?",
        "pilihan": [
            "Only tangible products",
            "Only services",
            "Goods, services, experiences, and ideas",
            "Advertising campaigns only",
            "Distribution channels only"
        ],
        "jawaban_benar": "Goods, services, experiences, and ideas"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Demand in marketing occurs when:",
        "pilihan": [
            "A customer wants a product",
            "A customer needs a product",
            "A want is supported by buying power",
            "A product is heavily promoted",
            "A product is widely available"
        ],
        "jawaban_benar": "A want is supported by buying power"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which type of utility is created by making a product available at convenient locations?",
        "pilihan": [
            "Form utility",
            "Time utility",
            "Place utility",
            "Possession utility",
            "Image utility"
        ],
        "jawaban_benar": "Place utility"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Marketing myopia refers to a firm’s tendency to:",
        "pilihan": [
            "Overestimate customer loyalty",
            "Focus on customer benefits",
            "Define its business too narrowly",
            "Invest too much in promotion",
            "Ignore competition"
        ],
        "jawaban_benar": "Define its business too narrowly"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which marketing orientation considers both customer satisfaction and societal well-being?",
        "pilihan": [
            "Production orientation",
            "Product orientation",
            "Sales orientation",
            "Marketing orientation",
            "Societal marketing orientation"
        ],
        "jawaban_benar": "Societal marketing orientation"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which stage of the marketing process focuses on selecting customers to serve?",
        "pilihan": [
            "Market research",
            "Market segmentation and targeting",
            "Marketing mix development",
            "Relationship building",
            "Value capture"
        ],
        "jawaban_benar": "Market segmentation and targeting"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is NOT part of the extended marketing mix?",
        "pilihan": [
            "People",
            "Process",
            "Physical evidence",
            "Positioning",
            "Product"
        ],
        "jawaban_benar": "Positioning"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The ultimate objective of building strong customer relationships is to:",
        "pilihan": [
            "Increase advertising reach",
            "Reduce marketing costs",
            "Capture customer lifetime value",
            "Improve internal efficiency",
            "Expand product variety"
        ],
        "jawaban_benar": "Capture customer lifetime value"
    },

    # =========================
    # SHORT ANSWER (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "Marketing focuses on delivering value to customers at a ________.",
        "jawaban_benar": "profit"
    },
    {
        "tipe": "isian",
        "pertanyaan": "A product, service, or idea offered to a market is known as a market ________.",
        "jawaban_benar": "offering"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Customer value is created when perceived benefits exceed perceived ________.",
        "jawaban_benar": "costs"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The process of dividing a market into distinct customer groups is called market ________.",
        "jawaban_benar": "segmentation"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Marketing management involves analysis, planning, implementation, and ________.",
        "jawaban_benar": "control"
    }
]
# Inisialisasi session state untuk menyimpan status koreksi
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

# Tampilkan setiap soal
for i, soal in enumerate(soal_list):
    with st.container():
        st.markdown(f"**_Question {i+1}_**")
        st.markdown(f"{soal['pertanyaan']}")
        
        # Input berdasarkan tipe soal
        if soal["tipe"] == "pilihan_ganda":
            jawaban_user = st.radio(
                "Pilih jawaban:",
                options=soal["pilihan"],
                key=f"mc_{i}",
                index=None,  # tidak ada default
                label_visibility="collapsed"  # menyembunyikan label "Pilih jawaban" agar lebih ringkas
            )
        else:  # isian
            jawaban_user = st.text_input(
                "Masukkan jawaban:",
                key=f"sa_{i}",
                label_visibility="collapsed"
            ).strip()
        
        # Jika sudah dicek, tampilkan feedback
        if st.session_state.cek_dilakukan:
            # Ambil jawaban user dari session state
            if soal["tipe"] == "pilihan_ganda":
                jawaban = st.session_state.get(f"mc_{i}")
            else:
                jawaban = st.session_state.get(f"sa_{i}", "").strip()
            
            # Pastikan jawaban tidak None untuk pilihan ganda
            if jawaban is None:
                jawaban = ""
            
            # Bandingkan dengan jawaban benar (case insensitive untuk isian)
            if soal["tipe"] == "isian":
                benar = jawaban.lower() == soal["jawaban_benar"].lower()
            else:
                benar = jawaban == soal["jawaban_benar"]
            
            if benar:
                st.success("✅ Jawaban Anda benar!")
            else:
                st.error(f"❌ Jawaban Anda salah. Jawaban yang benar: {soal['jawaban_benar']}")
        
        st.markdown("---")

# Tombol untuk mengecek jawaban
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔍 Cek Jawaban", use_container_width=True):
        st.session_state.cek_dilakukan = True
        st.rerun()

# Tombol untuk mengulang (reset)
if st.session_state.cek_dilakukan:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Coba Lagi", use_container_width=True):
            # Hapus semua jawaban dari session state
            for key in list(st.session_state.keys()):
                if key.startswith("mc_") or key.startswith("sa_"):
                    del st.session_state[key]
            st.session_state.cek_dilakukan = False
            st.rerun()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Selamat belajar! 🌟</p>", unsafe_allow_html=True)