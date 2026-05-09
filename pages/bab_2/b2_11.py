import streamlit as st

soal_list = [

# =========================
# 15 PILIHAN GANDA
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Services are primarily different from physical goods because services are mainly:",
    "pilihan": [
        "Stored in warehouses",
        "Mass produced",
        "Intangible in nature",
        "Easy to standardize",
        "Transferred through ownership"
    ],
    "jawaban_benar": "Intangible in nature"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following best describes a service?",
    "pilihan": [
        "A physical product that can be owned permanently",
        "An experience or performance offered to customers",
        "A tangible object stored for future use",
        "A manufactured item sold through retailers",
        "A product that requires no customer involvement"
    ],
    "jawaban_benar": "An experience or performance offered to customers"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The inability of services to be stored for future use is known as:",
    "pilihan": [
        "Intangibility",
        "Heterogeneity",
        "Perishability",
        "Inseparability",
        "Tangibility"
    ],
    "jawaban_benar": "Perishability"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A movie theater offering discounted tickets on weekdays is an example of managing:",
    "pilihan": [
        "Customer loyalty",
        "Perishability of services",
        "Physical evidence",
        "Employee productivity",
        "Brand positioning"
    ],
    "jawaban_benar": "Perishability of services"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The characteristic of services where production and consumption occur simultaneously is called:",
    "pilihan": [
        "Perishability",
        "Tangibility",
        "Inseparability",
        "Variability",
        "Durability"
    ],
    "jawaban_benar": "Inseparability"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Customers participating directly during service delivery illustrates:",
    "pilihan": [
        "Automation",
        "Mass production",
        "Co-creation",
        "Inventory control",
        "Product ownership"
    ],
    "jawaban_benar": "Co-creation"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Variation in service quality caused by human behavior is referred to as:",
    "pilihan": [
        "Tangibility",
        "Heterogeneity",
        "Perishability",
        "Standardization",
        "Positioning"
    ],
    "jawaban_benar": "Heterogeneity"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which strategy is commonly used to reduce service heterogeneity?",
    "pilihan": [
        "Increasing inventory",
        "Reducing customer interaction",
        "Employee training and standard procedures",
        "Eliminating branding",
        "Avoiding technology"
    ],
    "jawaban_benar": "Employee training and standard procedures"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Logos, uniforms, and interior design are examples of:",
    "pilihan": [
        "Reservation systems",
        "Flexible pricing",
        "Tangible cues",
        "Mass customization",
        "Distribution channels"
    ],
    "jawaban_benar": "Tangible cues"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The physical environment where a service transaction takes place is known as:",
    "pilihan": [
        "Value chain",
        "Servicescape",
        "Supply chain",
        "Touchpoint",
        "Benchmarking"
    ],
    "jawaban_benar": "Servicescape"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The traditional marketing mix consists of:",
    "pilihan": [
        "3Ps",
        "4Ps",
        "5Ps",
        "6Ps",
        "7Ps"
    ],
    "jawaban_benar": "4Ps"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is NOT part of the expanded 7Ps marketing mix?",
    "pilihan": [
        "People",
        "Processes",
        "Physical Evidence",
        "Product",
        "Productivity"
    ],
    "jawaban_benar": "Productivity"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Employees are considered important in services marketing because they:",
    "pilihan": [
        "Replace customers completely",
        "Act as the face of the company",
        "Eliminate service variability",
        "Control customer emotions entirely",
        "Reduce all operational costs"
    ],
    "jawaban_benar": "Act as the face of the company"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Music, scent, and lighting used to influence customer perceptions are known as:",
    "pilihan": [
        "Distribution systems",
        "Atmospherics",
        "Benchmarking tools",
        "Price indicators",
        "Market segmentation"
    ],
    "jawaban_benar": "Atmospherics"
},

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A customer journey map is mainly used to:",
    "pilihan": [
        "Measure employee salaries",
        "Track financial performance",
        "Understand customer experiences and touchpoints",
        "Reduce production costs",
        "Create inventory systems"
    ],
    "jawaban_benar": "Understand customer experiences and touchpoints"
},

# =========================
# USE CASE GROUP
# =========================

{
    "tipe": "use_case_group",
    "bacaan": """
A premium coffee shop chain is experiencing inconsistent customer satisfaction across its branches. 
Some customers praise the friendly staff and relaxing atmosphere, while others complain about slow service 
and differences in drink quality.

The company redesigned its stores with comfortable seating, calming music, and unique interior decoration 
to strengthen its brand image. Employees are trained to interact warmly with customers, and customers often 
customize their drink orders according to personal preferences.

During weekdays, customer demand is usually low, so the company offers promotional discounts in the afternoon. 
Management also introduced a mobile ordering application to speed up service delivery and reduce waiting times.

However, managers realize that service quality still depends heavily on employee performance at each branch.
""",

    "soal": [

        {
            "pertanyaan": "Differences in drink quality between branches illustrate service ______.",
            "jawaban_benar": "heterogeneity"
        },

        {
            "pertanyaan": "Comfortable seating, music, and decoration are part of the service ______.",
            "jawaban_benar": "servicescape"
        },

        {
            "pertanyaan": "Customers customizing their drink orders demonstrate ______ creation.",
            "jawaban_benar": "co"
        },

        {
            "pertanyaan": "Afternoon discounts are used to manage service ______.",
            "jawaban_benar": "perishability"
        },

        {
            "pertanyaan": "The inability to store unused service capacity is called ______.",
            "jawaban_benar": "perishability"
        },

        {
            "pertanyaan": "Employees interacting warmly with customers relate to the ______ variable.",
            "jawaban_benar": "people"
        },

        {
            "pertanyaan": "Music and interior design are examples of service ______.",
            "jawaban_benar": "atmospherics"
        },

        {
            "pertanyaan": "Mobile ordering applications help improve service ______.",
            "jawaban_benar": "processes"
        },

        {
            "pertanyaan": "Service quality depending on employees reflects service ______.",
            "jawaban_benar": "heterogeneity"
        },

        {
            "pertanyaan": "Customer interactions with the company throughout the experience are called customer ______.",
            "jawaban_benar": "journey"
        }

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

st.title("📘 Services Marketing Quiz")

score = 0
total = 0

for i, soal in enumerate(soal_list):

    st.markdown(f"### Question {i+1}")

    if soal["tipe"] == "pilihan_ganda":

        key = f"mc_{i}"

        st.radio(
            soal["pertanyaan"],
            soal["pilihan"],
            key=key,
            index=None
        )

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

            st.text_input(
                sub["pertanyaan"],
                key=key
            )

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