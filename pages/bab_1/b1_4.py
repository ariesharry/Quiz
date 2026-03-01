import streamlit as st

soal_list = [
    # =========================
    # PILIHAN GANDA (10)
    # =========================
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Motivation is best defined as:",
        "pilihan": [
            "The ability to complete tasks efficiently",
            "A set of forces that initiates, directs, and sustains behaviour toward goals",
            "A reward system used by managers",
            "Employee satisfaction with salary",
            "A leadership style"
        ],
        "jawaban_benar": "A set of forces that initiates, directs, and sustains behaviour toward goals"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "According to the performance equation, performance is the result of:",
        "pilihan": [
            "Motivation × Rewards × Ability",
            "Ability × Motivation × Situation",
            "Skills × Experience × Pay",
            "Effort × Time × Supervision",
            "Motivation × Leadership × Power"
        ],
        "jawaban_benar": "Ability × Motivation × Situation"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Intrinsic motivation refers to motivation that comes from:",
        "pilihan": [
            "Salary increases",
            "Bonuses and promotions",
            "Interest and enjoyment in the task itself",
            "Punishment avoidance",
            "Managerial pressure"
        ],
        "jawaban_benar": "Interest and enjoyment in the task itself"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Extrinsic motivation is primarily driven by:",
        "pilihan": [
            "Personal growth",
            "Internal satisfaction",
            "Interest in work",
            "Rewards and punishments",
            "Self-actualisation"
        ],
        "jawaban_benar": "Rewards and punishments"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Maslow’s hierarchy of needs suggests that people are motivated by:",
        "pilihan": [
            "Only financial rewards",
            "Needs that are already satisfied",
            "Needs that are not yet satisfied",
            "Organisational goals",
            "Managerial expectations"
        ],
        "jawaban_benar": "Needs that are not yet satisfied"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Which of the following is the highest level in Maslow’s hierarchy of needs?",
        "pilihan": [
            "Safety",
            "Social",
            "Esteem",
            "Physiological",
            "Self-actualisation"
        ],
        "jawaban_benar": "Self-actualisation"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "The deficit principle states that:",
        "pilihan": [
            "Satisfied needs strongly motivate behaviour",
            "Unsatisfied needs drive behaviour",
            "All needs motivate equally",
            "Higher-level needs must be met first",
            "Motivation depends on personality"
        ],
        "jawaban_benar": "Unsatisfied needs drive behaviour"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Goal-setting theory argues that motivation increases when goals are:",
        "pilihan": [
            "Easy and flexible",
            "Vague and general",
            "Specific and challenging",
            "Assigned only by managers",
            "Focused on rewards only"
        ],
        "jawaban_benar": "Specific and challenging"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "Equity theory is based on the idea that employees:",
        "pilihan": [
            "Work only for money",
            "Compare their input–output ratios with others",
            "Prefer intrinsic rewards",
            "Are motivated only by goals",
            "Ignore fairness issues"
        ],
        "jawaban_benar": "Compare their input–output ratios with others"
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "A likely response to perceived under-reward inequity is that employees may:",
        "pilihan": [
            "Increase effort",
            "Ignore the situation",
            "Reduce effort or quit",
            "Become more loyal",
            "Work overtime"
        ],
        "jawaban_benar": "Reduce effort or quit"
    },

    # =========================
    # ISIAN SINGKAT (5)
    # =========================
    {
        "tipe": "isian",
        "pertanyaan": "Performance is influenced by ability, motivation, and ________.",
        "jawaban_benar": "situation"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Motivation that comes from internal satisfaction is called ________ motivation.",
        "jawaban_benar": "intrinsic"
    },
    {
        "tipe": "isian",
        "pertanyaan": "According to Maslow, once lower-level needs are satisfied, people strive for ________ needs.",
        "jawaban_benar": "higher-level"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Goal-setting theory emphasises the importance of feedback and making ________ toward goals.",
        "jawaban_benar": "progress"
    },
    {
        "tipe": "isian",
        "pertanyaan": "Equity theory is based on the principle of social ________.",
        "jawaban_benar": "comparison"
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