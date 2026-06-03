import streamlit as st

soal_list = [

# =========================
# 15 MULTIPLE CHOICE QUESTIONS
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "International Business (IB) is best defined as:",
    "pilihan": [
        "Selling products only within one country",
        "Managing local employees",
        "Trading goods, services, technology, capital, or knowledge across national boundaries",
        "Importing products only",
        "International tourism activities"
    ],
    "jawaban_benar": "Trading goods, services, technology, capital, or knowledge across national boundaries"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which motive encourages firms to seek new customers and increase market share abroad?",
    "pilihan": [
        "Efficiency-seeking motive",
        "Resource-seeking motive",
        "Market-seeking motive",
        "Political motive",
        "Tax-seeking motive"
    ],
    "jawaban_benar": "Market-seeking motive"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company expanding overseas to access raw materials is pursuing:",
    "pilihan": [
        "Market-seeking motives",
        "Resource-seeking motives",
        "Cultural motives",
        "Promotional motives",
        "Domestic motives"
    ],
    "jawaban_benar": "Resource-seeking motives"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is NOT one of the three key considerations for international business?",
    "pilihan": [
        "Legal-Political Environment",
        "Economic Environment",
        "Cultural Environment",
        "Technological Environment",
        "None of the above"
    ],
    "jawaban_benar": "Technological Environment"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Companies operating internationally must comply with:",
    "pilihan": [
        "Only home-country laws",
        "Only international laws",
        "The laws of each country in which they operate",
        "UN regulations only",
        "Industry standards only"
    ],
    "jawaban_benar": "The laws of each country in which they operate"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Infrastructure such as transport, logistics, internet, and energy systems belongs to which environment?",
    "pilihan": [
        "Legal-Political Environment",
        "Economic Environment",
        "Cultural Environment",
        "Marketing Environment",
        "Technological Environment"
    ],
    "jawaban_benar": "Economic Environment"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Ethnocentrism refers to:",
    "pilihan": [
        "Adapting to foreign cultures",
        "Learning multiple languages",
        "Viewing one's own culture as superior to others",
        "Avoiding international business",
        "Supporting cultural diversity"
    ],
    "jawaban_benar": "Viewing one's own culture as superior to others"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Cultural shock is best described as:",
    "pilihan": [
        "Excitement about a new country",
        "Confusion and discomfort in an unfamiliar culture",
        "Cultural superiority",
        "Political disagreement",
        "Economic instability"
    ],
    "jawaban_benar": "Confusion and discomfort in an unfamiliar culture"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "According to Hofstede, power distance refers to:",
    "pilihan": [
        "Differences in income",
        "Acceptance of unequal distribution of power",
        "Differences in education",
        "Distance between countries",
        "Differences in language"
    ],
    "jawaban_benar": "Acceptance of unequal distribution of power"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which Hofstede dimension measures how a society tolerates risk and uncertainty?",
    "pilihan": [
        "Power Distance",
        "Achievement-Nurturing",
        "Individualism-Collectivism",
        "Uncertainty Avoidance",
        "Time Orientation"
    ],
    "jawaban_benar": "Uncertainty Avoidance"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Marketing Mix traditionally consists of:",
    "pilihan": [
        "Product, Price, Promotion, Place",
        "People, Profit, Planning, Product",
        "Price, Process, Policy, Place",
        "Promotion, Planning, Production, Profit",
        "Product, Performance, Profit, Position"
    ],
    "jawaban_benar": "Product, Price, Promotion, Place"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Labelling requirements and product safety standards are examples of:",
    "pilihan": [
        "Economic considerations",
        "Cultural considerations",
        "Legal considerations",
        "Promotional considerations",
        "Consumer considerations"
    ],
    "jawaban_benar": "Legal considerations"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which pricing strategy maintains consistency and brand control across countries?",
    "pilihan": [
        "Adapted pricing",
        "Cost-plus pricing",
        "Standardized pricing",
        "Discount pricing",
        "Penetration pricing"
    ],
    "jawaban_benar": "Standardized pricing"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Adapted pricing is characterized by:",
    "pilihan": [
        "Using identical prices everywhere",
        "Government-controlled pricing",
        "Pricing flexibility based on local conditions",
        "Ignoring cultural factors",
        "Fixed profit margins"
    ],
    "jawaban_benar": "Pricing flexibility based on local conditions"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The promotional mix refers to:",
    "pilihan": [
        "Methods used to manufacture products",
        "Mechanisms managers use to communicate with customers",
        "Ways of distributing products",
        "International trade agreements",
        "Methods of employee training"
    ],
    "jawaban_benar": "Mechanisms managers use to communicate with customers"
},

# =========================
# USE CASE (10 SHORT ANSWER QUESTIONS)
# =========================
{
    "tipe": "use_case_group",
    "bacaan": """
A New Zealand beverage company plans to expand into several Asian markets.
Management hopes to increase market share and gain access to new customers.

Before entering the new markets, managers study the legal-political, economic,
and cultural environments. They review product labelling requirements,
consumer purchasing power, and local cultural preferences.

The company wants to maintain a consistent global brand image but may adjust
prices according to local market conditions. Marketing managers are also
designing promotional campaigns that match local cultural values.

To improve international success, the company creates a culturally diverse
management team and trains employees to avoid ethnocentric thinking.
""",
    "soal": [
        {
            "pertanyaan": "Expanding to gain new customers reflects a ______-seeking motive.",
            "jawaban_benar": "market"
        },
        {
            "pertanyaan": "Product labelling requirements are a ______ consideration.",
            "jawaban_benar": "legal"
        },
        {
            "pertanyaan": "Purchasing power is part of the ______ environment.",
            "jawaban_benar": "economic"
        },
        {
            "pertanyaan": "Local values and preferences belong to the ______ environment.",
            "jawaban_benar": "cultural"
        },
        {
            "pertanyaan": "Viewing one's own culture as superior is called ______.",
            "jawaban_benar": "ethnocentrism"
        },
        {
            "pertanyaan": "A globally consistent pricing approach is called ______ pricing.",
            "jawaban_benar": "standardized"
        },
        {
            "pertanyaan": "Flexible pricing based on local conditions is called ______ pricing.",
            "jawaban_benar": "adapted"
        },
        {
            "pertanyaan": "Product, price, promotion, and place make up the marketing ______.",
            "jawaban_benar": "mix"
        },
        {
            "pertanyaan": "Communication tools used to reach customers are part of ______.",
            "jawaban_benar": "promotion"
        },
        {
            "pertanyaan": "A management team with members from different cultures is considered culturally ______.",
            "jawaban_benar": "diverse"
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