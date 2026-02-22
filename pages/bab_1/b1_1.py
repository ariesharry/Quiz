import streamlit as st

# Definisi soal
soal_list = [
    # =========================
    # PILIHAN GANDA (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Management is defined as the attainment of organisational goals in an effective and efficient manner through which four functions?",
        "pilihan": [
            "Planning, Organising, Staffing, Reporting",
            "Planning, Organising, Leading, Controlling",
            "Leading, Directing, Controlling, Evaluating",
            "Organising, Budgeting, Staffing, Leading",
            "Planning, Marketing, Leading, Controlling"
        ],
        "jawaban_benar": "Planning, Organising, Leading, Controlling"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Effectiveness in management refers to:",
        "pilihan": [
            "Minimising costs",
            "Doing things right",
            "Achieving organisational goals",
            "Reducing employees",
            "Increasing supervision"
        ],
        "jawaban_benar": "Achieving organisational goals"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "According to Mintzberg, managers prefer which type of communication?",
        "pilihan": [
            "Written reports",
            "Formal emails",
            "Verbal communication",
            "Automated systems",
            "Digital dashboards"
        ],
        "jawaban_benar": "Verbal communication"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Power is defined as the potential ability to:",
        "pilihan": [
            "Control financial resources",
            "Influence the behaviour of others",
            "Reward employees",
            "Hire and fire staff",
            "Increase production output"
        ],
        "jawaban_benar": "Influence the behaviour of others"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Trait theory suggests that:",
        "pilihan": [
            "Leaders are trained through experience only",
            "Leadership depends entirely on followers",
            "Leaders are born, not made",
            "Leadership changes in every situation",
            "All managers are leaders"
        ],
        "jawaban_benar": "Leaders are born, not made"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is an example of a leadership trait mentioned in the lecture?",
        "pilihan": [
            "Technical coding ability",
            "Honesty and integrity",
            "Marketing expertise",
            "Financial forecasting",
            "Sales negotiation"
        ],
        "jawaban_benar": "Honesty and integrity"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The behavioural approach focuses on:",
        "pilihan": [
            "Who leaders are",
            "What leaders do",
            "How leaders are born",
            "Organisational profit only",
            "Financial outcomes"
        ],
        "jawaban_benar": "What leaders do"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Blake and McCanse’s leadership grid is based on which two dimensions?",
        "pilihan": [
            "Power and influence",
            "Integrity and honesty",
            "Concern for production and concern for people",
            "Ability and confidence",
            "Experience and knowledge"
        ],
        "jawaban_benar": "Concern for production and concern for people"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "In the situational leadership model, readiness refers to:",
        "pilihan": [
            "Leader’s experience level",
            "Organisational budget",
            "How able, willing and confident followers are",
            "The company’s size",
            "Manager’s authority"
        ],
        "jawaban_benar": "How able, willing and confident followers are"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Servant leadership emphasises:",
        "pilihan": [
            "Leader’s personal power",
            "Strict control of employees",
            "Serving others and focusing on followers",
            "Maximising profit above all",
            "Reducing employee autonomy"
        ],
        "jawaban_benar": "Serving others and focusing on followers"
    },

    # =========================
    # ISIAN SINGKAT (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "Management involves planning, organising, leading and ________.",
        "jawaban_benar": "controlling"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Leadership is the process of influencing others to achieve group or organisational ________.",
        "jawaban_benar": "goals"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The two dimensions of leadership style are concern for production and concern for ________.",
        "jawaban_benar": "people"
    },
    {
        "tipe": "isian",
        "pertanyaan": "In Hersey and Blanchard’s model, D4 followers are confident, willing and ________.",
        "jawaban_benar": "able"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Māori leadership emphasises community, relationships, integrity, stewardship and ________.",
        "jawaban_benar": "empathy"
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