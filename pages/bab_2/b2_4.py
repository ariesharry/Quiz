import streamlit as st

soal_list = [
    # =========================
    # MULTIPLE CHOICE (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which statement best describes the relationship between corporate strategy and marketing strategy?",
        "pilihan": [
            "Marketing strategy determines corporate financial policy",
            "Corporate strategy defines overall business direction while marketing strategy supports it by creating customer value",
            "Marketing strategy replaces corporate strategy in competitive markets",
            "Corporate strategy focuses only on operations while marketing handles profits",
            "Both strategies operate independently from each other"
        ],
        "jawaban_benar": "Corporate strategy defines overall business direction while marketing strategy supports it by creating customer value"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A company defines its mission as 'to provide affordable and reliable transportation solutions for urban commuters.' This mission is considered effective primarily because it:",
        "pilihan": [
            "Focuses strictly on increasing market share",
            "Is defined in terms of customer needs rather than specific products",
            "Emphasizes maximizing shareholder value",
            "Lists operational activities clearly",
            "Targets only a single market segment"
        ],
        "jawaban_benar": "Is defined in terms of customer needs rather than specific products"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "In the BCG growth-share matrix, which strategic recommendation is most appropriate for a 'Question Mark' business unit?",
        "pilihan": [
            "Harvest the business and reduce investment",
            "Invest heavily to increase market share or consider divesting",
            "Maintain current investment to sustain profits",
            "Shift the unit into unrelated markets",
            "Convert it immediately into a diversification strategy"
        ],
        "jawaban_benar": "Invest heavily to increase market share or consider divesting"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A company introduces a new version of an existing smartphone with improved features for its current customer base. According to the Ansoff Matrix, this strategy represents:",
        "pilihan": [
            "Market penetration",
            "Market development",
            "Product development",
            "Diversification",
            "Vertical integration"
        ],
        "jawaban_benar": "Product development"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Why do many companies move away from strict portfolio matrix approaches such as the BCG matrix?",
        "pilihan": [
            "They cannot measure market share accurately",
            "Matrix models ignore all financial data",
            "They may oversimplify complex strategic situations",
            "They are only useful for small companies",
            "They require excessive marketing budgets"
        ],
        "jawaban_benar": "They may oversimplify complex strategic situations"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following best explains the concept of a value delivery network?",
        "pilihan": [
            "A company’s internal marketing department structure",
            "The network of suppliers, distributors, and partners working together to deliver value to customers",
            "A digital platform used for marketing analytics",
            "A distribution channel that focuses only on logistics",
            "A system used exclusively for customer feedback"
        ],
        "jawaban_benar": "The network of suppliers, distributors, and partners working together to deliver value to customers"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A firm divides the market into segments and then develops a clear brand image in the minds of the chosen segment relative to competitors. This final step is known as:",
        "pilihan": [
            "Differentiation",
            "Segmentation",
            "Targeting",
            "Positioning",
            "Brand extension"
        ],
        "jawaban_benar": "Positioning"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which marketing management function focuses on assessing the company’s internal and external environment before strategy development?",
        "pilihan": [
            "Marketing control",
            "Marketing analysis",
            "Marketing implementation",
            "Marketing communication",
            "Marketing budgeting"
        ],
        "jawaban_benar": "Marketing analysis"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "In a marketing plan, which section typically outlines what actions will be taken, when they will occur, who is responsible, and the associated costs?",
        "pilihan": [
            "Executive summary",
            "Current marketing situation",
            "Marketing strategy",
            "Action programs",
            "Controls"
        ],
        "jawaban_benar": "Action programs"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A company compares its expected marketing performance with actual results and adjusts strategies accordingly. This activity is part of:",
        "pilihan": [
            "Strategic segmentation",
            "Marketing implementation",
            "Marketing control",
            "Marketing differentiation",
            "Marketing forecasting"
        ],
        "jawaban_benar": "Marketing control"
    },

    # =========================
    # SHORT ANSWER (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "Strategic Business Units are commonly abbreviated as ________.",
        "jawaban_benar": "SBU"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The portfolio planning tool that evaluates market growth and market share is known as the ________ matrix.",
        "jawaban_benar": "BCG"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The network consisting of the company, suppliers, distributors, and customers working together is called the value delivery ________.",
        "jawaban_benar": "network"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Marketing implementation is the process of turning marketing ________ into actions.",
        "jawaban_benar": "plans"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Customer lifetime value is commonly abbreviated as ________.",
        "jawaban_benar": "CLV"
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