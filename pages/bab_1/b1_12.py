import streamlit as st

soal_list = [

# =========================
# 15 PILIHAN GANDA
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Diversity refers to:",
    "pilihan": [
        "People having the same background",
        "All the ways in which people differ",
        "Only cultural differences",
        "Only gender differences",
        "Workplace rules"
    ],
    "jawaban_benar": "All the ways in which people differ"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Workplace diversity means:",
    "pilihan": [
        "Employees with similar skills",
        "A workforce with different human qualities",
        "Only experienced workers",
        "Only educated workers",
        "Same cultural background"
    ],
    "jawaban_benar": "A workforce with different human qualities"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Primary dimensions of diversity are:",
    "pilihan": [
        "Temporary traits",
        "Core elements shaping identity",
        "Job-related skills",
        "Company policies",
        "External environment"
    ],
    "jawaban_benar": "Core elements shaping identity"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Secondary dimensions of diversity are:",
    "pilihan": [
        "Fixed traits",
        "Cannot change",
        "Acquired or changeable traits",
        "Only biological traits",
        "Genetic traits"
    ],
    "jawaban_benar": "Acquired or changeable traits"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which is an example of primary dimension?",
    "pilihan": [
        "Education",
        "Work experience",
        "Age",
        "Income",
        "Job title"
    ],
    "jawaban_benar": "Age"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Prejudice means:",
    "pilihan": [
        "Acting fairly",
        "Assuming different = deficient",
        "Following rules",
        "Respecting diversity",
        "Equal treatment"
    ],
    "jawaban_benar": "Assuming different = deficient"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Discrimination is:",
    "pilihan": [
        "Thinking differently",
        "Acting on prejudice",
        "Ignoring differences",
        "Accepting diversity",
        "Equal treatment"
    ],
    "jawaban_benar": "Acting on prejudice"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Stereotypes are:",
    "pilihan": [
        "Facts about individuals",
        "Assumptions about a group",
        "Legal rules",
        "Company policies",
        "Cultural laws"
    ],
    "jawaban_benar": "Assumptions about a group"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Pay gap refers to:",
    "pilihan": [
        "Equal salary",
        "Difference in earnings between groups",
        "Bonus system",
        "Company profit",
        "Employee benefits"
    ],
    "jawaban_benar": "Difference in earnings between groups"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Equality means:",
    "pilihan": [
        "Giving same resources to everyone",
        "Giving based on needs",
        "Different treatment",
        "Special privileges",
        "Ignoring fairness"
    ],
    "jawaban_benar": "Giving same resources to everyone"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Equity means:",
    "pilihan": [
        "Same treatment for all",
        "Fair outcomes based on needs",
        "Ignoring differences",
        "Favoritism",
        "Equal salary"
    ],
    "jawaban_benar": "Fair outcomes based on needs"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Equity is different from special treatment because:",
    "pilihan": [
        "It is favoritism",
        "It focuses on fairness",
        "It ignores needs",
        "It is illegal",
        "It increases bias"
    ],
    "jawaban_benar": "It focuses on fairness"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Generational diversity refers to:",
    "pilihan": [
        "Same age group",
        "Different age cohorts",
        "Same culture",
        "Same education",
        "Same job role"
    ],
    "jawaban_benar": "Different age cohorts"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Different generations may have different:",
    "pilihan": [
        "Genes",
        "Motivations and communication styles",
        "Legal rights",
        "Salaries",
        "Work contracts"
    ],
    "jawaban_benar": "Motivations and communication styles"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Managers should:",
    "pilihan": [
        "Ignore differences",
        "Value diversity",
        "Avoid communication",
        "Apply bias",
        "Treat everyone identically"
    ],
    "jawaban_benar": "Value diversity"
},

# =========================
# USE CASE (10 ISIAN)
# =========================
{
    "tipe": "use_case_group",
    "bacaan": """
A company has employees from different ages, cultures, and backgrounds. However, some managers believe younger employees are less committed, while others think older employees are resistant to change.

In addition, the company provides the same resources to all employees, even those with different needs. For example, employees with disabilities do not receive special support, and new parents are not given flexible working arrangements.

Some employees also report unfair treatment in promotions and salary differences based on gender and ethnicity.

The organization is now facing issues related to bias, fairness, and inclusion.
""",
    "soal": [
        {"pertanyaan": "Assumptions about age groups are called ______.", "jawaban_benar": "stereotypes"},
        {"pertanyaan": "Treating people unfairly based on bias is ______.", "jawaban_benar": "discrimination"},
        {"pertanyaan": "Believing one group is inferior is ______.", "jawaban_benar": "prejudice"},
        {"pertanyaan": "Providing the same resources to all is ______.", "jawaban_benar": "equality"},
        {"pertanyaan": "Providing based on needs is ______.", "jawaban_benar": "equity"},
        {"pertanyaan": "Differences in salary between groups is called ______.", "jawaban_benar": "pay gap"},
        {"pertanyaan": "Different age groups represent ______ diversity.", "jawaban_benar": "generational"},
        {"pertanyaan": "Managers should ______ diversity.", "jawaban_benar": "value"},
        {"pertanyaan": "Fair outcomes require treating people ______.", "jawaban_benar": "differently"},
        {"pertanyaan": "Bias in workplace creates ______ issues.", "jawaban_benar": "diversity"}
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