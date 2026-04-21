import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (15)
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which statement best defines Human Resource Management (HRM)?",
    "pilihan": [
        "Managing financial resources to maximise profit",
        "Ensuring the organisation has the right people with the right skills at the right time",
        "Designing marketing strategies to attract customers",
        "Controlling operational processes to reduce costs",
        "Developing technological systems for business operations"
    ],
    "jawaban_benar": "Ensuring the organisation has the right people with the right skills at the right time"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which activity is primarily associated with identifying HR needs?",
    "pilihan": [
        "Performance appraisal",
        "Workforce planning",
        "Employee training",
        "Compensation management",
        "Conflict resolution"
    ],
    "jawaban_benar": "Workforce planning"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Recruitment is best described as:",
    "pilihan": [
        "Selecting the best candidate from a pool of applicants",
        "Training employees to improve their performance",
        "Developing a pool of qualified candidates for a job",
        "Evaluating employee performance over time",
        "Designing compensation systems"
    ],
    "jawaban_benar": "Developing a pool of qualified candidates for a job"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is an example of internal recruitment?",
    "pilihan": [
        "Hiring from job portals",
        "Using recruitment agencies",
        "Promoting an existing employee",
        "Campus recruitment",
        "Advertising in newspapers"
    ],
    "jawaban_benar": "Promoting an existing employee"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "What is the main purpose of a Realistic Job Preview (RJP)?",
    "pilihan": [
        "To attract as many candidates as possible",
        "To provide only positive aspects of a job",
        "To give accurate and complete job information to candidates",
        "To reduce recruitment costs",
        "To speed up the hiring process"
    ],
    "jawaban_benar": "To give accurate and complete job information to candidates"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which step comes immediately after recruitment in the HRM process?",
    "pilihan": [
        "Training",
        "Selection",
        "Performance management",
        "Compensation",
        "Orientation"
    ],
    "jawaban_benar": "Selection"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is NOT typically part of the selection process?",
    "pilihan": [
        "Interview",
        "Testing",
        "Reference check",
        "Advertising vacancies",
        "Final decision making"
    ],
    "jawaban_benar": "Advertising vacancies"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Structured interviews are preferred because they:",
    "pilihan": [
        "Allow complete flexibility in questioning",
        "Make comparison between candidates easier",
        "Focus only on informal discussions",
        "Eliminate the need for evaluation",
        "Reduce the number of applicants"
    ],
    "jawaban_benar": "Make comparison between candidates easier"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The STAR technique in interviews is used to:",
    "pilihan": [
        "Measure technical knowledge",
        "Evaluate past behavior and experiences",
        "Determine salary expectations",
        "Assess personality traits only",
        "Conduct group discussions"
    ],
    "jawaban_benar": "Evaluate past behavior and experiences"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "One major risk of using AI in employee selection is:",
    "pilihan": [
        "Higher operational efficiency",
        "Reduced hiring time",
        "Algorithmic bias",
        "Improved data processing",
        "Lower recruitment costs"
    ],
    "jawaban_benar": "Algorithmic bias"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which HRM activity focuses on improving employee skills and capabilities?",
    "pilihan": [
        "Recruitment",
        "Selection",
        "Training and development",
        "Compensation",
        "Job analysis"
    ],
    "jawaban_benar": "Training and development"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following best describes orientation in HRM?",
    "pilihan": [
        "Evaluating employee performance annually",
        "Introducing new employees to the organisation and its culture",
        "Designing salary structures",
        "Recruiting new candidates",
        "Conducting exit interviews"
    ],
    "jawaban_benar": "Introducing new employees to the organisation and its culture"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which selection method assesses a candidate’s problem-solving and decision-making ability?",
    "pilihan": [
        "Reference check",
        "Cognitive testing",
        "Panel interview",
        "Background verification",
        "Job advertisement"
    ],
    "jawaban_benar": "Cognitive testing"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is a benefit of using a Realistic Job Preview (RJP)?",
    "pilihan": [
        "Higher employee turnover",
        "Lower job satisfaction",
        "Better employee retention",
        "Increased recruitment cost",
        "Reduced candidate pool"
    ],
    "jawaban_benar": "Better employee retention"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which HRM function deals with salaries, benefits, and rewards?",
    "pilihan": [
        "Recruitment",
        "Training",
        "Performance management",
        "Compensation and remuneration",
        "Selection"
    ],
    "jawaban_benar": "Compensation and remuneration"
},

# =========================
# SHORT ANSWER (5)
# =========================
{
    "tipe": "isian_singkat",
    "pertanyaan": "What is the process of attracting a pool of qualified candidates called?",
    "jawaban_benar": "Recruitment"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Providing honest and complete information about a job to candidates is known as ______.",
    "jawaban_benar": "Realistic Job Preview"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The process of evaluating and choosing the best candidate is called ______.",
    "jawaban_benar": "Selection"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "In the STAR technique, the letter 'A' stands for ______.",
    "jawaban_benar": "Action"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The use of algorithms and software to perform HR tasks is referred to as ______ in HRM.",
    "jawaban_benar": "Artificial Intelligence"
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