import streamlit as st

soal_list = [
    # =========================
    # PILIHAN GANDA (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The Treaty of Waitangi was signed in which year?",
        "pilihan": [
            "1835",
            "1840",
            "1850",
            "1865",
            "1900"
        ],
        "jawaban_benar": "1840"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The Treaty of Waitangi was first signed at:",
        "pilihan": [
            "Auckland",
            "Wellington",
            "Christchurch",
            "Waitangi",
            "Dunedin"
        ],
        "jawaban_benar": "Waitangi"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which two groups originally signed the Treaty of Waitangi?",
        "pilihan": [
            "British settlers and Australian leaders",
            "The British Crown and Māori chiefs",
            "The New Zealand Parliament and Māori tribes",
            "Missionaries and traders",
            "Local governors and farmers"
        ],
        "jawaban_benar": "The British Crown and Māori chiefs"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which issue created differences in interpretation of the Treaty?",
        "pilihan": [
            "The number of signatories",
            "The location of signing",
            "The existence of two different language versions",
            "The involvement of traders",
            "The date of signing"
        ],
        "jawaban_benar": "The existence of two different language versions"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A Treaty breach refers to:",
        "pilihan": [
            "The signing of the treaty",
            "Failure to honour the promises of the treaty",
            "The translation of the treaty",
            "A new treaty agreement",
            "A government election"
        ],
        "jawaban_benar": "Failure to honour the promises of the treaty"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which organisation was created to investigate Treaty claims?",
        "pilihan": [
            "Supreme Court",
            "New Zealand Council",
            "Waitangi Tribunal",
            "Treaty Commission",
            "Parliamentary Review Board"
        ],
        "jawaban_benar": "Waitangi Tribunal"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The Waitangi Tribunal was established under which legislation?",
        "pilihan": [
            "New Zealand Governance Act",
            "Treaty Protection Act",
            "Treaty of Waitangi Act 1975",
            "Māori Development Act",
            "Land Settlement Act"
        ],
        "jawaban_benar": "Treaty of Waitangi Act 1975"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is a common form of Treaty settlement?",
        "pilihan": [
            "Financial compensation",
            "Increased taxation",
            "Military support",
            "Foreign investment",
            "Trade agreements"
        ],
        "jawaban_benar": "Financial compensation"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "In modern management in New Zealand, the Treaty principles include:",
        "pilihan": [
            "Leadership, strategy, innovation",
            "Planning, organising, controlling",
            "Partnership, participation, protection",
            "Authority, discipline, unity",
            "Efficiency, productivity, profit"
        ],
        "jawaban_benar": "Partnership, participation, protection"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The principle of partnership in the Treaty context means:",
        "pilihan": [
            "Māori control all government decisions",
            "The Crown and Māori work together in decision-making",
            "Only government makes decisions",
            "Businesses manage Māori resources",
            "Foreign organisations manage resources"
        ],
        "jawaban_benar": "The Crown and Māori work together in decision-making"
    },

    # =========================
    # ISIAN SINGKAT (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "The Treaty of Waitangi was signed in the year ________.",
        "jawaban_benar": "1840"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The tribunal that investigates Treaty claims is called the ________ Tribunal.",
        "jawaban_benar": "Waitangi"
    },
    {
        "tipe": "isian",
        "pertanyaan": "One of the three Treaty principles is partnership, participation, and ________.",
        "jawaban_benar": "protection"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The Treaty settlement process aims to address historical ________ of the Treaty.",
        "jawaban_benar": "breaches"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The Māori version of the Treaty is called ________ Tiriti o Waitangi.",
        "jawaban_benar": "Te"
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