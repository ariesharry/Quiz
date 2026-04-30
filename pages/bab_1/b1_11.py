import streamlit as st

soal_list = [
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Corporate Social Responsibility (CSR) refers to:",
    "pilihan": [
        "Maximizing short-term profits only",
        "Obligations of a business to serve both its own interests and those of stakeholders",
        "Following government regulations only",
        "Reducing employee salaries",
        "Ignoring environmental impacts"
    ],
    "jawaban_benar": "Obligations of a business to serve both its own interests and those of stakeholders"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following best describes social responsibility?",
    "pilihan": [
        "Individual moral judgment",
        "Organizational obligation to act ethically toward society",
        "Legal compliance only",
        "Personal belief system",
        "Financial accountability only"
    ],
    "jawaban_benar": "Organizational obligation to act ethically toward society"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Who are considered stakeholders in CSR?",
    "pilihan": [
        "Only shareholders",
        "Only employees",
        "All parties affected by the organization",
        "Government only",
        "Customers only"
    ],
    "jawaban_benar": "All parties affected by the organization"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which stakeholder group primarily expects profit and dividends?",
    "pilihan": [
        "Employees",
        "Customers",
        "Investors",
        "Community",
        "Suppliers"
    ],
    "jawaban_benar": "Investors"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is NOT a stakeholder expectation?",
    "pilihan": [
        "Employee safety",
        "Product quality",
        "Environmental protection",
        "Unlimited profit without responsibility",
        "Fair treatment"
    ],
    "jawaban_benar": "Unlimited profit without responsibility"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The 'capacity argument' in CSR suggests that:",
    "pilihan": [
        "Companies should ignore social issues",
        "Firms have resources to address social problems",
        "Only governments handle social issues",
        "CSR reduces profits",
        "CSR is illegal"
    ],
    "jawaban_benar": "Firms have resources to address social problems"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which level is at the base of the CSR pyramid?",
    "pilihan": [
        "Ethical",
        "Legal",
        "Economic",
        "Philanthropic",
        "Social"
    ],
    "jawaban_benar": "Economic"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which CSR level involves voluntary contributions to society?",
    "pilihan": [
        "Economic",
        "Legal",
        "Ethical",
        "Philanthropic",
        "Operational"
    ],
    "jawaban_benar": "Philanthropic"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Sustainability is best defined as:",
    "pilihan": [
        "Maximizing profits regardless of impact",
        "Meeting present needs without compromising future generations",
        "Reducing costs only",
        "Ignoring environmental concerns",
        "Short-term business growth"
    ],
    "jawaban_benar": "Meeting present needs without compromising future generations"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is NOT one of the three pillars of sustainability?",
    "pilihan": [
        "Economic",
        "Social",
        "Environmental",
        "Technological",
        "All are pillars"
    ],
    "jawaban_benar": "Technological"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The 'People' pillar of sustainability focuses on:",
    "pilihan": [
        "Profit growth",
        "Environmental conservation",
        "Social equity and well-being",
        "Legal compliance",
        "Market expansion"
    ],
    "jawaban_benar": "Social equity and well-being"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The 'Planet' pillar emphasizes:",
    "pilihan": [
        "Financial performance",
        "Employee salaries",
        "Environmental protection",
        "Market share",
        "Customer satisfaction"
    ],
    "jawaban_benar": "Environmental protection"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The 'Profit' pillar in sustainability refers to:",
    "pilihan": [
        "Short-term gains",
        "Illegal earnings",
        "Long-term economic viability",
        "Ignoring stakeholders",
        "Reducing workforce"
    ],
    "jawaban_benar": "Long-term economic viability"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Sustainable Development Goals (SDGs) aim to:",
    "pilihan": [
        "Increase company profits only",
        "Promote global social, economic, and environmental development",
        "Reduce regulations",
        "Focus only on developed countries",
        "Eliminate businesses"
    ],
    "jawaban_benar": "Promote global social, economic, and environmental development"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which concept emphasizes balancing people, planet, and profit?",
    "pilihan": [
        "Corporate governance",
        "Triple bottom line",
        "Market equilibrium",
        "Cost leadership",
        "Competitive advantage"
    ],
    "jawaban_benar": "Triple bottom line"
},

{
    "tipe": "isian_singkat",
    "pertanyaan": "CSR stands for Corporate Social ______.",
    "jawaban_benar": "Responsibility"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The three pillars of sustainability are People, Planet, and ______.",
    "jawaban_benar": "Profit"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "The voluntary level of CSR is called ______.",
    "jawaban_benar": "Philanthropic"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Meeting present needs without harming future generations is called ______.",
    "jawaban_benar": "Sustainability"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Global goals for sustainable development are known as ______.",
    "jawaban_benar": "SDGs"
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