import streamlit as st

# =========================
# QUESTION DATA (REFACTORED - MORE DETAILED & LONGER)
# =========================
soal_list = [

# =========================
# 20 MULTIPLE CHOICE (ENRICHED WITH SCENARIOS)
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company is facing a situation where it could increase profits by manipulating financial reports, but that action would harm small shareholders. The manager chooses to remain honest even though profits are lower. Which principle best describes the manager's action?",
    "pilihan": [
        "Maximizing profit at any cost",
        "Applying moral principles in business decisions",
        "Ignoring stakeholders",
        "Following only the law",
        "Prioritizing personal gain"
    ],
    "jawaban_benar": "Applying moral principles in business decisions"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An employee at a factory discovers that the company is illegally dumping toxic waste into the river. He reports this finding to environmental authorities even though he knows he will be fired. This employee's action is known as:",
    "pilihan": [
        "Marketing activity",
        "Reporting unethical practices (whistleblowing)",
        "Employee recruitment process",
        "Selling illegal products",
        "Financial planning"
    ],
    "jawaban_benar": "Reporting unethical practices"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company leader consistently shows honesty, keeps promises, and does not engage in corruption even under pressure to cover up mistakes. The most prominent personal quality of this leader is:",
    "pilihan": [
        "Dishonesty",
        "Consistency in moral principles (integrity)",
        "Ignoring rules",
        "Avoiding responsibility",
        "Breaking laws"
    ],
    "jawaban_benar": "Consistency in moral principles"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In a board meeting, the CFO presents the actual data about the company's losses, including potential risks, without hiding any facts. This attitude reflects the principle of:",
    "pilihan": [
        "Hiding information",
        "Open communication (transparency)",
        "Avoiding responsibility",
        "Increasing profit by any means",
        "Overly controlling employees"
    ],
    "jawaban_benar": "Open communication"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "GreenLeaf Inc. voluntarily sets aside part of its profits to build city parks, recycle waste, and provide scholarships. These activities are a form of:",
    "pilihan": [
        "Corporate Social Responsibility (CSR)",
        "Company Sales Report",
        "Customer Service Role",
        "Corporate Strategy Rules",
        "Central System Regulation"
    ],
    "jawaban_benar": "Corporate Social Responsibility"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An accountant deliberately inflates revenue figures to make the financial statements look healthier and boost stock prices. Legally and ethically, this action is classified as:",
    "pilihan": [
        "Honest reporting",
        "Intentional deception (fraud)",
        "Financial transparency",
        "Legal compliance",
        "Ethical action"
    ],
    "jawaban_benar": "Intentional deception"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "After a product fails in the market, the product manager does not blame the team or external factors; instead, he acknowledges his own strategic mistake and accepts scrutiny. This attitude demonstrates the principle of:",
    "pilihan": [
        "Avoiding responsibility",
        "Taking responsibility (accountability)",
        "Ignoring outcomes",
        "Delegating tasks without control",
        "Maximizing profit"
    ],
    "jawaban_benar": "Taking responsibility"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In ethical decision-making, the approach that seeks to produce the greatest happiness for the greatest number of people is called:",
    "pilihan": [
        "Individual rights",
        "Maximizing overall benefits (utilitarianism)",
        "Legal rules",
        "Personal gain",
        "Cultural norms"
    ],
    "jawaban_benar": "Maximizing overall benefits"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A judge in a business case rules that each harmed party must receive fair compensation regardless of social status. This decision is based on an ethical theory that emphasizes:",
    "pilihan": [
        "Profit",
        "Fairness (justice)",
        "Speed of process",
        "Power",
        "Control"
    ],
    "jawaban_benar": "Fairness"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A procurement manager owns shares in a major supplier. When choosing a vendor, he tends to favor that supplier even though it charges higher prices. This situation is an example of:",
    "pilihan": [
        "Following rules properly",
        "Personal interests interfering with duties (conflict of interest)",
        "Reasonable profit increase",
        "Employee collaboration",
        "Customer satisfaction"
    ],
    "jawaban_benar": "Personal interests interfering with duties"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A CEO often speaks about integrity, but when a mistake occurs, he covers it up and fires the person who reported it. This type of leadership fails to demonstrate ethical leadership because the leader fails to:",
    "pilihan": [
        "Ignore employees",
        "Set a moral example",
        "Maximize profit",
        "Avoid risk",
        "Control staff rigidly"
    ],
    "jawaban_benar": "Set a moral example"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A timber company chooses to replant the trees it cuts, use renewable energy, and ensure its operations do not damage the ecosystem in the long term. This practice reflects the principle of:",
    "pilihan": [
        "Short-term gain",
        "Long-term balance (sustainability)",
        "Ignoring the environment",
        "Increasing waste",
        "Reducing ethics"
    ],
    "jawaban_benar": "Long-term balance"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "When a company builds a new factory, not only owners and employees are affected, but also the surrounding community, suppliers, consumers, and government. These groups collectively are called:",
    "pilihan": [
        "Only managers",
        "Anyone affected by the business (stakeholders)",
        "Only customers",
        "Only employees",
        "Only investors"
    ],
    "jawaban_benar": "Anyone affected by the business"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In one country, bribery is considered a normal way to expedite matters, while in another it is a serious crime. The ethical view that right or wrong depends on local cultural context is called:",
    "pilihan": [
        "Universal rules",
        "Context-based ethics (relativism)",
        "Strict law",
        "Profit focus",
        "No ethics"
    ],
    "jawaban_benar": "Context-based ethics"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company issues an official document containing values, principles, and rules of conduct that all employees must follow in daily decision-making. This document is called a:",
    "pilihan": [
        "Financial report",
        "Code of ethics",
        "Marketing plan",
        "Employment contract",
        "Activity schedule"
    ],
    "jawaban_benar": "Code of ethics"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A public official asks a contractor for money so that the contractor can win a government project tender. The act of giving money to influence a decision is legally called:",
    "pilihan": [
        "Ethical action",
        "Illegal incentive (bribery)",
        "Transparency",
        "Responsibility",
        "Fairness"
    ],
    "jawaban_benar": "Illegal incentive"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An e-commerce startup regularly publishes data about product defects, customer complaints, and its improvement processes openly on its website. This helps build long‑term relationships with customers. Trust is built through:",
    "pilihan": [
        "Deception",
        "Transparency",
        "Fraud",
        "Manipulation",
        "Bribery"
    ],
    "jawaban_benar": "Transparency"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In a negotiation, a businessperson considers only how to maximize their own profit, without caring whether the business partner gains or loses. The ethical approach behind this behavior is called:",
    "pilihan": [
        "Others' benefit",
        "Self-interest (egoism)",
        "Legal compliance",
        "Fairness",
        "Culture"
    ],
    "jawaban_benar": "Self-interest"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A manager faces two choices: lay off 50 employees to save the company from bankruptcy, or keep them and risk the entire company closing. Both options have serious moral consequences. This situation is called:",
    "pilihan": [
        "A clear answer",
        "Conflicting choices (ethical dilemma)",
        "No options at all",
        "Legal rules only",
        "No consequences"
    ],
    "jawaban_benar": "Conflicting choices"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "After an environmental pollution scandal is revealed, the company loses customers, investors withdraw funds, and its brand is perceived negatively. The most important factor for corporate reputation in the long term is:",
    "pilihan": [
        "Ethical behavior",
        "Office design",
        "Company location",
        "Logo",
        "Brand color"
    ],
    "jawaban_benar": "Ethical behavior"
},

# =========================
# USE CASE (10 FILL-IN-THE-BLANK) - ENRICHED STORY
# =========================
{
    "tipe": "use_case_group",
    "bacaan": """
David is a senior executive at the multinational company "GreenEnergy Inc.," which claims to be environmentally friendly and highly ethical. One day, David discovers strong evidence that over the past two years his company has committed two serious violations:

1. **Financial statement falsification** - Top management deliberately inflated revenues and hid huge losses from a failed renewable energy project. This was done to attract new investors and keep the stock price high.

2. **Secret toxic waste dumping** - Instead of recycling hazardous waste from production, the company hired an illegal operator to dump the waste into the river at night. The illegal dumping cost only one‑fifth of proper treatment.

Publicly, GreenEnergy Inc. aggressively campaigns about its environmental commitment, publishes sustainability reports full of green photos, and even received an award as "Most Ethical Company" last year.

If David reports his findings to authorities (such as the SEC or environmental agency), he could be fired, sued, or ostracized from the industry. But if he stays silent, the dishonest practices will continue to harm investors (who bought shares based on false reports) and the communities living near the polluted river.

David is deeply torn. On one hand, his family depends on his high salary. On the other hand, his conscience aches over the deception and environmental damage. He must choose between protecting his career or doing what is ethically right.
""",
    "soal": [
        {"pertanyaan": "The situation where David must choose between two options, both with serious moral consequences, is called an ethical ______.", "jawaban_benar": "dilemma"},
        {"pertanyaan": "David's act of reporting the company's violations to authorities even at his own expense is known as ______.", "jawaban_benar": "whistleblowing"},
        {"pertanyaan": "The practice of deliberately inflating revenues in financial reports falls under the category of ______.", "jawaban_benar": "fraud"},
        {"pertanyaan": "Dumping toxic waste into the river violates the company's ______ responsibility toward society and the environment.", "jawaban_benar": "social"},
        {"pertanyaan": "The concept that emphasizes long‑term balance between economic, social, and environmental factors is called ______.", "jawaban_benar": "sustainability"},
        {"pertanyaan": "The company hides the facts about waste dumping and false financial reports. The act of concealing the truth is called ______.", "jawaban_benar": "deception"},
        {"pertanyaan": "If David chooses to keep his job and remain silent for the sake of his high salary, he shows a lack of ______ (consistency between principles and actions).", "jawaban_benar": "integrity"},
        {"pertanyaan": "The ethical approach that would suggest David should report because it produces the greatest good for the greatest number of people (investors, the community) is called ______.", "jawaban_benar": "utilitarianism"},
        {"pertanyaan": "All parties affected by David's decision – such as investors, riverside communities, employees, and the government – are called ______.", "jawaban_benar": "stakeholders"},
        {"pertanyaan": "The ethical principle that requires harm from environmental pollution to be fairly compensated to victims is the principle of ______.", "jawaban_benar": "justice"}
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

st.title("📘 Business Ethics Quiz - Detailed Version")

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