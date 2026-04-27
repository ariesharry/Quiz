import streamlit as st

# ======================================================
# DATABASE SOAL (PILIHAN GANDA + ESAI) DENGAN PEMBAHASAN
# ======================================================
soal_list = [
    # ========== MULTIPLE CHOICE (1–20) ==========
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "1. A product is best defined as _____.",
        "pilihan": [
            "a physical object only",
            "anything that satisfies a need or want",
            "a service only",
            "a production process",
            "a marketing strategy"
        ],
        "jawaban_benar": "anything that satisfies a need or want",
        "pembahasan": "**Explanation:** A product includes goods, services, ideas, and more—anything that satisfies needs or wants."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "2. Which of the following is an example of an intangible product?",
        "pilihan": [
            "Laptop",
            "Car",
            "Consulting service",
            "Shoes",
            "Book"
        ],
        "jawaban_benar": "Consulting service",
        "pembahasan": "**Explanation:** Services are intangible because they cannot be physically touched."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "3. The core product focuses on _____.",
        "pilihan": [
            "design",
            "packaging",
            "brand name",
            "main benefit",
            "delivery"
        ],
        "jawaban_benar": "main benefit",
        "pembahasan": "**Explanation:** Core product is the fundamental benefit the customer seeks."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "4. Which level of product includes warranty and after-sales service?",
        "pilihan": [
            "Core product",
            "Actual product",
            "Augmented product",
            "Industrial product",
            "Convenience product"
        ],
        "jawaban_benar": "Augmented product",
        "pembahasan": "**Explanation:** Augmented product includes additional services like warranty and support."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "5. Product line refers to _____.",
        "pilihan": [
            "all products of a company",
            "a single product",
            "a group of related products",
            "a brand strategy",
            "a pricing method"
        ],
        "jawaban_benar": "a group of related products",
        "pembahasan": "**Explanation:** A product line is a set of related products."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "6. Product mix width refers to _____.",
        "pilihan": [
            "number of items",
            "number of product lines",
            "product quality",
            "brand strength",
            "price level"
        ],
        "jawaban_benar": "number of product lines",
        "pembahasan": "**Explanation:** Width measures how many product lines a company has."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "7. Convenience products are usually _____.",
        "pilihan": [
            "expensive",
            "rarely purchased",
            "frequently purchased",
            "high involvement",
            "customized"
        ],
        "jawaban_benar": "frequently purchased",
        "pembahasan": "**Explanation:** Convenience products are bought often with minimal effort."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "8. Specialty products are characterized by _____.",
        "pilihan": [
            "low price",
            "high availability",
            "unique characteristics",
            "frequent purchase",
            "low involvement"
        ],
        "jawaban_benar": "unique characteristics",
        "pembahasan": "**Explanation:** Specialty products are unique and require special effort to obtain."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "9. Raw materials are classified as _____.",
        "pilihan": [
            "consumer products",
            "B2B products",
            "services",
            "ideas",
            "experiences"
        ],
        "jawaban_benar": "B2B products",
        "pembahasan": "**Explanation:** Raw materials are used by businesses, not end consumers."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "10. A brand is best described as _____.",
        "pilihan": [
            "a price tag",
            "a product design",
            "a symbol or name identifying a product",
            "a distribution channel",
            "a manufacturing process"
        ],
        "jawaban_benar": "a symbol or name identifying a product",
        "pembahasan": "**Explanation:** A brand differentiates a product from competitors."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "11. Brand equity refers to _____.",
        "pilihan": [
            "production cost",
            "brand value",
            "distribution level",
            "inventory size",
            "sales volume"
        ],
        "jawaban_benar": "brand value",
        "pembahasan": "**Explanation:** Brand equity is the value a brand adds to a product."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "12. Which branding strategy uses the same brand for multiple products?",
        "pilihan": [
            "Individual branding",
            "Family branding",
            "Private branding",
            "Co-branding",
            "Licensed branding"
        ],
        "jawaban_benar": "Family branding",
        "pembahasan": "**Explanation:** Family branding applies one brand across multiple products."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "13. Packaging primarily serves to _____.",
        "pilihan": [
            "increase cost",
            "protect and promote the product",
            "replace branding",
            "reduce quality",
            "eliminate competition"
        ],
        "jawaban_benar": "protect and promote the product",
        "pembahasan": "**Explanation:** Packaging both protects and markets the product."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "14. The introduction stage of PLC is characterized by _____.",
        "pilihan": [
            "high profits",
            "rapid growth",
            "slow sales",
            "declining demand",
            "market saturation"
        ],
        "jawaban_benar": "slow sales",
        "pembahasan": "**Explanation:** Sales are low in the introduction stage."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "15. The growth stage focuses on _____.",
        "pilihan": [
            "market exit",
            "brand loyalty",
            "product removal",
            "cost cutting",
            "decline"
        ],
        "jawaban_benar": "brand loyalty",
        "pembahasan": "**Explanation:** Growth stage builds loyalty and expands the market."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "16. The maturity stage is characterized by _____.",
        "pilihan": [
            "rapid growth",
            "declining sales",
            "peak sales",
            "no competition",
            "product launch"
        ],
        "jawaban_benar": "peak sales",
        "pembahasan": "**Explanation:** Sales reach their highest point in maturity."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "17. Decline stage occurs when _____.",
        "pilihan": [
            "sales increase",
            "profits rise",
            "sales and profits fall",
            "competition disappears",
            "new markets open"
        ],
        "jawaban_benar": "sales and profits fall",
        "pembahasan": "**Explanation:** Decline stage shows decreasing demand and profits."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "18. Market penetration aims to _____.",
        "pilihan": [
            "enter new markets",
            "increase usage in existing markets",
            "launch new products",
            "reduce price only",
            "exit market"
        ],
        "jawaban_benar": "increase usage in existing markets",
        "pembahasan": "**Explanation:** It focuses on selling more to current customers."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "19. Product modification includes _____.",
        "pilihan": [
            "price changes only",
            "feature improvement",
            "distribution expansion",
            "market exit",
            "branding removal"
        ],
        "jawaban_benar": "feature improvement",
        "pembahasan": "**Explanation:** Product modification improves features, quality, or style."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "20. New product development is important due to _____.",
        "pilihan": [
            "stable markets",
            "no competition",
            "changing consumer needs",
            "reduced technology",
            "fixed demand"
        ],
        "jawaban_benar": "changing consumer needs",
        "pembahasan": "**Explanation:** Markets evolve, requiring continuous innovation."
    },

    # ========== SHORT ANSWER (21–30) ==========
    {
        "tipe": "isian_singkat",
        "pertanyaan": "21. Define a product in marketing.",
        "jawaban_benar": "Anything that satisfies needs or wants",
        "pembahasan": "**Explanation:** Product includes goods, services, ideas, etc."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "22. What is the core product?",
        "jawaban_benar": "Main benefit",
        "pembahasan": "**Explanation:** It is the fundamental value offered."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "23. Give one example of a service product.",
        "jawaban_benar": "Consulting",
        "pembahasan": "**Explanation:** Services are intangible offerings."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "24. What does PLC stand for?",
        "jawaban_benar": "Product Life Cycle",
        "pembahasan": "**Explanation:** Refers to stages of product over time."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "25. Name one stage of PLC.",
        "jawaban_benar": "Growth",
        "pembahasan": "**Explanation:** Other stages include introduction, maturity, decline."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "26. What is brand equity?",
        "jawaban_benar": "Brand value",
        "pembahasan": "**Explanation:** Value a brand adds to a product."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "27. What does packaging primarily do?",
        "jawaban_benar": "Protect product",
        "pembahasan": "**Explanation:** Also helps promotion and usability."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "28. What is a product line?",
        "jawaban_benar": "Group of related products",
        "pembahasan": "**Explanation:** Products with similar characteristics."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "29. What type of product is bought frequently with low effort?",
        "jawaban_benar": "Convenience product",
        "pembahasan": "**Explanation:** These require minimal decision-making."
    },
    {
        "tipe": "isian_singkat",
        "pertanyaan": "30. What drives new product development?",
        "jawaban_benar": "Changing needs",
        "pembahasan": "**Explanation:** Also competition and technology changes."
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