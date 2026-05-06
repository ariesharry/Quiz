import streamlit as st

soal_list = [

# =========================
# 15 PILIHAN GANDA (LEBIH DESKRIPTIF)
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Organisational culture is best defined as a system of shared values, beliefs, and behaviors that:",
    "pilihan": [
        "Only applies to top management decisions",
        "Guides how employees behave and interact within the organisation",
        "Focuses only on financial performance",
        "Is written formally in company policies only",
        "Changes daily based on individual preferences"
    ],
    "jawaban_benar": "Guides how employees behave and interact within the organisation"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The phrase 'the way we do things around here' refers to:",
    "pilihan": [
        "Formal procedures only",
        "Organisational culture",
        "Legal compliance",
        "Operational efficiency",
        "Strategic planning"
    ],
    "jawaban_benar": "Organisational culture"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A strong organisational culture is characterized by:",
    "pilihan": [
        "Unclear values and inconsistent behaviors",
        "Clearly defined norms and shared commitment",
        "Lack of employee engagement",
        "Strict rules without flexibility",
        "Frequent leadership changes"
    ],
    "jawaban_benar": "Clearly defined norms and shared commitment"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Norms within an organisation refer to:",
    "pilihan": [
        "Financial targets",
        "Standards of conduct that guide behavior",
        "Legal obligations",
        "Organisational hierarchy",
        "Employee contracts"
    ],
    "jawaban_benar": "Standards of conduct that guide behavior"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Visible organisational culture includes elements such as:",
    "pilihan": [
        "Values and beliefs only",
        "Office layout, dress code, and observable behaviors",
        "Employee attitudes only",
        "Internal motivations",
        "Personal goals"
    ],
    "jawaban_benar": "Office layout, dress code, and observable behaviors"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Invisible culture primarily refers to:",
    "pilihan": [
        "Company logos",
        "Physical office design",
        "Core values and underlying beliefs",
        "Dress code",
        "Organisational charts"
    ],
    "jawaban_benar": "Core values and underlying beliefs"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Symbols in organisational culture are important because they:",
    "pilihan": [
        "Only represent financial performance",
        "Convey meaning about relationships and interactions",
        "Are used only for marketing",
        "Replace leadership communication",
        "Eliminate the need for training"
    ],
    "jawaban_benar": "Convey meaning about relationships and interactions"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Stories in organisations are typically used to:",
    "pilihan": [
        "Replace formal training programs",
        "Communicate and reinforce organisational values",
        "Evaluate employee performance",
        "Reduce operational costs",
        "Manage finances"
    ],
    "jawaban_benar": "Communicate and reinforce organisational values"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Organisational heroes are individuals who:",
    "pilihan": [
        "Hold the highest position in the company",
        "Exemplify values and act as role models",
        "Focus only on profit generation",
        "Avoid risks completely",
        "Work independently from teams"
    ],
    "jawaban_benar": "Exemplify values and act as role models"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Rites and rituals within organisations are designed to:",
    "pilihan": [
        "Control employee behavior strictly",
        "Reinforce values and build social bonds",
        "Increase competition only",
        "Reduce communication",
        "Focus only on performance evaluation"
    ],
    "jawaban_benar": "Reinforce values and build social bonds"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A symbolic leader influences organisational culture by:",
    "pilihan": [
        "Ignoring daily activities",
        "Using symbols and articulating a clear vision",
        "Focusing only on financial results",
        "Avoiding communication",
        "Delegating all decisions"
    ],
    "jawaban_benar": "Using symbols and articulating a clear vision"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The phrase 'walking the talk' in cultural leadership means:",
    "pilihan": [
        "Giving instructions without action",
        "Aligning actions with stated values",
        "Avoiding difficult decisions",
        "Delegating responsibility",
        "Focusing on short-term goals"
    ],
    "jawaban_benar": "Aligning actions with stated values"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Organisations are considered social entities because:",
    "pilihan": [
        "They only focus on profits",
        "They consist of individuals working toward a common purpose",
        "They operate independently from people",
        "They are controlled by technology",
        "They do not require interaction"
    ],
    "jawaban_benar": "They consist of individuals working toward a common purpose"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Culture influences employee behavior primarily by:",
    "pilihan": [
        "Providing strict legal rules",
        "Shaping how individuals think and act",
        "Controlling salary structures",
        "Managing physical resources",
        "Eliminating diversity"
    ],
    "jawaban_benar": "Shaping how individuals think and act"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following best illustrates a cultural symbol?",
    "pilihan": [
        "Company financial report",
        "Dress code and office design",
        "Employee contracts",
        "Performance evaluation forms",
        "Production targets"
    ],
    "jawaban_benar": "Dress code and office design"
},

# =========================
# USE CASE (10 ISIAN - ANALYTICAL)
# =========================
{
    "tipe": "use_case_group",
    "bacaan": """
A technology company is trying to strengthen its organisational culture. Employees notice that the company promotes innovation and collaboration in its mission statement, but daily practices do not always reflect these values.

The office design is modern and open, encouraging communication, and employees are expected to dress casually. The company frequently shares stories about past employees who took risks and created successful products.

However, managers rarely reward innovative behavior, and decision-making is still centralized. Leaders often communicate the vision but do not consistently demonstrate it in their actions.

The company also holds monthly events and recognition programs, but employees feel that these activities are not aligned with real organizational practices.
""",
    "soal": [
        {"pertanyaan": "The mismatch between stated values and actions reflects weak ______.", "jawaban_benar": "culture"},
        {"pertanyaan": "Office design and dress code represent ______ culture.", "jawaban_benar": "visible"},
        {"pertanyaan": "Underlying values such as innovation belong to ______ culture.", "jawaban_benar": "invisible"},
        {"pertanyaan": "Stories about past employees are used to reinforce ______.", "jawaban_benar": "values"},
        {"pertanyaan": "Employees who take risks and succeed can be considered ______.", "jawaban_benar": "heroes"},
        {"pertanyaan": "Monthly events and recognition programs are examples of ______.", "jawaban_benar": "rituals"},
        {"pertanyaan": "Leaders not practicing what they say fail to ______ the talk.", "jawaban_benar": "walk"},
        {"pertanyaan": "Centralized decision-making may limit ______ culture.", "jawaban_benar": "innovative"},
        {"pertanyaan": "Symbols such as office layout help convey organizational ______.", "jawaban_benar": "meaning"},
        {"pertanyaan": "A leader who uses symbols and vision is called a ______ leader.", "jawaban_benar": "symbolic"}
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