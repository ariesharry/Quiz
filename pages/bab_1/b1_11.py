import streamlit as st

# =========================
# QUESTION DATA (REFACTORED - MORE DETAILED & LONGER)
# =========================
soal_list = [

# =========================
# 15 MULTIPLE CHOICE (ENRICHED WITH SCENARIOS)
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "PT Hijau Lestari, a manufacturing company, decides not only to pursue profit but also to build city parks, recycle waste, and provide scholarships. This practice reflects the concept of:",
    "pilihan": [
        "Maximizing short-term profits only",
        "A business's obligation to serve both its own interests and those of stakeholders (CSR)",
        "Following government regulations only",
        "Reducing employee salaries",
        "Ignoring environmental impacts"
    ],
    "jawaban_benar": "A business's obligation to serve both its own interests and those of stakeholders"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A cigarette company donates to youth sports programs, but its products remain harmful to health. Does this action fulfill social responsibility? True social responsibility requires:",
    "pilihan": [
        "Individual moral judgment",
        "An organization's obligation to act ethically toward society",
        "Legal compliance only",
        "Personal belief system",
        "Financial accountability only"
    ],
    "jawaban_benar": "An organization's obligation to act ethically toward society"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "When the management of PT Maju Jaya plans to close a factory, many parties are affected: workers lose livelihoods, suppliers lose buyers, the local community loses economic sources, and creditors worry about bad loans. These groups are called:",
    "pilihan": [
        "Only shareholders",
        "Only employees",
        "All parties affected by the organization (stakeholders)",
        "Government only",
        "Customers only"
    ],
    "jawaban_benar": "All parties affected by the organization"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An investor puts capital into a startup. He expects dividends and share price appreciation each year. This stakeholder group primarily expects:",
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
    "pertanyaan": "In a CSR discussion, which of the following is NOT a reasonable stakeholder expectation?",
    "pilihan": [
        "Workplace safety for employees",
        "Product quality for customers",
        "Environmental protection for the community",
        "Unlimited profit without responsibility",
        "Fair treatment for all parties"
    ],
    "jawaban_benar": "Unlimited profit without responsibility"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The 'capacity argument' in CSR states that large companies like Google or Toyota have funds, technology, and expertise to solve social problems (e.g., forest fires or poverty). The core of this argument is:",
    "pilihan": [
        "Companies should ignore social issues",
        "Firms have resources to address social problems",
        "Only governments should handle social issues",
        "CSR reduces profits",
        "CSR is illegal"
    ],
    "jawaban_benar": "Firms have resources to address social problems"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In Carroll's CSR pyramid, the most basic level (foundation) is the obligation to earn profit because a company must survive. This level is called:",
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
    "pertanyaan": "A company voluntarily builds hospitals and schools in a remote area without legal pressure or ethical demands. This CSR level is called:",
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
    "pertanyaan": "A conservation specialist defines sustainable development as meeting present needs without compromising the ability of future generations to meet their own needs. This definition refers to the concept of:",
    "pilihan": [
        "Maximizing profits regardless of impact",
        "Meeting present needs without compromising future generations (sustainability)",
        "Reducing costs only",
        "Ignoring environmental concerns",
        "Short-term business growth"
    ],
    "jawaban_benar": "Meeting present needs without compromising future generations"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In sustainable development, the three main pillars are economic, social, and environmental. Which of the following is NOT one of these three pillars?",
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
    "pertanyaan": "The 'People' pillar of sustainability emphasizes employee well‑being, human rights, social justice, and community participation. The main focus of this pillar is:",
    "pilihan": [
        "Profit growth",
        "Environmental conservation",
        "Social equity and well‑being",
        "Legal compliance",
        "Market expansion"
    ],
    "jawaban_benar": "Social equity and well‑being"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The 'Planet' pillar of sustainability focuses on ecosystem protection, emission reduction, waste management, and natural resource conservation. This means emphasizing:",
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
    "pertanyaan": "The 'Profit' pillar in the triple bottom line does not mean short‑term profit, but rather long‑term economic viability that does not damage the social and environmental pillars. The correct definition is:",
    "pilihan": [
        "Short‑term gains",
        "Illegal earnings",
        "Long‑term economic viability",
        "Ignoring stakeholders",
        "Reducing the workforce"
    ],
    "jawaban_benar": "Long‑term economic viability"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The Sustainable Development Goals (SDGs) launched by the UN aim to end poverty, protect the planet, and ensure prosperity for all by 2030. The main objective of the SDGs is:",
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
    "pertanyaan": "The concept that balances company performance across three dimensions – profit, people, and planet – is known as the:",
    "pilihan": [
        "Corporate governance",
        "Triple bottom line",
        "Market equilibrium",
        "Cost leadership",
        "Competitive advantage"
    ],
    "jawaban_benar": "Triple bottom line"
},

# =========================
# USE CASE GROUP (10 FILL‑IN‑THE‑BLANK) - INTEGRATED STORY
# =========================
{
    "tipe": "use_case_group",
    "bacaan": """
PT EcoNusa is a medium‑sized textile company operating along a riverbank. For 10 years, the company focused only on profit. Dye waste was dumped directly into the river, workers were paid below minimum wage, and there were no community programs.

Last year, new management under CEO Sarah decided to change direction. Sarah realized that the company could not survive on short‑term profit alone. She started by:
- Building a wastewater treatment plant (even though costs rose by 20%)
- Raising worker wages above the minimum wage
- Providing scholarships to local fishermen's children
- Transparently reporting environmental, social, and financial performance every year

Investors initially protested because dividends fell. However, within two years, the company's reputation improved, customer loyalty grew, and the government provided tax incentives. The company survived while competitors went bankrupt due to pollution lawsuits.

One day, an employee discovered that the logistics department was still bribing port officials to speed up export permits. Sarah faced a dilemma: fire the highly valuable head of logistics or cover up the case. She chose to investigate and fire those involved in bribery, and then self‑reported to the authorities. This action cost the company a large contract in the short term, but saved its long‑term integrity.
""",
    "soal": [
        {"pertanyaan": "Sarah's decision to pursue not only profit but also care for the environment and community reflects the concept of Corporate Social ______.", "jawaban_benar": "Responsibility"},
        {"pertanyaan": "The parties affected by Sarah's decisions – such as workers, the river community, investors, and the government – are called ______.", "jawaban_benar": "stakeholders"},
        {"pertanyaan": "A report that includes economic, social, and environmental performance is known as a ______ bottom line report.", "jawaban_benar": "triple"},
        {"pertanyaan": "The principle of development that meets present needs without harming future generations is called ______.", "jawaban_benar": "sustainability"},
        {"pertanyaan": "The voluntary effort by PT EcoNusa to provide scholarships without legal pressure belongs to the ______ CSR level.", "jawaban_benar": "philanthropic"},
        {"pertanyaan": "Building a wastewater treatment plant despite higher costs is a form of responsibility toward the 'Planet' pillar, also known as ______ protection.", "jawaban_benar": "environment"},
        {"pertanyaan": "Raising worker wages reflects the 'People' pillar, which is about social ______ and well‑being.", "jawaban_benar": "equity"},
        {"pertanyaan": "The company's ability to remain economically viable in the long term without damaging the environment is called the '______' pillar.", "jawaban_benar": "Profit"},
        {"pertanyaan": "Sarah reported the bribery to authorities even though it hurt business temporarily. This shows the company supports the Sustainable Development Goals (______), especially Goal 16 on peace, justice, and strong institutions.", "jawaban_benar": "SDGs"},
        {"pertanyaan": "The argument that companies like PT EcoNusa have resources (money, technology, expertise) to solve social problems is called the ______ argument.", "jawaban_benar": "capacity"}
    ]
}
]

# =========================
# SESSION STATE
# =========================
if "submitted" not in st.session_state:
    st.session_state.submitted = False

def norm(x):
    return x.strip().lower() if x else ""

st.title("📘 CSR & Sustainability Quiz - Detailed Version")

score = 0
total = 0

for i, soal in enumerate(soal_list):
    st.markdown(f"### Question {i+1}")

    if soal["tipe"] == "pilihan_ganda":
        key = f"mc_{i}"
        st.radio(soal["pertanyaan"], soal["pilihan"], key=key, index=None)

        if st.session_state.submitted:
            total += 1
            user = st.session_state.get(key)
            if user == soal["jawaban_benar"]:
                score += 1
                st.success("✅ Correct")
            else:
                st.error(f"❌ Wrong. Correct answer: {soal['jawaban_benar']}")

    elif soal["tipe"] == "use_case_group":
        st.info(soal["bacaan"])
        for j, sub in enumerate(soal["soal"]):
            key = f"use_{i}_{j}"
            st.text_input(sub["pertanyaan"], key=key)

            if st.session_state.submitted:
                total += 1
                user = st.session_state.get(key, "")
                if norm(user) == norm(sub["jawaban_benar"]):
                    score += 1
                    st.success("✅ Correct")
                else:
                    st.error(f"❌ Wrong. Correct answer: {sub['jawaban_benar']}")

    st.markdown("---")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("🔍 Submit Answers", use_container_width=True):
        st.session_state.submitted = True
        st.rerun()

if st.session_state.submitted:
    percent = (score / total * 100)
    st.success(f"Your score: {score}/{total} ({percent:.1f}%)")

    with col2:
        if st.button("🔄 Reset Quiz", use_container_width=True):
            for k in list(st.session_state.keys()):
                if k.startswith(("mc_", "use_")):
                    del st.session_state[k]
            st.session_state.submitted = False
            st.rerun()