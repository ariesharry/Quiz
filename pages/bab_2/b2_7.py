import streamlit as st

soal_list = [
    # =========================
    # MULTIPLE CHOICE (10) - ADVANCED
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A company uses AI tools to analyze large volumes of customer transaction data and predict future buying behavior. This activity is best described as:",
        "pilihan": [
            "Marketing intelligence",
            "Predictive analytics",
            "Descriptive research",
            "Internal reporting",
            "Exploratory analysis"
        ],
        "jawaban_benar": "Predictive analytics"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which statement best explains the primary role of a Marketing Information System (MKIS)?",
        "pilihan": [
            "To replace human decision-making with automated systems",
            "To collect, analyze, and distribute relevant information for marketing decisions",
            "To store only internal company financial data",
            "To monitor employee performance",
            "To manage production processes"
        ],
        "jawaban_benar": "To collect, analyze, and distribute relevant information for marketing decisions"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A company conducts initial interviews to better understand an unclear marketing problem before designing a full study. This is an example of:",
        "pilihan": [
            "Descriptive research",
            "Causal research",
            "Exploratory research",
            "Experimental research",
            "Quantitative research"
        ],
        "jawaban_benar": "Exploratory research"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which research approach is most appropriate when a company wants to test whether a change in price will affect sales volume?",
        "pilihan": [
            "Observational research",
            "Survey research",
            "Exploratory research",
            "Causal research",
            "Ethnographic research"
        ],
        "jawaban_benar": "Causal research"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A researcher collects data by observing how customers behave in a retail store without interacting with them. This method is known as:",
        "pilihan": [
            "Survey research",
            "Experimental research",
            "Observational research",
            "Causal research",
            "Secondary data analysis"
        ],
        "jawaban_benar": "Observational research"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following best distinguishes primary data from secondary data?",
        "pilihan": [
            "Primary data is always cheaper than secondary data",
            "Secondary data is collected specifically for the current research problem",
            "Primary data is collected for a specific purpose, while secondary data already exists",
            "Secondary data is always more accurate than primary data",
            "Primary data cannot be quantitative"
        ],
        "jawaban_benar": "Primary data is collected for a specific purpose, while secondary data already exists"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A company uses online focus groups and social media discussions to understand customer opinions. This approach is best categorized as:",
        "pilihan": [
            "Quantitative research",
            "Causal research",
            "Qualitative research",
            "Experimental research",
            "Secondary data collection"
        ],
        "jawaban_benar": "Qualitative research"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which situation best represents a limitation of secondary data?",
        "pilihan": [
            "It is too expensive to collect",
            "It may not be relevant or up-to-date for the current problem",
            "It requires direct interaction with respondents",
            "It cannot be analyzed statistically",
            "It is always biased"
        ],
        "jawaban_benar": "It may not be relevant or up-to-date for the current problem"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "In sampling design, what is the key characteristic of probability sampling?",
        "pilihan": [
            "Only experts are selected",
            "Every population element has a known chance of selection",
            "Selection is based on convenience",
            "It does not require a sampling frame",
            "It is only used in qualitative research"
        ],
        "jawaban_benar": "Every population element has a known chance of selection"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A major ethical issue in modern marketing research, especially online, is:",
        "pilihan": [
            "High data processing speed",
            "Excessive use of qualitative methods",
            "Consumer privacy and data misuse",
            "Limited availability of technology",
            "Lack of marketing tools"
        ],
        "jawaban_benar": "Consumer privacy and data misuse"
    },

    # =========================
    # SHORT ANSWER (5) - ADVANCED
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "Large and complex datasets generated by modern technologies are referred to as ______ data.",
        "jawaban_benar": "big"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Research used to describe market characteristics or functions is called ______ research.",
        "jawaban_benar": "descriptive"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Data collected directly from respondents for a specific research purpose is known as ______ data.",
        "jawaban_benar": "primary"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The step in the marketing research process where data is analyzed and conclusions are presented is called ______ and reporting.",
        "jawaban_benar": "interpreting"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The use of online communities and social media to study consumer behavior is known as ______ research.",
        "jawaban_benar": "netnographic"
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