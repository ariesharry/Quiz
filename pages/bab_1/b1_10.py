import streamlit as st

soal_list = [
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "What is the best definition of ethics?",
    "pilihan": [
        "Rules enforced by the government",
        "A set of moral principles that define right and wrong",
        "Company policies and procedures",
        "Cultural traditions only",
        "Personal preferences without standards"
    ],
    "jawaban_benar": "A set of moral principles that define right and wrong"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Business ethics primarily deals with:",
    "pilihan": [
        "Legal compliance only",
        "Financial performance",
        "Ethical issues in a commercial context",
        "Government regulations",
        "Employee contracts"
    ],
    "jawaban_benar": "Ethical issues in a commercial context"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is a benefit of ethical behavior in organizations?",
    "pilihan": [
        "Increased legal risk",
        "Reduced customer trust",
        "Improved company image",
        "Higher employee turnover",
        "Lower accountability"
    ],
    "jawaban_benar": "Improved company image"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "What is the main difference between law and ethics?",
    "pilihan": [
        "Law is optional, ethics is mandatory",
        "Ethics is enforced by government",
        "Law is a minimum standard, ethics goes beyond it",
        "There is no difference",
        "Ethics applies only to individuals"
    ],
    "jawaban_benar": "Law is a minimum standard, ethics goes beyond it"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An ethical dilemma occurs when:",
    "pilihan": [
        "There is a clear right answer",
        "Only one option is available",
        "There are conflicting moral choices",
        "Laws are strictly followed",
        "No consequences exist"
    ],
    "jawaban_benar": "There are conflicting moral choices"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is NOT a characteristic of an ethical dilemma?",
    "pilihan": [
        "Conflicting values",
        "Clear right and wrong answer",
        "Significant consequences",
        "Time pressure",
        "Multiple alternatives"
    ],
    "jawaban_benar": "Clear right and wrong answer"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which factor contributes to ethical problems in business?",
    "pilihan": [
        "Strong moral values",
        "High transparency",
        "Personal gain and self-interest",
        "Clear regulations",
        "Ethics training"
    ],
    "jawaban_benar": "Personal gain and self-interest"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Ego strength refers to:",
    "pilihan": [
        "Physical strength of an individual",
        "Ability to influence others",
        "Strength of a person's moral convictions",
        "Level of intelligence",
        "Position in organization"
    ],
    "jawaban_benar": "Strength of a person's moral convictions"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Locus of control is defined as:",
    "pilihan": [
        "Control over other people",
        "Degree to which people believe they control their own fate",
        "Company control system",
        "Legal authority",
        "External pressure"
    ],
    "jawaban_benar": "Degree to which people believe they control their own fate"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "At which stage of moral development do individuals follow rules to avoid punishment?",
    "pilihan": [
        "Post-conventional",
        "Conventional",
        "Pre-conventional",
        "Universal stage",
        "Ethical stage"
    ],
    "jawaban_benar": "Pre-conventional"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Ethical intensity refers to:",
    "pilihan": [
        "Level of company profit",
        "Degree of legal enforcement",
        "Level of concern about an ethical issue",
        "Employee motivation",
        "Organizational hierarchy"
    ],
    "jawaban_benar": "Level of concern about an ethical issue"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which component of ethical intensity refers to total harm or benefit?",
    "pilihan": [
        "Social consensus",
        "Proximity",
        "Magnitude of consequences",
        "Probability of effect",
        "Concentration effect"
    ],
    "jawaban_benar": "Magnitude of consequences"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which organizational factor most strongly influences ethical behavior?",
    "pilihan": [
        "Office design",
        "Manager behavior",
        "Salary level",
        "Work hours",
        "Job title"
    ],
    "jawaban_benar": "Manager behavior"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The principle of utilitarianism focuses on:",
    "pilihan": [
        "Individual rights",
        "Personal virtue",
        "Maximizing overall benefits over harms",
        "Strict legal compliance",
        "Cultural norms"
    ],
    "jawaban_benar": "Maximizing overall benefits over harms"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Distributive justice emphasizes:",
    "pilihan": [
        "Profit maximization",
        "Fairness and equity",
        "Personal gain",
        "Legal enforcement",
        "Speed of decision-making"
    ],
    "jawaban_benar": "Fairness and equity"
},

{
    "tipe": "isian_singkat",
    "pertanyaan": "The principles that define right and wrong behavior are called ______.",
    "jawaban_benar": "Ethics"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "A situation involving conflicting moral choices is called an ethical ______.",
    "jawaban_benar": "Dilemma"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The stage of moral development based on internal principles is called ______-conventional.",
    "jawaban_benar": "Post"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The principle that focuses on fairness and equality is called distributive ______.",
    "jawaban_benar": "Justice"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The idea of maximizing benefits over harms is known as ______.",
    "jawaban_benar": "Utilitarianism"
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