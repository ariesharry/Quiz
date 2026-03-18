import streamlit as st

# ======================================================
# DATABASE SOAL (PILIHAN GANDA + ESAI) DENGAN PEMBAHASAN
# ======================================================
soal_list = [
    # ========== PILIHAN GANDA (1–27) ==========
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "1. Which of the following is an example of a need?",
        "pilihan": [
            "Even though there are many types of flour on the market, Brenda will buy only the Gold Medal brand when she decides to bake.",
            "Although she claims to be thirsty, Joanna will not buy a soda from this vending machine because it does not contain any Diet Coke.",
            "Adam realises he is hungry.",
            "Marilyn decides she would like to have a McDonald’s milkshake.",
            "Michael will only go to a movie if Ashton Kutcher is the lead actor."
        ],
        "jawaban_benar": "Adam realises he is hungry.",
        "pembahasan": "**Pembahasan:** Kebutuhan (need) adalah keadaan dasar yang dirasakan seseorang, seperti lapar, haus, atau rasa aman. Pilihan C (Adam menyadari bahwa dia lapar) adalah contoh kebutuhan. Pilihan lain merupakan contoh keinginan (want) yang dipengaruhi oleh preferensi pribadi atau merek."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "2. A _____ delivers a benefit when it satisfies a _____.",
        "pilihan": [
            "product; demand",
            "company; competitor",
            "service; utility",
            "product; need or want",
            "marketplace; marketer"
        ],
        "jawaban_benar": "product; need or want",
        "pembahasan": "**Pembahasan:** Produk (barang atau jasa) memberikan manfaat ketika memenuhi kebutuhan atau keinginan konsumen. Konsep ini merupakan inti dari pemasaran."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "3. If a product is expensive, complex or the outcome of use is uncertain the consumer may experience _____.",
        "pilihan": [
            "perceived risk",
            "reference group pressure",
            "social class pressure",
            "heuristic confusion",
            "lifestyle inconsistencies"
        ],
        "jawaban_benar": "perceived risk",
        "pembahasan": "**Pembahasan:** Risiko yang dirasakan (perceived risk) adalah kekhawatiran konsumen atas konsekuensi pembelian yang tidak diinginkan, misalnya karena harga tinggi, kompleksitas produk, atau ketidakpastian hasil."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "4. Arrange the following steps in the order in which they occur in the consumer decision-making process.\n1. evaluation of alternatives\n2. post-purchase evaluation\n3. problem recognition\n4. Purchase\n5. information search",
        "pilihan": [
            "3; 2; 1; 4; 5",
            "5; 3; 1; 2; 4",
            "3; 5; 1; 4; 2",
            "1; 2; 3; 4; 5",
            "1; 3; 5; 4; 2"
        ],
        "jawaban_benar": "3; 5; 1; 4; 2",
        "pembahasan": "**Pembahasan:** Urutan yang benar dalam proses keputusan konsumen: 3) pengenalan masalah, 5) pencarian informasi, 1) evaluasi alternatif, 4) pembelian, 2) evaluasi pasca pembelian."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "5. When Anna was invited to go skiing she realised she needed a much warmer coat than her current coat. Anna was in which stage of the decision-making process?",
        "pilihan": [
            "product evaluation",
            "situational analysis",
            "problem recognition",
            "problem screening",
            "information search"
        ],
        "jawaban_benar": "problem recognition",
        "pembahasan": "**Pembahasan:** Anna menyadari bahwa mantelnya tidak cukup hangat untuk ski – ini adalah pengenalan masalah (problem recognition), yaitu tahap pertama di mana konsumen merasakan perbedaan antara keadaan aktual dan yang diinginkan."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "6. A consumer gathers information, identifies a small number of products and then narrows down the choice by comparing the pros and cons of each product. This consumer is experiencing the _____ step of the consumer decision process.",
        "pilihan": [
            "problem recognition",
            "information search",
            "evaluation of alternatives",
            "product choice",
            "post-purchase evaluation"
        ],
        "jawaban_benar": "evaluation of alternatives",
        "pembahasan": "**Pembahasan:** Setelah mencari informasi, konsumen mengevaluasi alternatif dengan membandingkan kelebihan dan kekurangan setiap produk sebelum memutuskan pembelian."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "7. In the model of buyer behaviour, which of the following is NOT a major type of force or event in the buyer’s environment?",
        "pilihan": [
            "economic",
            "channels",
            "political",
            "technological",
            "cultural"
        ],
        "jawaban_benar": "channels",
        "pembahasan": "**Pembahasan:** Kekuatan utama dalam lingkungan pembeli meliputi ekonomi, politik, teknologi, dan budaya. 'Channels' (saluran distribusi) bukan bagian dari lingkungan makro, melainkan bagian dari strategi pemasaran."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "8. Maslow’s hierarchy of needs _____.",
        "pilihan": [
            "examines six levels of motivation",
            "suggests a person cannot move to the next level until previous need levels are satisfied",
            "suggests that love and friendship fulfil safety needs",
            "culminates in the need for belonging",
            "suggests that consumers start by first satisfying ego needs"
        ],
        "jawaban_benar": "suggests a person cannot move to the next level until previous need levels are satisfied",
        "pembahasan": "**Pembahasan:** Hierarki kebutuhan Maslow menyatakan bahwa kebutuhan tingkat rendah (fisiologis, keamanan) harus dipenuhi sebelum seseorang termotivasi oleh kebutuhan tingkat lebih tinggi (sosial, penghargaan, aktualisasi diri)."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "9. Learning is _____.",
        "pilihan": [
            "an internal state that drives us to satisfy need",
            "the process by which people select, organise and interpret information from the outside world",
            "a change in behaviour caused by information or experience",
            "a lasting evaluation of a person, object or issue",
            "the set of unique psychological characteristics that consistently influence the way a person responds to situations in the environment"
        ],
        "jawaban_benar": "a change in behaviour caused by information or experience",
        "pembahasan": "**Pembahasan:** Pembelajaran (learning) adalah perubahan perilaku yang relatif permanen sebagai akibat dari pengalaman atau informasi. Definisi lain: motivasi (A), persepsi (B), sikap (D), kepribadian (E)."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "10. Strategic business planning _____.",
        "pilihan": [
            "will cause management to deal with only current planning issues",
            "will be based only on the economy of the world",
            "should identify and build on the firm’s strengths, and it helps managers at all levels make informed decisions",
            "is only necessary in large organisations",
            "is used only when facing difficult decisions"
        ],
        "jawaban_benar": "should identify and build on the firm’s strengths, and it helps managers at all levels make informed decisions",
        "pembahasan": "**Pembahasan:** Perencanaan bisnis strategis bertujuan mengidentifikasi kekuatan perusahaan dan membantu manajer membuat keputusan berdasarkan informasi. Ini penting untuk semua organisasi, tidak hanya saat sulit atau besar."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "11. Which of the following would NOT be a part of a marketing plan?",
        "pilihan": [
            "description of the marketing environment",
            "outline of marketing strategies",
            "details as to how marketing strategies will be implemented",
            "assurances the firm has a strong monopoly in the industry",
            "details as to how marketing strategies will be monitored and controlled"
        ],
        "jawaban_benar": "assurances the firm has a strong monopoly in the industry",
        "pembahasan": "**Pembahasan:** Rencana pemasaran mencakup analisis lingkungan, strategi, implementasi, dan pengendalian. Jaminan monopoli tidak realistis dan bukan bagian dari rencana pemasaran."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "12. A marketing manager sets the objective of gaining a 20% share of the market and introducing three new products over the coming year. This objective would be part of a _____.",
        "pilihan": [
            "operational analysis",
            "macro-strategic plan",
            "overall strategic implementation plan",
            "tactical implementation plan",
            "functional plan"
        ],
        "jawaban_benar": "functional plan",
        "pembahasan": "**Pembahasan:** Tujuan yang spesifik untuk fungsi pemasaran (pangsa pasar, produk baru) termasuk dalam rencana fungsional (functional plan), yang merupakan bagian dari rencana strategis keseluruhan."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "13. The first step in strategic planning is to _____.",
        "pilihan": [
            "recruit and hire the right personnel",
            "examine historical data",
            "develop a mission for the total corporation",
            "allocate resources to the company’s various SBUs",
            "establish the corporation’s long-term objectives"
        ],
        "jawaban_benar": "develop a mission for the total corporation",
        "pembahasan": "**Pembahasan:** Langkah pertama perencanaan strategis adalah menetapkan misi perusahaan (mission statement) yang mendefinisikan tujuan dan bisnis perusahaan."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "14. Strategic Business Units (SBUs) whose products have a small market share in slow-growth markets are called _____; SBUs whose products have a low market share in high-growth markets are called _____; and SBUs whose products have a dominant market share in low-growth markets are called _____.",
        "pilihan": [
            "stars; dogs; cash cows",
            "cash cows; question marks; stars",
            "cash cows; stars; dogs",
            "dogs; question marks; cash cows",
            "question marks; cash cows; question marks"
        ],
        "jawaban_benar": "dogs; question marks; cash cows",
        "pembahasan": "**Pembahasan:** Matriks BCG: Dogs (pangsa kecil, pertumbuhan rendah), Question Marks (pangsa kecil, pertumbuhan tinggi), Cash Cows (pangsa besar, pertumbuhan rendah), Stars (pangsa besar, pertumbuhan tinggi)."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "15. A company that has been selling its products in New Zealand and Australia decides to expand into Asia, offering the same products as it does in New Zealand and Australia. This company has implemented a _____ strategy.",
        "pilihan": [
            "market development",
            "product penetration",
            "market penetration",
            "diversification",
            "product development"
        ],
        "jawaban_benar": "market development",
        "pembahasan": "**Pembahasan:** Strategi pengembangan pasar (market development) adalah memperkenalkan produk yang sudah ada ke pasar baru (geografis baru)."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "16. Which of the following is/are a source of information for a marketing intelligence system?",
        "pilihan": [
            "trade publications",
            "salespeople",
            "observational research",
            "current customers",
            "all of the above"
        ],
        "jawaban_benar": "all of the above",
        "pembahasan": "**Pembahasan:** Sistem intelijen pemasaran menggunakan berbagai sumber: publikasi dagang, tenaga penjualan, riset observasi, dan pelanggan saat ini untuk mengumpulkan informasi tentang lingkungan pemasaran."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "17. _____ is the process of collecting, analysing, and interpreting data about customers, competition, and the business environment to improve marketing effectiveness.",
        "pilihan": [
            "Marketing research",
            "Marketing management",
            "Competitive departmentalisation",
            "Data synergy",
            "Internal marketing"
        ],
        "jawaban_benar": "Marketing research",
        "pembahasan": "**Pembahasan:** Riset pemasaran (marketing research) adalah proses sistematis mengumpulkan, menganalisis, dan menginterpretasi data untuk membantu pengambilan keputusan pemasaran."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "18. _____ data refers to data collected for some other purpose than the one at hand. _____ data is collected to help in making a specific decision.",
        "pilihan": [
            "Primary; secondary",
            "Primary; acquired",
            "Acquired; consumer",
            "Secondary; acquired",
            "Secondary; primary"
        ],
        "jawaban_benar": "Secondary; primary",
        "pembahasan": "**Pembahasan:** Data sekunder telah dikumpulkan untuk tujuan lain, sedangkan data primer dikumpulkan khusus untuk riset saat ini."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "19. Which of these is not part of the marketing concept?",
        "pilihan": [
            "Providing customer satisfaction",
            "Matching competitors' offerings",
            "It relies on the integrated effort of numerous departments, not just marketing",
            "That corporate goals can be achieved through customer satisfaction",
            "Understanding customer needs"
        ],
        "jawaban_benar": "Matching competitors' offerings",
        "pembahasan": "**Pembahasan:** Konsep pemasaran berfokus pada kepuasan kebutuhan pelanggan melalui upaya terpadu, bukan sekadar meniru pesaing."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "20. A consumer who is considering purchasing a new car would be likely to use _____.",
        "pilihan": [
            "Routinised response behaviour",
            "stimulus generalisation",
            "impulse",
            "limited problem solving",
            "extended problem solving"
        ],
        "jawaban_benar": "extended problem solving",
        "pembahasan": "**Pembahasan:** Pembelian mobil baru melibatkan risiko tinggi dan pertimbangan kompleks, sehingga konsumen akan melakukan pemecahan masalah yang diperluas (extended problem solving)."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "21. Before selecting a marketing strategy, a marketing manager should consider:",
        "pilihan": [
            "the company's resources and objectives.",
            "the company's competitors.",
            "the needs of potential customers.",
            "relevant technological changes in the area.",
            "All of the above."
        ],
        "jawaban_benar": "All of the above.",
        "pembahasan": "**Pembahasan:** Sebelum memilih strategi pemasaran, manajer harus mempertimbangkan semua faktor: sumber daya perusahaan, pesaing, kebutuhan pelanggan, dan perubahan teknologi."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "22. According to the BCG growth matrix, _____ emphasise/s both new products and new markets to achieve growth.",
        "pilihan": [
            "Diversification strategies",
            "Market penetration strategies",
            "Monopolistic competition",
            "Operations planning",
            "Strategic planning"
        ],
        "jawaban_benar": "Diversification strategies",
        "pembahasan": "**Pembahasan:** Strategi diversifikasi melibatkan produk baru dan pasar baru, sesuai dengan matriks pertumbuhan Ansoff."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "23. Though Mitre 10 Mega experienced significant growth since they first entered the market, sales figures have been declining for the last few years. Their marketing team wants to design a campaign that aims to increase sales figures, but first they would like to find out some of the potential reasons why their sales have been declining. What type of research approach would be most useful to them?",
        "pilihan": [
            "Experimental",
            "Causal",
            "Descriptive",
            "Exploratory",
            "Experiential"
        ],
        "jawaban_benar": "Exploratory",
        "pembahasan": "**Pembahasan:** Riset eksploratori digunakan untuk memahami masalah yang belum jelas, mencari ide dan wawasan awal sebelum penelitian lebih lanjut."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "24. When Amy realises her supply of alcohol was consumed at last weekend’s party, she first retrieves information from her memory about what types of alcohol she and her friends like most and then asks the clerk at the store what he would recommend. Amy started with a(n) _____ search and then progressed to a(n) _____ search.",
        "pilihan": [
            "consideration; evaluative",
            "focused; broad",
            "internal; external",
            "routinised; extended",
            "self; inclusive"
        ],
        "jawaban_benar": "internal; external",
        "pembahasan": "**Pembahasan:** Pencarian internal mengacu pada ingatan, sedangkan pencarian external melibatkan sumber luar seperti teman atau tenaga penjual."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "25. Beck is puzzled by the recent decrease in sales at one of the Auto Barn locations for which she is the regional manager. She knows the best way to approach this problem and obtain accurate information is to use:",
        "pilihan": [
            "the marketing research process.",
            "the opinions of store managers.",
            "company sales data.",
            "hypothesis testing.",
            "stratified sampling of customers."
        ],
        "jawaban_benar": "the marketing research process.",
        "pembahasan": "**Pembahasan:** Proses riset pemasaran memberikan pendekatan sistematis untuk mengidentifikasi masalah, mengumpulkan data, dan memperoleh informasi yang akurat."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "26. Amazon, the online provider of books, music, movies, toys and many other products, follows buyers’ purchases and recommends related topics. The firm is exhibiting characteristics associated with the [BLANK] orientation.",
        "pilihan": [
            "production",
            "sales",
            "marketing",
            "social",
            "Development"
        ],
        "jawaban_benar": "marketing",
        "pembahasan": "**Pembahasan:** Orientasi pemasaran berfokus pada memenuhi kebutuhan pelanggan. Amazon menggunakan data pembelian untuk merekomendasikan produk yang relevan, menunjukkan pemahaman terhadap pelanggan."
    },
    {
        "tipe": "pilihan_ganda",
        "pertanyaan": "27. If The Warehouse wants to learn about consumers’ attitudes towards online purchases and conducts a study to acquire this information, this study would collect [BLANK] data.",
        "pilihan": [
            "causal",
            "experimental",
            "primary",
            "laboratory",
            "secondary"
        ],
        "jawaban_benar": "primary",
        "pembahasan": "**Pembahasan:** Karena The Warehouse melakukan studi khusus untuk memperoleh informasi tentang sikap konsumen, data yang dikumpulkan adalah data primer."
    },

    # ========== ESAI (1–5) ==========
    {
        "tipe": "essai",
        "pertanyaan": "1. As the text notes, technology is changing rapidly. Less than a decade ago, the hot new technology was the Radio-frequency Identification Chip (RFID) which enabled tracking of inventory or postal items and promised to revolutionise warehouse management and delivery systems. Today the latest technologies involve tracking people. Consumers can wear bracelets with embedded chips that track a person’s movements through a venue. Alternatively, tracking can be carried out via Smartphones. These types of technologies have advantages and disadvantages to consumers. Briefly outline two advantages and two disadvantages of personalised tracking devices. (15 marks)",
        "jawaban_benar": "Advantages: personalisation, efficiency; Disadvantages: privacy, security.",
        "pembahasan": "**Model jawaban:**\n\nKeuntungan:\n- Personalisasi layanan (misal: rekomendasi berbasis lokasi, penawaran khusus).\n- Kemudahan dan efisiensi (pembayaran otomatis, navigasi dalam ruangan).\n\nKekurangan:\n- Pelanggaran privasi (data lokasi dapat disalahgunakan).\n- Keamanan data (risiko peretasan dan kebocoran informasi pribadi)."
    },
    {
        "tipe": "essai",
        "pertanyaan": "2. In a short essay, briefly explain why consumers in the modern marketplace are said to have greater power and control. (15 marks)",
        "jawaban_benar": "Consumers have more power due to internet access, social media, and ability to compare prices and reviews.",
        "pembahasan": "**Model jawaban:**\nKonsumen modern memiliki kekuatan lebih karena akses internet dan media sosial memungkinkan mereka membandingkan harga, membaca ulasan, dan berbagi pengalaman. Mereka dapat mencari informasi secara mandiri, memberikan umpan balik langsung ke perusahaan, dan memengaruhi merek melalui konten buatan pengguna. Perusahaan harus responsif terhadap ekspektasi konsumen yang semakin tinggi."
    },
    {
        "tipe": "essai",
        "pertanyaan": "3. An up-market accommodation hotel wants to gain customer insights about the level of service being offered to its current customers. What recommendations would you make about suitable data collection methods? Briefly outline the principal advantages and disadvantages of each data collection method identified. (15 marks)",
        "jawaban_benar": "Methods: surveys, interviews, observation, suggestion boxes.",
        "pembahasan": "**Model jawaban:**\nMetode yang cocok:\n- **Survei daring (email/QR code):** Murah, cepat, mudah dianalisis; namun response rate rendah, kurang mendalam.\n- **Wawancara mendalam (tatap muka/telepon):** Data kaya, bisa eksplorasi; mahal, butuh waktu, bias pewawancara.\n- **Observasi (mistery guest):** Perilaku nyata, objektif; terbatas pada aspek yang bisa diamati, etika.\n- **Kotak saran/follow-up email:** Sederhana, langsung dari pelanggan; sukarela, tidak representatif."
    },
    {
        "tipe": "essai",
        "pertanyaan": "4. Kathmandu has recently noticed that many younger consumers are shifting their purchasing behaviour. Instead of buying products purely based on price or brand reputation, customers are increasingly considering sustainability, product reviews on social media, and recommendations from influencers. In response, Kathmandu is redesigning its marketing strategy by promoting eco-friendly materials, encouraging online reviews, and collaborating with outdoor lifestyle influencers. Tasks: Using relevant consumer behaviour concepts and theories, discuss how consumers make purchasing decisions in today’s marketplace. In your answer, analyse the factors that may influence consumer behaviour and explain how businesses can use this understanding to develop effective marketing strategies. Support your discussion with examples from the case and other relevant examples where appropriate. (15 marks)",
        "jawaban_benar": "Consumer decision process: problem recognition, information search, evaluation, purchase, post-purchase. Influenced by social, personal, psychological factors.",
        "pembahasan": "**Model jawaban:**\nProses keputusan konsumen (problem recognition, information search, evaluation, purchase, post-purchase) dipengaruhi faktor budaya, sosial, pribadi, dan psikologis. Saat ini, media sosial dan influencer (faktor sosial) serta kesadaran lingkungan (faktor pribadi) sangat berpengaruh. Kathmandu merespons dengan menyediakan informasi berkelanjutan (evaluasi alternatif) dan bekerja sama dengan influencer (memudahkan pencarian informasi). Strategi serupa digunakan oleh brand seperti Patagonia yang menekankan etika lingkungan."
    },
    {
        "tipe": "essai",
        "pertanyaan": "5. Macpac has experienced strong growth in recent years as more consumers take part in hiking, camping, and outdoor activities. However, the company is now facing increasing competition from international brands entering the New Zealand market and changing consumer expectations regarding sustainability, pricing, and online shopping. To remain competitive, Macpac’s management team is reviewing its long-term direction. They are analysing market trends, evaluating the company’s strengths and weaknesses, and considering new opportunities such as expanding into new markets, introducing innovative products, and strengthening their digital marketing presence. Tasks: Discuss the importance of strategic planning for organisations operating in competitive markets. In your answer, explain how strategic planning helps companies identify opportunities, allocate resources effectively, and achieve long-term objectives. Use examples from the case and other relevant examples to support your discussion. (15 marks)",
        "jawaban_benar": "Strategic planning helps set direction, allocate resources, adapt to changes.",
        "pembahasan": "**Model jawaban:**\nPerencanaan strategis penting untuk menetapkan arah jangka panjang, mengalokasikan sumber daya secara optimal, dan beradaptasi dengan perubahan pasar. Macpac menggunakan analisis SWOT untuk mengidentifikasi peluang (ekspansi pasar, inovasi produk) dan ancaman (kompetitor, perubahan preferensi). Dengan strategic planning, perusahaan dapat memfokuskan investasi pada area yang menjanjikan (digital marketing) dan mempertahankan keunggulan bersaing. Contoh lain: Nike yang terus berinovasi dan memperkuat kanal digital."
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