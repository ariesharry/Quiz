import streamlit as st

soal_list = [
    # =========================
    # MULTIPLE CHOICE (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Marketing is best described as:",
        "pilihan": [
            "Selling products at the lowest price",
            "Advertising products aggressively",
            "Creating value for customers and capturing value in return",
            "Managing company finances",
            "Producing goods efficiently"
        ],
        "jawaban_benar": "Creating value for customers and capturing value in return"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "According to marketing theory, which concept is central to all marketing activities?",
        "pilihan": [
            "Profit maximisation",
            "Customer value",
            "Product features",
            "Sales volume",
            "Advertising budget"
        ],
        "jawaban_benar": "Customer value"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A marketing exchange requires:",
        "pilihan": [
            "One party and one product",
            "At least two parties, each with something of value",
            "Only money as currency",
            "A physical product",
            "Government regulation"
        ],
        "jawaban_benar": "At least two parties, each with something of value"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A need is best defined as:",
        "pilihan": [
            "A desire for luxury products",
            "A state of felt deprivation",
            "A demand supported by buying power",
            "A marketing-created desire",
            "A personal preference"
        ],
        "jawaban_benar": "A state of felt deprivation"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following best represents a product in marketing?",
        "pilihan": [
            "Only physical goods",
            "Goods and services only",
            "Anything that can be offered to satisfy a need or want",
            "Only branded items",
            "Only paid offerings"
        ],
        "jawaban_benar": "Anything that can be offered to satisfy a need or want"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Customer value is determined by:",
        "pilihan": [
            "Price alone",
            "Product quality alone",
            "Benefits minus costs",
            "Company profit",
            "Advertising effectiveness"
        ],
        "jawaban_benar": "Benefits minus costs"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is NOT a type of customer cost?",
        "pilihan": [
            "Monetary cost",
            "Time cost",
            "Energy cost",
            "Psychological cost",
            "Brand loyalty"
        ],
        "jawaban_benar": "Brand loyalty"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Marketing myopia occurs when firms focus too much on:",
        "pilihan": [
            "Customer needs",
            "Customer value",
            "The benefits they provide",
            "Their products rather than customer needs",
            "Long-term relationships"
        ],
        "jawaban_benar": "Their products rather than customer needs"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which marketing orientation emphasises satisfying customer needs better than competitors?",
        "pilihan": [
            "Production orientation",
            "Product orientation",
            "Sales orientation",
            "Marketing orientation",
            "Selling orientation"
        ],
        "jawaban_benar": "Marketing orientation"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The primary goal of marketing management is to:",
        "pilihan": [
            "Increase production efficiency",
            "Maximise advertising exposure",
            "Create profitable customer relationships",
            "Reduce operational costs",
            "Control employee performance"
        ],
        "jawaban_benar": "Create profitable customer relationships"
    },

    # =========================
    # SHORT ANSWER (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "Marketing is the process of creating, communicating, and delivering ________ to customers.",
        "jawaban_benar": "value"
    },
    {
        "tipe": "isian",
        "pertanyaan": "A want becomes a demand when it is supported by buying ________.",
        "jawaban_benar": "power"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Customer satisfaction is strongly related to perceived customer ________.",
        "jawaban_benar": "value"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Form, place, time, possession, and image utility are types of ________.",
        "jawaban_benar": "utility"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Marketing management consists of analysis, planning, implementation, and ________.",
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