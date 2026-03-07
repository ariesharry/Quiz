import streamlit as st

soal_list = [
    # =========================
    # MULTIPLE CHOICE (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Strategic planning in marketing refers to:",
        "pilihan": [
            "Developing short-term promotional campaigns",
            "Maintaining a strategic fit between company goals, capabilities, and marketing opportunities",
            "Maximizing sales through aggressive advertising",
            "Focusing only on internal company efficiency",
            "Eliminating competition in the marketplace"
        ],
        "jawaban_benar": "Maintaining a strategic fit between company goals, capabilities, and marketing opportunities"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A mission statement should primarily:",
        "pilihan": [
            "Focus on increasing short-term profits",
            "Describe the company’s purpose and customer needs it aims to satisfy",
            "List all operational procedures",
            "Describe employee responsibilities",
            "Focus only on production efficiency"
        ],
        "jawaban_benar": "Describe the company’s purpose and customer needs it aims to satisfy"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which unit represents a key business area within a company that can be planned independently?",
        "pilihan": [
            "Market segment",
            "Strategic Business Unit",
            "Distribution channel",
            "Marketing department",
            "Customer cluster"
        ],
        "jawaban_benar": "Strategic Business Unit"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "In the BCG growth-share matrix, a business unit with high market share but low market growth is classified as:",
        "pilihan": [
            "Star",
            "Question Mark",
            "Dog",
            "Cash Cow",
            "Pioneer"
        ],
        "jawaban_benar": "Cash Cow"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which strategy in the Ansoff Matrix focuses on selling existing products to new markets?",
        "pilihan": [
            "Market penetration",
            "Market development",
            "Product development",
            "Diversification",
            "Market repositioning"
        ],
        "jawaban_benar": "Market development"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The value chain refers to:",
        "pilihan": [
            "The sequence of customer purchases over time",
            "A network of retail outlets",
            "Internal departments that perform value-creating activities",
            "A pricing strategy used by marketers",
            "A system for monitoring financial performance"
        ],
        "jawaban_benar": "Internal departments that perform value-creating activities"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Market targeting is the process of:",
        "pilihan": [
            "Dividing the market into different groups",
            "Selecting the most attractive market segments to serve",
            "Developing new products for existing markets",
            "Positioning a brand in the consumer’s mind",
            "Designing promotional strategies"
        ],
        "jawaban_benar": "Selecting the most attractive market segments to serve"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which element is part of the extended marketing mix?",
        "pilihan": [
            "People",
            "Positioning",
            "Segmentation",
            "Targeting",
            "Brand equity"
        ],
        "jawaban_benar": "People"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which stage of marketing management involves converting marketing plans into actions?",
        "pilihan": [
            "Analysis",
            "Planning",
            "Implementation",
            "Control",
            "Forecasting"
        ],
        "jawaban_benar": "Implementation"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Marketing control primarily aims to:",
        "pilihan": [
            "Increase advertising frequency",
            "Measure and evaluate marketing performance and take corrective action",
            "Eliminate marketing risks",
            "Reduce operational costs",
            "Replace marketing managers"
        ],
        "jawaban_benar": "Measure and evaluate marketing performance and take corrective action"
    },

    # =========================
    # SHORT ANSWER (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "The collection of businesses and products that make up a company is called a business ________.",
        "jawaban_benar": "portfolio"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The BCG matrix evaluates business units using market growth rate and relative market ________.",
        "jawaban_benar": "share"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The process of dividing a market into distinct groups of buyers is called market ________.",
        "jawaban_benar": "segmentation"
    },
    {
        "tipe": "isian",
        "pertanyaan": "A SWOT analysis evaluates strengths, weaknesses, opportunities, and ________.",
        "jawaban_benar": "threats"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Return on Marketing Investment is commonly abbreviated as marketing ________.",
        "jawaban_benar": "ROI"
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