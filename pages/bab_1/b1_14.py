import streamlit as st

soal_list = [

# =========================
# 15 MULTIPLE CHOICE QUESTIONS
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Manufacturing organisations are primarily characterized by:",
    "pilihan": [
        "Producing non-physical services only",
        "Simultaneous production and consumption",
        "Producing physical goods that can be stored",
        "Customer participation in production",
        "Highly customized outputs only"
    ],
    "jawaban_benar": "Producing physical goods that can be stored"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is an example of a service organisation?",
    "pilihan": [
        "Furniture factory",
        "Chocolate manufacturer",
        "University education",
        "Steel production company",
        "Lego manufacturing"
    ],
    "jawaban_benar": "University education"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Operations Management (OM) is best defined as:",
    "pilihan": [
        "Managing only financial resources",
        "The process of advertising products",
        "The set of processes that transforms inputs into outputs",
        "A method used only in manufacturing firms",
        "A strategy for reducing taxes"
    ],
    "jawaban_benar": "The set of processes that transforms inputs into outputs"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is considered an input in the operations value chain?",
    "pilihan": [
        "Finished products",
        "Customers",
        "Raw materials",
        "Sales revenue",
        "Market share"
    ],
    "jawaban_benar": "Raw materials"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A competitive strategy focused on offering unique products or services is called:",
    "pilihan": [
        "Low-cost strategy",
        "Rapid response strategy",
        "Differentiation strategy",
        "Inventory strategy",
        "Automation strategy"
    ],
    "jawaban_benar": "Differentiation strategy"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Process layout is most suitable for:",
    "pilihan": [
        "High-volume standardized production",
        "Low-volume and high-variety production",
        "Continuous production only",
        "Fast-food restaurants",
        "Mass production of identical products"
    ],
    "jawaban_benar": "Low-volume and high-variety production"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which layout keeps the product in one location while workers and equipment move to it?",
    "pilihan": [
        "Product layout",
        "Cellular layout",
        "Process layout",
        "Fixed-position layout",
        "Assembly layout"
    ],
    "jawaban_benar": "Fixed-position layout"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Product layout is most effective when:",
    "pilihan": [
        "Product demand is low and irregular",
        "Products are highly customized",
        "Production volume is high and standardized",
        "Machines are grouped by function",
        "The product cannot be moved"
    ],
    "jawaban_benar": "Production volume is high and standardized"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Supply chain management focuses on:",
    "pilihan": [
        "Managing employee salaries",
        "Managing the sequence from suppliers to final customers",
        "Designing marketing campaigns",
        "Reducing taxes and legal costs",
        "Managing only transportation"
    ],
    "jawaban_benar": "Managing the sequence from suppliers to final customers"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Vertical integration refers to:",
    "pilihan": [
        "Grouping employees into teams",
        "Buying competitors in the same industry",
        "Producing goods previously purchased or buying suppliers/distributors",
        "Reducing inventory levels",
        "Increasing product prices"
    ],
    "jawaban_benar": "Producing goods previously purchased or buying suppliers/distributors"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Productivity is calculated using the formula:",
    "pilihan": [
        "Inputs / Outputs",
        "Outputs × Inputs",
        "Outputs / Inputs",
        "Revenue / Costs",
        "Profit / Employees"
    ],
    "jawaban_benar": "Outputs / Inputs"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Single-factor productivity compares outputs with:",
    "pilihan": [
        "Multiple combined inputs",
        "Only financial performance",
        "A single input such as labour hours",
        "Customer satisfaction",
        "Market demand"
    ],
    "jawaban_benar": "A single input such as labour hours"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which type of inventory includes partially completed products?",
    "pilihan": [
        "Raw materials",
        "Finished goods",
        "MRO inventory",
        "Work-in-progress inventory",
        "Buffer inventory"
    ],
    "jawaban_benar": "Work-in-progress inventory"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Just-in-time (JIT) inventory aims to:",
    "pilihan": [
        "Increase storage costs",
        "Keep large amounts of inventory",
        "Reduce the time inventory sits in storage",
        "Eliminate customer demand",
        "Maximize paperwork"
    ],
    "jawaban_benar": "Reduce the time inventory sits in storage"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Technology and automation improve operations primarily through:",
    "pilihan": [
        "Reducing communication",
        "Increasing manual work",
        "Improving speed, flexibility, quality, and efficiency",
        "Eliminating supply chains",
        "Reducing customer value"
    ],
    "jawaban_benar": "Improving speed, flexibility, quality, and efficiency"
},

# =========================
# USE CASE (10 SHORT ANSWER QUESTIONS)
# =========================
{
    "tipe": "use_case_group",
    "bacaan": """
A furniture manufacturing company is reviewing its operations and supply chain strategy. 
The company produces customized furniture products and groups machines according to their functions. 
Managers are trying to improve productivity while reducing unnecessary inventory costs.

The company purchases timber and raw materials from suppliers and stores partially completed furniture products in the factory. 
To improve efficiency, the company plans to adopt technology and automation systems. 

Management is also considering a rapid response strategy to deliver products faster to customers. 
The operations manager evaluates whether the company’s processes add customer value and support competitive advantage.

The company wants to maintain lower inventory levels using just-in-time practices while improving coordination with suppliers across the supply chain.
""",
    "soal": [
        {"pertanyaan": "The company described is primarily a ______ organisation.", "jawaban_benar": "manufacturing"},
        {"pertanyaan": "Grouping machines by similar functions is called a ______ layout.", "jawaban_benar": "process"},
        {"pertanyaan": "Timber used in production is classified as ______ materials.", "jawaban_benar": "raw"},
        {"pertanyaan": "Partially completed furniture products are called work-in-______ inventory.", "jawaban_benar": "progress"},
        {"pertanyaan": "The formula for productivity is outputs divided by ______.", "jawaban_benar": "inputs"},
        {"pertanyaan": "A strategy focused on fast delivery is called rapid ______.", "jawaban_benar": "response"},
        {"pertanyaan": "Just-in-time inventory aims to reduce storage ______.", "jawaban_benar": "time"},
        {"pertanyaan": "The sequence from suppliers to customers is called the supply ______.", "jawaban_benar": "chain"},
        {"pertanyaan": "Technology and automation improve operational ______.", "jawaban_benar": "efficiency"},
        {"pertanyaan": "Processes should maximize customer ______.", "jawaban_benar": "value"}
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

st.title("📘 Operations & Supply Chain Management Quiz")

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