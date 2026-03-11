import streamlit as st

soal_list = [
    # =========================
    # MULTIPLE CHOICE (10) - ADVANCED
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A smartphone company monitors changes in consumer lifestyle, environmental awareness, and social values that influence product design. These factors are primarily part of the:",
        "pilihan": [
            "Demographic environment",
            "Technological environment",
            "Cultural and social environment",
            "Economic environment",
            "Political environment"
        ],
        "jawaban_benar": "Cultural and social environment"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A disruption in global semiconductor supply causes a company to delay product launches. This situation represents which type of marketing environment influence?",
        "pilihan": [
            "Microenvironment influence from suppliers",
            "Macroenvironment influence from political regulations",
            "Macroenvironment influence from demographic shifts",
            "Internal company operational failure",
            "Consumer market instability"
        ],
        "jawaban_benar": "Microenvironment influence from suppliers"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which scenario best illustrates a company responding strategically to the technological environment?",
        "pilihan": [
            "Reducing prices to compete with rivals",
            "Launching a mobile application to enhance customer experience",
            "Changing distribution partners",
            "Hiring additional sales staff",
            "Expanding into international markets"
        ],
        "jawaban_benar": "Launching a mobile application to enhance customer experience"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A company analyzes inflation trends, unemployment rates, and household income before launching a premium product. This analysis focuses on the:",
        "pilihan": [
            "Demographic environment",
            "Economic environment",
            "Cultural environment",
            "Technological environment",
            "Competitive environment"
        ],
        "jawaban_benar": "Economic environment"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "When a government introduces stricter data privacy regulations affecting digital marketing campaigns, the company is experiencing changes in the:",
        "pilihan": [
            "Technological environment",
            "Political and legal environment",
            "Natural environment",
            "Economic environment",
            "Cultural environment"
        ],
        "jawaban_benar": "Political and legal environment"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following situations represents a macroenvironmental threat for most companies?",
        "pilihan": [
            "A supplier increases raw material prices",
            "A competitor launches a similar product",
            "A sudden global recession reduces purchasing power",
            "A marketing agency changes its advertising strategy",
            "A retailer stops selling a specific brand"
        ],
        "jawaban_benar": "A sudden global recession reduces purchasing power"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A marketing manager collects data from social media trends, competitor campaigns, and industry reports to anticipate market changes. This activity is best described as:",
        "pilihan": [
            "Marketing intelligence",
            "Production analysis",
            "Operational management",
            "Financial forecasting",
            "Human resource planning"
        ],
        "jawaban_benar": "Marketing intelligence"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which example best represents an opportunity created by demographic changes?",
        "pilihan": [
            "Launching financial services for an aging population",
            "Reducing product packaging costs",
            "Increasing warehouse capacity",
            "Hiring additional engineers",
            "Reducing advertising spending"
        ],
        "jawaban_benar": "Launching financial services for an aging population"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A company identifies that younger consumers prefer sustainable packaging and environmentally friendly products. This insight mainly reflects influence from the:",
        "pilihan": [
            "Natural environment only",
            "Cultural and social environment",
            "Economic environment",
            "Political environment",
            "Supplier environment"
        ],
        "jawaban_benar": "Cultural and social environment"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which statement best explains the relationship between the microenvironment and macroenvironment?",
        "pilihan": [
            "The macroenvironment directly controls the internal company structure",
            "The microenvironment operates independently from societal forces",
            "The macroenvironment shapes conditions that influence the microenvironment",
            "The microenvironment replaces macroenvironmental influences",
            "Both environments focus only on competitors"
        ],
        "jawaban_benar": "The macroenvironment shapes conditions that influence the microenvironment"
    },

    # =========================
    # SHORT ANSWER (5) - ADVANCED
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "The process of collecting and analyzing information about competitors, market trends, and environmental changes is called marketing ______.",
        "jawaban_benar": "intelligence"
    },
    {
        "tipe": "isian",
        "pertanyaan": "A decline in consumer purchasing power due to inflation reflects changes in the ______ environment.",
        "jawaban_benar": "economic"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Companies that buy goods and services to resell them for profit operate in the ______ market.",
        "jawaban_benar": "reseller"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Large societal forces that affect the microenvironment are collectively known as the ______ environment.",
        "jawaban_benar": "macro"
    },
    {
        "tipe": "isian",
        "pertanyaan": "When a company develops eco-friendly products in response to environmental concerns, it is responding to the ______ environment.",
        "jawaban_benar": "natural"
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