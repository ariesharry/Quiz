import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which statement best describes the concept of organising in management?",
    "pilihan": [
        "Monitoring employee performance and correcting errors",
        "Deploying organisational resources and aligning activities to achieve strategic goals",
        "Developing financial forecasts for future investments",
        "Motivating employees through leadership practices",
        "Setting long-term organisational objectives"
    ],
    "jawaban_benar": "Deploying organisational resources and aligning activities to achieve strategic goals"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following questions is typically addressed during the organising process?",
    "pilihan": [
        "How much profit should the company generate?",
        "Which marketing campaign should be launched first?",
        "Who will perform specific tasks and how those tasks are grouped?",
        "What will be the company's future mission statement?",
        "How will competitors respond to pricing changes?"
    ],
    "jawaban_benar": "Who will perform specific tasks and how those tasks are grouped?"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which description best represents a formal organisational structure?",
    "pilihan": [
        "Social relationships that develop naturally among employees",
        "An unofficial network of communication among staff",
        "The officially defined system of tasks, reporting relationships, and communication channels",
        "A temporary project team formed to solve a problem",
        "Personal friendships formed in the workplace"
    ],
    "jawaban_benar": "The officially defined system of tasks, reporting relationships, and communication channels"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which job design approach involves moving employees from one job to another to develop broader skills?",
    "pilihan": [
        "Job Simplification",
        "Job Rotation",
        "Job Enlargement",
        "Job Specialisation",
        "Job Automation"
    ],
    "jawaban_benar": "Job Rotation"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which job design approach increases the number of tasks performed by an employee in order to reduce boredom?",
    "pilihan": [
        "Job Enlargement",
        "Job Simplification",
        "Job Rotation",
        "Centralisation",
        "Formalisation"
    ],
    "jawaban_benar": "Job Enlargement"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Grouping employees into departments such as marketing, finance, and human resources is an example of which type of departmentalisation?",
    "pilihan": [
        "Customer departmentalisation",
        "Functional departmentalisation",
        "Geographic departmentalisation",
        "Product departmentalisation",
        "Team-based departmentalisation"
    ],
    "jawaban_benar": "Functional departmentalisation"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An organisation that groups its operations by geographic regions such as Asia, Europe, and America is using which type of structure?",
    "pilihan": [
        "Functional structure",
        "Divisional structure",
        "Matrix structure",
        "Process structure",
        "Informal structure"
    ],
    "jawaban_benar": "Divisional structure"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Vertical differentiation in an organisation refers to:",
    "pilihan": [
        "The number of management levels within the organisation",
        "The number of departments performing different functions",
        "The distribution of employees across geographic locations",
        "The degree of employee collaboration in teams",
        "The level of customer involvement in decision making"
    ],
    "jawaban_benar": "The number of management levels within the organisation"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which concept describes the degree to which rules, procedures, and job descriptions are standardised in an organisation?",
    "pilihan": [
        "Centralisation",
        "Formalisation",
        "Differentiation",
        "Departmentalisation",
        "Coordination"
    ],
    "jawaban_benar": "Formalisation"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "When most decision-making authority is concentrated at the top levels of management, the organisation is described as:",
    "pilihan": [
        "Decentralised",
        "Organic",
        "Centralised",
        "Team-based",
        "Informal"
    ],
    "jawaban_benar": "Centralised"
},

# =========================
# SHORT ANSWER (5)
# =========================
{
    "tipe": "isian_singkat",
    "pertanyaan": "What is the term used to describe the grouping of jobs and employees into departments?",
    "jawaban_benar": "Departmentalisation"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "In organisational structure, the number of management layers in a company is known as ______ differentiation.",
    "jawaban_benar": "Vertical"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The degree to which decision-making authority is concentrated at higher levels of management is called ______.",
    "jawaban_benar": "Centralisation"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The model that explains how job characteristics influence employee motivation is called the ______ model.",
    "jawaban_benar": "Job Characteristics"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "An organisational design that emphasises flexibility, collaboration, and decentralised decision making is known as an ______ organisation.",
    "jawaban_benar": "Adaptive"
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