import streamlit as st

# ======================================================
# DATABASE SOAL (PILIHAN GANDA + ESAI) DENGAN PEMBAHASAN
# ======================================================
soal_list = [
    # ========== PILIHAN GANDA (1–40) ==========
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "1. Which of the following best represents a want rather than a need?",
        "pilihan": [
            "Feeling hungry after skipping lunch",
            "Needing water after exercise",
            "Choosing a premium coffee brand over others",
            "Wanting shelter during heavy rain",
            "Feeling tired and needing sleep"
        ],
        "jawaban_benar": "Choosing a premium coffee brand over others",
        "pembahasan": "**Pembahasan:** Want adalah keinginan yang dipengaruhi preferensi, seperti memilih merek tertentu, bukan kebutuhan dasar."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "2. A service differs from a product because it is _____.",
        "pilihan": [
            "tangible",
            "owned permanently",
            "produced in factories",
            "intangible",
            "easily stored"
        ],
        "jawaban_benar": "intangible",
        "pembahasan": "**Pembahasan:** Jasa bersifat tidak berwujud (intangible), berbeda dengan produk fisik."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "3. When consumers rely on shortcuts or simple rules to make decisions, they are using _____.",
        "pilihan": [
            "extended thinking",
            "heuristics",
            "perception bias",
            "cognitive dissonance",
            "motivation loops"
        ],
        "jawaban_benar": "heuristics",
        "pembahasan": "**Pembahasan:** Heuristics adalah aturan sederhana yang membantu pengambilan keputusan cepat."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "4. Which stage comes immediately after information search?",
        "pilihan": [
            "purchase decision",
            "problem recognition",
            "evaluation of alternatives",
            "post-purchase behaviour",
            "brand loyalty"
        ],
        "jawaban_benar": "evaluation of alternatives",
        "pembahasan": "**Pembahasan:** Setelah mencari informasi, konsumen mengevaluasi alternatif sebelum membeli."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "5. A consumer reading online reviews before buying a phone is engaging in _____.",
        "pilihan": [
            "internal search",
            "external search",
            "impulse buying",
            "routine decision",
            "post-purchase evaluation"
        ],
        "jawaban_benar": "external search",
        "pembahasan": "**Pembahasan:** External search melibatkan sumber luar seperti ulasan online."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "6. Cultural influences are best described as _____.",
        "pilihan": [
            "temporary trends",
            "individual habits",
            "deep-rooted values and norms",
            "company strategies",
            "random behaviours"
        ],
        "jawaban_benar": "deep-rooted values and norms",
        "pembahasan": "**Pembahasan:** Budaya membentuk nilai dasar dan norma yang memengaruhi perilaku."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "7. Which factor is most likely to influence brand preference?",
        "pilihan": [
            "weather patterns",
            "product benefits",
            "government policy",
            "factory size",
            "inventory systems"
        ],
        "jawaban_benar": "product benefits",
        "pembahasan": "**Pembahasan:** Manfaat produk sangat memengaruhi preferensi merek."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "8. Motivation is best defined as _____.",
        "pilihan": [
            "external pressure",
            "internal drive to satisfy needs",
            "market condition",
            "economic factor",
            "social influence"
        ],
        "jawaban_benar": "internal drive to satisfy needs",
        "pembahasan": "**Pembahasan:** Motivasi adalah dorongan internal untuk memenuhi kebutuhan."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "9. Perception refers to _____.",
        "pilihan": [
            "buying behaviour",
            "interpreting information",
            "pricing strategy",
            "production method",
            "sales promotion"
        ],
        "jawaban_benar": "interpreting information",
        "pembahasan": "**Pembahasan:** Persepsi adalah proses memilih dan menafsirkan informasi."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "10. Strategic planning helps organisations to _____.",
        "pilihan": [
            "focus only on short-term goals",
            "ignore competitors",
            "set long-term direction",
            "avoid decision-making",
            "reduce marketing efforts"
        ],
        "jawaban_benar": "set long-term direction",
        "pembahasan": "**Pembahasan:** Strategic planning menetapkan arah jangka panjang organisasi."
    },

    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "11. Which is NOT part of the marketing mix?",
        "pilihan": [
            "product",
            "price",
            "place",
            "promotion",
            "people"
        ],
        "jawaban_benar": "people",
        "pembahasan": "**Pembahasan:** 4P terdiri dari product, price, place, promotion."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "12. Market penetration involves _____.",
        "pilihan": [
            "new products in new markets",
            "existing products in existing markets",
            "new markets only",
            "diversification",
            "product replacement"
        ],
        "jawaban_benar": "existing products in existing markets",
        "pembahasan": "**Pembahasan:** Market penetration fokus pada produk lama di pasar lama."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "13. A strong brand helps to _____.",
        "pilihan": [
            "increase uncertainty",
            "reduce perceived risk",
            "limit customer choices",
            "increase production cost",
            "avoid competition"
        ],
        "jawaban_benar": "reduce perceived risk",
        "pembahasan": "**Pembahasan:** Brand kuat mengurangi risiko yang dirasakan konsumen."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "14. Post-purchase behaviour mainly involves _____.",
        "pilihan": [
            "product design",
            "customer satisfaction",
            "pricing decisions",
            "distribution planning",
            "promotion strategy"
        ],
        "jawaban_benar": "customer satisfaction",
        "pembahasan": "**Pembahasan:** Tahap ini mengevaluasi kepuasan setelah pembelian."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "15. A focus group is a method used in _____.",
        "pilihan": [
            "production",
            "marketing research",
            "distribution",
            "finance",
            "operations"
        ],
        "jawaban_benar": "marketing research",
        "pembahasan": "**Pembahasan:** Focus group digunakan untuk mengumpulkan insight konsumen."
    },

    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "16. Secondary data is _____.",
        "pilihan": [
            "collected first-hand",
            "collected for another purpose",
            "always more accurate",
            "expensive",
            "collected through experiments"
        ],
        "jawaban_benar": "collected for another purpose",
        "pembahasan": "**Pembahasan:** Data sekunder dikumpulkan untuk tujuan lain."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "17. Which is an example of primary data?",
        "pilihan": [
            "government reports",
            "industry statistics",
            "survey results",
            "published articles",
            "online databases"
        ],
        "jawaban_benar": "survey results",
        "pembahasan": "**Pembahasan:** Data primer dikumpulkan langsung melalui survei atau observasi."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "18. Extended problem solving occurs when _____.",
        "pilihan": [
            "buying routine items",
            "risk is low",
            "purchase is complex and expensive",
            "decision is automatic",
            "no information is needed"
        ],
        "jawaban_benar": "purchase is complex and expensive",
        "pembahasan": "**Pembahasan:** Extended problem solving terjadi untuk keputusan kompleks."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "19. Reference groups influence consumers through _____.",
        "pilihan": [
            "production",
            "pricing",
            "social pressure",
            "technology",
            "distribution"
        ],
        "jawaban_benar": "social pressure",
        "pembahasan": "**Pembahasan:** Reference group memengaruhi melalui tekanan sosial."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "20. Lifestyle refers to _____.",
        "pilihan": [
            "income only",
            "age only",
            "patterns of living",
            "education level",
            "occupation"
        ],
        "jawaban_benar": "patterns of living",
        "pembahasan": "**Pembahasan:** Lifestyle mencerminkan pola hidup seseorang."
    },

    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "21. Personality is _____.",
        "pilihan": [
            "temporary mood",
            "consistent characteristics",
            "external influence",
            "social class",
            "economic factor"
        ],
        "jawaban_benar": "consistent characteristics",
        "pembahasan": "**Pembahasan:** Personality adalah karakteristik psikologis yang konsisten."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "22. Social class is mainly determined by _____.",
        "pilihan": [
            "weather",
            "income and occupation",
            "location only",
            "product type",
            "brand choice"
        ],
        "jawaban_benar": "income and occupation",
        "pembahasan": "**Pembahasan:** Social class dipengaruhi pendapatan dan pekerjaan."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "23. Marketing intelligence focuses on _____.",
        "pilihan": [
            "internal data only",
            "external environment information",
            "production efficiency",
            "financial reports",
            "HR management"
        ],
        "jawaban_benar": "external environment information",
        "pembahasan": "**Pembahasan:** Marketing intelligence mengumpulkan info lingkungan eksternal."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "24. Diversification involves _____.",
        "pilihan": [
            "existing products only",
            "new products in new markets",
            "same market only",
            "price reduction",
            "cost leadership"
        ],
        "jawaban_benar": "new products in new markets",
        "pembahasan": "**Pembahasan:** Diversifikasi mencakup produk baru dan pasar baru."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "25. A mission statement defines _____.",
        "pilihan": [
            "daily tasks",
            "long-term purpose",
            "marketing budget",
            "sales targets",
            "production volume"
        ],
        "jawaban_benar": "long-term purpose",
        "pembahasan": "**Pembahasan:** Mission statement menjelaskan tujuan utama perusahaan."
    },

    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "26. Which is an example of situational influence?",
        "pilihan": [
            "culture",
            "family",
            "store atmosphere",
            "personality",
            "income"
        ],
        "jawaban_benar": "store atmosphere",
        "pembahasan": "**Pembahasan:** Situational influence seperti suasana toko."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "27. Consumer behaviour studies _____.",
        "pilihan": [
            "production methods",
            "employee performance",
            "how consumers make decisions",
            "supply chains",
            "financial systems"
        ],
        "jawaban_benar": "how consumers make decisions",
        "pembahasan": "**Pembahasan:** Fokus pada perilaku dan keputusan konsumen."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "28. Brand loyalty leads to _____.",
        "pilihan": [
            "switching brands often",
            "repeat purchases",
            "lower satisfaction",
            "higher risk",
            "less trust"
        ],
        "jawaban_benar": "repeat purchases",
        "pembahasan": "**Pembahasan:** Loyalitas merek meningkatkan pembelian ulang."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "29. Which factor affects purchasing power?",
        "pilihan": [
            "culture",
            "income",
            "beliefs",
            "attitudes",
            "lifestyle"
        ],
        "jawaban_benar": "income",
        "pembahasan": "**Pembahasan:** Income menentukan daya beli."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "30. Online reviews mainly affect _____.",
        "pilihan": [
            "production",
            "evaluation stage",
            "distribution",
            "pricing",
            "supply chain"
        ],
        "jawaban_benar": "evaluation stage",
        "pembahasan": "**Pembahasan:** Review membantu evaluasi alternatif."
    },

    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "31. Impulse buying occurs when _____.",
        "pilihan": [
            "planned carefully",
            "no emotion involved",
            "spontaneous decision",
            "high involvement",
            "long evaluation"
        ],
        "jawaban_benar": "spontaneous decision",
        "pembahasan": "**Pembahasan:** Impulse buying bersifat spontan."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "32. Customer satisfaction leads to _____.",
        "pilihan": [
            "complaints",
            "negative reviews",
            "loyalty",
            "reduced sales",
            "uncertainty"
        ],
        "jawaban_benar": "loyalty",
        "pembahasan": "**Pembahasan:** Kepuasan meningkatkan loyalitas."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "33. Which is part of psychological factors?",
        "pilihan": [
            "income",
            "culture",
            "motivation",
            "location",
            "age"
        ],
        "jawaban_benar": "motivation",
        "pembahasan": "**Pembahasan:** Motivasi adalah faktor psikologis."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "34. The main goal of marketing is _____.",
        "pilihan": [
            "maximise production",
            "satisfy customer needs",
            "reduce costs",
            "control employees",
            "increase inventory"
        ],
        "jawaban_benar": "satisfy customer needs",
        "pembahasan": "**Pembahasan:** Tujuan utama marketing adalah kepuasan pelanggan."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "35. Which stage identifies a need?",
        "pilihan": [
            "evaluation",
            "purchase",
            "problem recognition",
            "post-purchase",
            "search"
        ],
        "jawaban_benar": "problem recognition",
        "pembahasan": "**Pembahasan:** Tahap awal adalah pengenalan masalah."
    },

    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "36. Innovation in products helps to _____.",
        "pilihan": [
            "reduce demand",
            "increase competition",
            "meet changing needs",
            "limit growth",
            "avoid marketing"
        ],
        "jawaban_benar": "meet changing needs",
        "pembahasan": "**Pembahasan:** Inovasi membantu memenuhi kebutuhan yang berubah."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "37. Digital marketing mainly uses _____.",
        "pilihan": [
            "newspapers",
            "television",
            "internet platforms",
            "radio",
            "billboards"
        ],
        "jawaban_benar": "internet platforms",
        "pembahasan": "**Pembahasan:** Digital marketing memanfaatkan internet."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "38. A target market is _____.",
        "pilihan": [
            "all consumers",
            "selected group of buyers",
            "competitors",
            "suppliers",
            "employees"
        ],
        "jawaban_benar": "selected group of buyers",
        "pembahasan": "**Pembahasan:** Target market adalah kelompok konsumen tertentu."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "39. Segmentation divides the market based on _____.",
        "pilihan": [
            "random selection",
            "similar characteristics",
            "price only",
            "product type",
            "location only"
        ],
        "jawaban_benar": "similar characteristics",
        "pembahasan": "**Pembahasan:** Segmentasi berdasarkan karakteristik yang sama."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "40. Competitive advantage means _____.",
        "pilihan": [
            "higher costs",
            "unique value over competitors",
            "lower quality",
            "less innovation",
            "reduced marketing"
        ],
        "jawaban_benar": "unique value over competitors",
        "pembahasan": "**Pembahasan:** Keunggulan kompetitif adalah nilai unik dibanding pesaing."
    },

    # ========== ESAI (1–5) ==========
    {
        "tipe": "essai",
        "pertanyaan": "1. Explain the difference between needs, wants, and demands. Provide examples for each. (15 marks)",
        "jawaban_benar": "Needs basic, wants shaped, demands backed by buying power.",
        "pembahasan": "**Model jawaban:** Needs adalah kebutuhan dasar (makan), wants adalah keinginan (fast food), dan demands adalah wants yang didukung kemampuan beli."
    },
    {
        "tipe": "essai",
        "pertanyaan": "2. Describe the stages of the consumer decision-making process and give a real-life example. (15 marks)",
        "jawaban_benar": "5 stages process explained.",
        "pembahasan": "**Model jawaban:** Tahapan: problem recognition, information search, evaluation, purchase, post-purchase. Contoh: membeli smartphone."
    },
    {
        "tipe": "essai",
        "pertanyaan": "3. Discuss the role of culture and social factors in influencing consumer behaviour. (15 marks)",
        "jawaban_benar": "Culture shapes values, social influences behavior.",
        "pembahasan": "**Model jawaban:** Budaya membentuk nilai, faktor sosial seperti keluarga dan teman memengaruhi keputusan."
    },
    {
        "tipe": "essai",
        "pertanyaan": "4. Explain the importance of marketing research in business decision-making. (15 marks)",
        "jawaban_benar": "Provides data for decisions.",
        "pembahasan": "**Model jawaban:** Riset pemasaran membantu memahami pelanggan, mengurangi risiko, dan mendukung keputusan."
    },
    {
        "tipe": "essai",
        "pertanyaan": "5. Analyse how digital technology has changed consumer behaviour in modern markets. (15 marks)",
        "jawaban_benar": "Internet increases access, comparison, influence.",
        "pembahasan": "**Model jawaban:** Teknologi digital memudahkan akses informasi, perbandingan harga, dan pengaruh media sosial."
    }
]

# ======================================================
# INISIALISASI SESSION STATE
# ======================================================
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

# ======================================================
# TAMPILAN STREAMLIT
# ======================================================
st.set_page_config(page_title="MKTG 100 - Latihan Soal", layout="wide")
st.title("📚 MKTG 100 – Soal Latihan (Pilihan Ganda + Esai)")
st.markdown("---")

# Loop setiap soal
for i, soal in enumerate(soal_list):
    with st.container():
        st.markdown(f"**_Question {i+1}_**")
        st.markdown(soal["pertanyaan"])

        # Input berdasarkan tipe soal
        if soal["tipe"] == "pilihan_ganda":
            jawaban_user = st.radio(
                "Pilih jawaban:",
                options=soal["pilihan"],
                key=f"mc_{i}",
                index=None,
                label_visibility="collapsed"
            )
        else:  # essai
            jawaban_user = st.text_area(
                "Tulis jawaban Anda:",
                key=f"essay_{i}",
                height=150,
                placeholder="Tulis jawaban esai di sini...",
                label_visibility="collapsed"
            ).strip()

        # Jika sudah dicek, tampilkan feedback dan pembahasan
        if st.session_state.cek_dilakukan:
            # Feedback untuk pilihan ganda
            if soal["tipe"] == "pilihan_ganda":
                jawaban = st.session_state.get(f"mc_{i}")
                if jawaban is None:
                    jawaban = ""
                if jawaban == soal["jawaban_benar"]:
                    st.success("✅ Jawaban Anda benar!")
                else:
                    st.error(f"❌ Jawaban Anda salah. Jawaban yang benar: **{soal['jawaban_benar']}**")
            else:
                # Untuk esai, kita tidak memberikan penilaian otomatis
                st.info("Jawaban Anda telah dicatat. Bandingkan dengan pembahasan di bawah.")

            # Dropdown pembahasan (untuk semua tipe soal)
            with st.expander("📘 Lihat Pembahasan"):
                st.markdown(soal["pembahasan"])

        st.markdown("---")

# ======================================================
# TOMBOL CEK & RESET
# ======================================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔍 Cek Jawaban", use_container_width=True):
        st.session_state.cek_dilakukan = True
        st.rerun()

if st.session_state.cek_dilakukan:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Coba Lagi", use_container_width=True):
            # Hapus semua jawaban dari session state
            for key in list(st.session_state.keys()):
                if key.startswith("mc_") or key.startswith("essay_"):
                    del st.session_state[key]
            st.session_state.cek_dilakukan = False
            st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center;'>Selamat berlatih! 🌟</p>", unsafe_allow_html=True)