import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (15)
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which statement best defines a team?",
    "pilihan": [
        "A group of individuals working independently",
        "Two or more people who interact and coordinate to achieve a common goal",
        "Employees assigned to different departments",
        "A collection of individuals with no shared objectives",
        "A temporary group with no accountability"
    ],
    "jawaban_benar": "Two or more people who interact and coordinate to achieve a common goal"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is NOT a characteristic of an effective team?",
    "pilihan": [
        "Shared goals",
        "Mutual accountability",
        "Complementary skills",
        "Lack of communication",
        "Regular interaction"
    ],
    "jawaban_benar": "Lack of communication"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Team diversity primarily refers to differences in:",
    "pilihan": [
        "Salary levels",
        "Organisational hierarchy",
        "Values, personalities, and experiences",
        "Working hours",
        "Office location"
    ],
    "jawaban_benar": "Values, personalities, and experiences"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "What is a key benefit of team diversity?",
    "pilihan": [
        "Reduced conflict",
        "Limited perspectives",
        "Improved problem-solving and creativity",
        "Less communication",
        "Simpler decision-making"
    ],
    "jawaban_benar": "Improved problem-solving and creativity"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which stage of team development is characterised by conflict and disagreement?",
    "pilihan": [
        "Forming",
        "Storming",
        "Norming",
        "Performing",
        "Adjourning"
    ],
    "jawaban_benar": "Storming"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is a common problem in teams?",
    "pilihan": [
        "Clear communication",
        "Strong leadership",
        "Personality conflicts",
        "Shared goals",
        "Defined roles"
    ],
    "jawaban_benar": "Personality conflicts"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Task conflict refers to disagreements about:",
    "pilihan": [
        "Personal relationships",
        "Emotions and trust",
        "Goals and work tasks",
        "Work schedules",
        "Salary levels"
    ],
    "jawaban_benar": "Goals and work tasks"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which type of conflict is generally considered constructive?",
    "pilihan": [
        "Relationship conflict",
        "Dysfunctional conflict",
        "Functional conflict",
        "Personal conflict",
        "Emotional conflict"
    ],
    "jawaban_benar": "Functional conflict"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Dysfunctional conflict typically results in:",
    "pilihan": [
        "Improved creativity",
        "Better cooperation",
        "Higher productivity",
        "Reduced performance",
        "Enhanced innovation"
    ],
    "jawaban_benar": "Reduced performance"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Social loafing occurs when:",
    "pilihan": [
        "Employees work harder in teams",
        "Individuals reduce effort when working in groups",
        "Teams have clear goals",
        "Group size decreases",
        "Tasks are well defined"
    ],
    "jawaban_benar": "Individuals reduce effort when working in groups"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which factor increases the likelihood of social loafing?",
    "pilihan": [
        "Small team size",
        "High accountability",
        "Large team size",
        "Clear roles",
        "Strong leadership"
    ],
    "jawaban_benar": "Large team size"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Team cohesiveness refers to:",
    "pilihan": [
        "The level of competition within a team",
        "The extent to which members are attracted to and committed to the team",
        "The number of tasks assigned to a team",
        "The structure of the organisation",
        "The level of external pressure on the team"
    ],
    "jawaban_benar": "The extent to which members are attracted to and committed to the team"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "High team cohesiveness is most effective when:",
    "pilihan": [
        "Performance norms are negative",
        "There is no leadership",
        "Performance norms are positive",
        "Tasks are unclear",
        "Conflict is avoided completely"
    ],
    "jawaban_benar": "Performance norms are positive"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following can improve team cohesion?",
    "pilihan": [
        "Reducing interaction among members",
        "Eliminating team goals",
        "Encouraging shared goals",
        "Increasing ambiguity",
        "Avoiding collaboration"
    ],
    "jawaban_benar": "Encouraging shared goals"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Balancing conflict and cooperation in teams aims to:",
    "pilihan": [
        "Eliminate all conflict",
        "Maximise performance through optimal conflict levels",
        "Reduce team interaction",
        "Avoid decision-making",
        "Increase hierarchy"
    ],
    "jawaban_benar": "Maximise performance through optimal conflict levels"
},

# =========================
# SHORT ANSWER (5)
# =========================
{
    "tipe": "isian_singkat",
    "pertanyaan": "The stage of team development where members start to resolve conflicts and establish norms is called ______.",
    "jawaban_benar": "Norming"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Conflict related to emotions and personal issues is known as ______ conflict.",
    "jawaban_benar": "Relationship"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The tendency of individuals to exert less effort in a group is called ______.",
    "jawaban_benar": "Social loafing"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The degree to which team members are attracted to each other and motivated to stay in the team is called ______.",
    "jawaban_benar": "Cohesiveness"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Conflict that improves team performance and creativity is called ______ conflict.",
    "jawaban_benar": "Functional"
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