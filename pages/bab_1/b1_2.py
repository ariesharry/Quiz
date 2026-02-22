import streamlit as st

# Definisi soal
soal_list = [
    # =========================
    # PILIHAN GANDA (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Leadership is defined as:",
        "pilihan": [
            "Controlling employees to increase profit",
            "The process of influencing others to achieve group or organisational goals",
            "Managing financial resources efficiently",
            "Supervising employees daily",
            "Making strategic plans only"
        ],
        "jawaban_benar": "The process of influencing others to achieve group or organisational goals"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Power is defined as the potential ability to:",
        "pilihan": [
            "Control organisational budgets",
            "Reward employees",
            "Influence the behaviour of others",
            "Increase production",
            "Hire staff"
        ],
        "jawaban_benar": "Influence the behaviour of others"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Influence refers to the effect of a person’s actions on others’:",
        "pilihan": [
            "Salaries only",
            "Attitudes, values, beliefs, or behaviour",
            "Work schedules",
            "Organisational charts",
            "Technical skills"
        ],
        "jawaban_benar": "Attitudes, values, beliefs, or behaviour"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Trait theory suggests that:",
        "pilihan": [
            "Leadership depends entirely on situation",
            "Leaders are born, not made",
            "Leadership is learned only through training",
            "All managers are leaders",
            "Leadership is temporary"
        ],
        "jawaban_benar": "Leaders are born, not made"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is mentioned as a leadership trait?",
        "pilihan": [
            "Emotional stability",
            "Accounting skills",
            "Programming ability",
            "Marketing strategy",
            "Budget analysis"
        ],
        "jawaban_benar": "Emotional stability"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The behavioural approach focuses on:",
        "pilihan": [
            "Who leaders are",
            "What leaders do",
            "Where leaders work",
            "Why organisations fail",
            "Financial outcomes"
        ],
        "jawaban_benar": "What leaders do"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Blake and McCanse’s leadership grid is based on:",
        "pilihan": [
            "Power and authority",
            "Concern for production and concern for people",
            "Integrity and honesty",
            "Experience and age",
            "Ability and intelligence"
        ],
        "jawaban_benar": "Concern for production and concern for people"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "In situational leadership theory, readiness refers to:",
        "pilihan": [
            "Leader’s authority level",
            "How able, willing and confident followers are",
            "Organisational size",
            "Budget availability",
            "Leader’s experience"
        ],
        "jawaban_benar": "How able, willing and confident followers are"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "According to Hersey & Blanchard, D4 followers are:",
        "pilihan": [
            "Insecure and not ready",
            "Confident but not able",
            "Able but unwilling",
            "Confident, willing and able",
            "Not confident and unwilling"
        ],
        "jawaban_benar": "Confident, willing and able"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Servant leadership emphasises:",
        "pilihan": [
            "Leader’s personal power",
            "Serving others and focusing on followers",
            "Strict supervision",
            "Maximising control",
            "Reducing employee autonomy"
        ],
        "jawaban_benar": "Serving others and focusing on followers"
    },

    # =========================
    # ISIAN SINGKAT (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "Leadership is one of the four main functions of ________.",
        "jawaban_benar": "management"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Trait theory is also known as the 'Great ________' theory.",
        "jawaban_benar": "man"
    },
    {
        "tipe": "isian",
        "pertanyaan": "The two dimensions of leadership style are concern for production and concern for ________.",
        "jawaban_benar": "people"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Follower readiness includes job readiness and ________ readiness.",
        "jawaban_benar": "psychological"
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