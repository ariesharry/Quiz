import streamlit as st

soal_list = [
    # =========================
    # MULTIPLE CHOICE (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "What is the marketing environment?",
        "pilihan": [
            "Only the internal departments within a company",
            "All external and internal factors that affect a company's ability to build relationships with customers",
            "The financial system used by the company",
            "The advertising strategy used by marketers",
            "Only the competitors in the market"
        ],
        "jawaban_benar": "All external and internal factors that affect a company's ability to build relationships with customers"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is part of the microenvironment?",
        "pilihan": [
            "Technological change",
            "Suppliers",
            "Demographic trends",
            "Cultural values",
            "Economic conditions"
        ],
        "jawaban_benar": "Suppliers"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which factor belongs to the macroenvironment?",
        "pilihan": [
            "Marketing intermediaries",
            "Customers",
            "Suppliers",
            "Demographic changes",
            "Company departments"
        ],
        "jawaban_benar": "Demographic changes"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Marketing intermediaries help companies by:",
        "pilihan": [
            "Producing raw materials",
            "Promoting, selling, and distributing products to buyers",
            "Regulating marketing laws",
            "Replacing competitors in the market",
            "Determining cultural values"
        ],
        "jawaban_benar": "Promoting, selling, and distributing products to buyers"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is NOT a type of public in the marketing microenvironment?",
        "pilihan": [
            "Media publics",
            "Government publics",
            "Financial publics",
            "Technological publics",
            "Local publics"
        ],
        "jawaban_benar": "Technological publics"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Changes in population size, age distribution, and geographic shifts belong to the:",
        "pilihan": [
            "Economic environment",
            "Technological environment",
            "Demographic environment",
            "Political environment",
            "Natural environment"
        ],
        "jawaban_benar": "Demographic environment"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which environment includes innovation, digital transformation, and research development?",
        "pilihan": [
            "Technological environment",
            "Natural environment",
            "Cultural environment",
            "Economic environment",
            "Political environment"
        ],
        "jawaban_benar": "Technological environment"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Government regulations and consumer protection laws are part of the:",
        "pilihan": [
            "Natural environment",
            "Technological environment",
            "Political and legal environment",
            "Cultural environment",
            "Demographic environment"
        ],
        "jawaban_benar": "Political and legal environment"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which type of market involves organizations that buy goods and services for further processing or production?",
        "pilihan": [
            "Consumer market",
            "Business market",
            "Government market",
            "Reseller market",
            "International market"
        ],
        "jawaban_benar": "Business market"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Identifying new market trends and emerging customer needs is part of:",
        "pilihan": [
            "Environmental analysis",
            "Production management",
            "Operational control",
            "Human resource planning",
            "Financial auditing"
        ],
        "jawaban_benar": "Environmental analysis"
    },

    # =========================
    # SHORT ANSWER (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "The marketing environment consists of two main components: microenvironment and ______ environment.",
        "jawaban_benar": "macro"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Organizations that help promote, sell, and distribute products to buyers are called marketing ______.",
        "jawaban_benar": "intermediaries"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Changes in income levels and purchasing power belong to the ______ environment.",
        "jawaban_benar": "economic"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The environment that includes innovation and technological advancement is the ______ environment.",
        "jawaban_benar": "technological"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Groups that have an interest or impact on a company's ability to achieve its objectives are called ______.",
        "jawaban_benar": "publics"
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