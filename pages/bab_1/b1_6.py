import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which statement best describes the concept of planning in management?",
    "pilihan": [
        "Allocating resources to departments without setting objectives",
        "Selecting goals and determining actions to achieve them",
        "Monitoring employee performance and correcting errors",
        "Motivating employees to complete assigned tasks",
        "Organizing people into departments and teams"
    ],
    "jawaban_benar": "Selecting goals and determining actions to achieve them"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Why is planning considered the most fundamental management function?",
    "pilihan": [
        "Because it directly generates company revenue",
        "Because it determines employee salaries",
        "Because other management functions depend on goals and plans established during planning",
        "Because it focuses mainly on supervision of employees",
        "Because it eliminates all business risks"
    ],
    "jawaban_benar": "Because other management functions depend on goals and plans established during planning"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In the planning framework, which sequence correctly represents the logical order?",
    "pilihan": [
        "Goals → Mission → Plans → Performance",
        "Plans → Mission → Performance → Goals",
        "Mission → Goals → Plans → Performance",
        "Performance → Mission → Goals → Plans",
        "Goals → Plans → Mission → Performance"
    ],
    "jawaban_benar": "Mission → Goals → Plans → Performance"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following best defines a mission statement?",
    "pilihan": [
        "A detailed description of company financial performance",
        "A broad declaration of an organization’s purpose and scope",
        "A list of company rules and regulations",
        "A short-term target for employees",
        "A description of operational procedures"
    ],
    "jawaban_benar": "A broad declaration of an organization’s purpose and scope"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which component of a mission statement focuses on identifying who the organization serves?",
    "pilihan": [
        "Technology",
        "Customers",
        "Public Image",
        "Self-Concept",
        "Concern for Survival"
    ],
    "jawaban_benar": "Customers"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company emphasizes environmental responsibility and community welfare in its mission statement. This reflects which component?",
    "pilihan": [
        "Concern for Public Image",
        "Self-Concept",
        "Markets",
        "Technology",
        "Products and Services"
    ],
    "jawaban_benar": "Concern for Public Image"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is an example of a standing plan?",
    "pilihan": [
        "Annual marketing campaign",
        "Construction of a new factory",
        "Company policy on employee attendance",
        "Special project for launching a product",
        "Temporary budget for an event"
    ],
    "jawaban_benar": "Company policy on employee attendance"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A plan created specifically for organizing a one-time international conference is best categorized as:",
    "pilihan": [
        "Standing plan",
        "Single-use plan",
        "Strategic policy",
        "Operational rule",
        "Corporate philosophy"
    ],
    "jawaban_benar": "Single-use plan"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which element of the CASTR goal model ensures that goals are clearly defined and unambiguous?",
    "pilihan": [
        "Challenging",
        "Attainable",
        "Specific",
        "Time-bound",
        "Results-oriented"
    ],
    "jawaban_benar": "Specific"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A manager sets a goal: 'Increase online sales by 15% within the next 12 months.' This goal demonstrates which two CASTR elements most clearly?",
    "pilihan": [
        "Specific and Time-bound",
        "Attainable and Philosophy",
        "Public image and Self-concept",
        "Markets and Technology",
        "Rules and Procedures"
    ],
    "jawaban_benar": "Specific and Time-bound"
},

# =========================
# SHORT ANSWER (5)
# =========================
{
    "tipe": "isian_singkat",
    "pertanyaan": "What is the primary purpose of planning in management?",
    "jawaban_benar": "To select goals and determine actions to achieve them"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "What term describes the broad declaration that explains an organization's purpose and scope?",
    "jawaban_benar": "Mission statement"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Plans that are used repeatedly to guide organizational actions are called ______ plans.",
    "jawaban_benar": "Standing"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "In the CASTR goal model, the letter 'T' stands for ______.",
    "jawaban_benar": "Time-bound"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "In the planning framework, goals are translated into actions through ______.",
    "jawaban_benar": "Plans"
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