import streamlit as st

# Definisi soal
soal_list = [
    # =========================
    # PILIHAN GANDA (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Management is best described as the process of:",
        "pilihan": [
            "Supervising employees on a daily basis",
            "Achieving organisational goals effectively and efficiently",
            "Controlling people to maximise profit",
            "Making decisions only at the top level",
            "Managing financial resources only"
        ],
        "jawaban_benar": "Achieving organisational goals effectively and efficiently"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is NOT one of the four management functions?",
        "pilihan": [
            "Planning",
            "Organising",
            "Leading",
            "Controlling",
            "Staffing"
        ],
        "jawaban_benar": "Staffing"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Effectiveness in management refers to:",
        "pilihan": [
            "Minimising costs",
            "Using fewer resources",
            "Doing the right things",
            "Doing things right",
            "Increasing efficiency"
        ],
        "jawaban_benar": "Doing the right things"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Efficiency is primarily concerned with:",
        "pilihan": [
            "Goal achievement",
            "Employee satisfaction",
            "Resource utilisation",
            "Strategic vision",
            "Leadership style"
        ],
        "jawaban_benar": "Resource utilisation"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which management function involves grouping tasks and allocating resources?",
        "pilihan": [
            "Planning",
            "Organising",
            "Leading",
            "Controlling",
            "Motivating"
        ],
        "jawaban_benar": "Organising"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Middle managers are primarily responsible for:",
        "pilihan": [
            "Setting organisational vision",
            "Supervising frontline employees only",
            "Managing departments or business units",
            "Performing technical tasks",
            "Owning the company"
        ],
        "jawaban_benar": "Managing departments or business units"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Functional managers differ from general managers because they:",
        "pilihan": [
            "Work at higher organisational levels",
            "Manage entire organisations",
            "Oversee a specific functional area",
            "Focus only on strategy",
            "Have no staff responsibility"
        ],
        "jawaban_benar": "Oversee a specific functional area"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which managerial skill is most important for first-line managers?",
        "pilihan": [
            "Conceptual skills",
            "Human skills",
            "Technical skills",
            "Strategic thinking",
            "Political skills"
        ],
        "jawaban_benar": "Technical skills"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Conceptual skills are best described as the ability to:",
        "pilihan": [
            "Motivate employees",
            "Perform specialised tasks",
            "Understand the organisation as a whole",
            "Communicate with teams",
            "Control daily operations"
        ],
        "jawaban_benar": "Understand the organisation as a whole"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which statement best describes the relationship between management levels and skills?",
        "pilihan": [
            "Top managers rely most on technical skills",
            "All managers need the same skills in equal amounts",
            "Conceptual skills increase in importance at higher levels",
            "Human skills are only important for middle managers",
            "Skills are unrelated to management level"
        ],
        "jawaban_benar": "Conceptual skills increase in importance at higher levels"
    },

    # =========================
    # ISIAN SINGKAT (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "The four functions of management are planning, organising, leading, and ________.",
        "jawaban_benar": "controlling"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Doing things right refers to managerial ________.",
        "jawaban_benar": "efficiency"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Top managers are responsible for the entire ________.",
        "jawaban_benar": "organisation"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Managers who are responsible for departments such as marketing or HR are called ________ managers.",
        "jawaban_benar": "functional"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The ability to work well with other people is known as ________ skills.",
        "jawaban_benar": "human"
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