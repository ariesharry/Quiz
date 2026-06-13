import streamlit as st

# =========================
# ARTICLE FOR SECTION A
# =========================

ARTICLE = """
**FreshBox NZ: Disrupting the Grocery Market Through Digital Innovation**

*Source: BusinessNZ.co.nz, 15 March 2024*

FreshBox NZ, a New Zealand-based online grocery and meal-kit delivery service, has rapidly grown since its 
launch in 2021 to become one of the country's most talked-about direct-to-consumer brands. The company 
delivers pre-portioned, fresh ingredients with recipe cards directly to customers' homes, targeting busy 
professionals and health-conscious families.

FreshBox CEO Mia Tane explained that the company was built on a simple insight: "Kiwis want to eat well 
but don't have time to plan and shop. We remove those barriers entirely." The company segments its 
customers into three primary groups — singles aged 18–30 looking for convenience, families seeking 
variety, and health-focused consumers aged 45–60.

The company's pricing strategy has been carefully considered. Rather than competing purely on price, 
FreshBox has positioned itself as a premium service emphasising freshness, local sourcing, and zero food 
waste. Mia noted, "We don't chase the lowest price — we price to reflect the real value of what we offer."

To manage demand during quieter periods, FreshBox offers discounted subscription rates on Mondays and 
Tuesdays and uses a flexible pricing model during peak holiday weeks. The company has also introduced a 
referral rewards programme and seasonal bundle packs that have proven popular with existing customers.

FreshBox operates entirely online, using a marketing website, a mobile app, social media and email 
marketing to connect with customers. The company's Instagram account has over 150,000 followers, where 
it posts recipe videos, sustainability content, and behind-the-scenes farm stories. "Social media is where 
our community lives," said Mia.

The brand invests heavily in employee training to ensure every customer interaction — whether over the 
phone, through live chat, or via email — meets high standards. Drivers are instructed to always greet 
customers warmly at delivery. "Our people are our brand at the doorstep," Mia said.

FreshBox's packaging has also become part of its brand identity — sustainably sourced boxes with vibrant 
colour-coded labels help customers identify freshness dates and dietary categories at a glance. The company 
recently introduced chilled inserts to extend freshness windows and reduce spoilage complaints.

Looking ahead, FreshBox plans to expand its product range by adding a line of ready-to-eat meals — a move 
that would stretch the product line into a new category. The company is also exploring a franchise model 
to allow regional operators to deliver under the FreshBox brand in the South Island and Northland.
"""

# =========================
# 64 MULTIPLE CHOICE QUESTIONS
# =========================

mcq_list = [
    # Q1–16: Article-based
    {
        "pertanyaan": "When FreshBox asks 'What are our customers really buying when they order a meal kit?', they are considering which product level?",
        "pilihan": ["Actual product", "Augmented product", "Core product", "Co-branding", "Exchange"],
        "jawaban_benar": "Core product"
    },
    {
        "pertanyaan": "FreshBox's sustainably sourced packaging with vibrant colour-coded labels relates to which product level?",
        "pilihan": ["Core product", "Actual product", "Augmented product", "Industrial product", "Brand equity"],
        "jawaban_benar": "Actual product"
    },
    {
        "pertanyaan": "When FreshBox adds chilled inserts and extended freshness guarantees to its meal kits, it is planning at which product level?",
        "pilihan": ["Core product", "Actual product", "Augmented product", "Brand extension", "Convenience product"],
        "jawaban_benar": "Augmented product"
    },
    {
        "pertanyaan": "FreshBox's plan to add a line of ready-to-eat meals is an example of:",
        "pilihan": ["Product line filling", "Product line stretching", "Brand extension", "Product mix narrowing", "Line pruning"],
        "jawaban_benar": "Product line stretching"
    },
    {
        "pertanyaan": "FreshBox segments its customers into singles, families, and health-focused consumers. This is an example of:",
        "pilihan": ["Geographic segmentation", "Psychographic segmentation", "Undifferentiated marketing", "Demographic segmentation", "Niche marketing"],
        "jawaban_benar": "Demographic segmentation"
    },
    {
        "pertanyaan": "FreshBox targets busy professionals who value convenience and health. Dividing the market based on lifestyle and values is known as:",
        "pilihan": ["Demographic segmentation", "Geographic segmentation", "Psychographic segmentation", "Behavioural segmentation", "Intermarket segmentation"],
        "jawaban_benar": "Psychographic segmentation"
    },
    {
        "pertanyaan": "FreshBox positions itself as a premium service emphasising freshness, local sourcing, and zero food waste. This is best described as a:",
        "pilihan": ["Price competition strategy", "Non-price competition strategy", "Penetration pricing strategy", "Product line filling", "Undifferentiated strategy"],
        "jawaban_benar": "Non-price competition strategy"
    },
    {
        "pertanyaan": "FreshBox's offer of discounted subscription rates on Mondays and Tuesdays is a strategy to manage which service characteristic?",
        "pilihan": ["Intangibility", "Heterogeneity", "Inseparability", "Perishability", "Variability"],
        "jawaban_benar": "Perishability"
    },
    {
        "pertanyaan": "FreshBox invests heavily in employee training so every customer interaction meets high standards. This strategy primarily addresses which service characteristic?",
        "pilihan": ["Intangibility", "Perishability", "Inseparability", "Heterogeneity", "Tangibility"],
        "jawaban_benar": "Heterogeneity"
    },
    {
        "pertanyaan": "FreshBox drivers greet customers warmly at delivery. This relates to which variable of the expanded services marketing mix?",
        "pilihan": ["Physical evidence", "Processes", "Price", "Promotion", "People"],
        "jawaban_benar": "People"
    },
    {
        "pertanyaan": "FreshBox's mobile app, live chat, and email interactions are examples of:",
        "pilihan": ["Servicescape", "Customer touchpoints", "Tangible cues", "Physical evidence", "Atmospherics"],
        "jawaban_benar": "Customer touchpoints"
    },
    {
        "pertanyaan": "FreshBox uses Instagram, a marketing website, and email marketing. This combination of online channels is best described as:",
        "pilihan": ["Conventional marketing", "A push strategy", "Omnichannel digital marketing", "Disintermediation", "A vertical marketing system"],
        "jawaban_benar": "Omnichannel digital marketing"
    },
    {
        "pertanyaan": "FreshBox posts recipe videos and behind-the-scenes farm stories on social media. The primary purpose of this content is to:",
        "pilihan": ["Conduct A/B testing", "Build brand engagement and community", "Practice price skimming", "Reduce channel conflict", "Set reference prices"],
        "jawaban_benar": "Build brand engagement and community"
    },
    {
        "pertanyaan": "FreshBox's referral rewards programme and seasonal bundle packs are examples of which promotional mix element?",
        "pilihan": ["Advertising", "Personal selling", "Public relations", "Sales promotion", "Direct marketing"],
        "jawaban_benar": "Sales promotion"
    },
    {
        "pertanyaan": "FreshBox is exploring a franchise model for South Island and Northland delivery. A franchise is an example of which type of vertical marketing system?",
        "pilihan": ["Corporate VMS", "Administered VMS", "Conventional marketing channel", "Contractual VMS", "Horizontal marketing system"],
        "jawaban_benar": "Contractual VMS"
    },
    {
        "pertanyaan": "FreshBox operates entirely online without traditional retail stores. This is an example of:",
        "pilihan": ["Intensive distribution", "Indirect distribution", "A direct marketing channel", "Horizontal conflict", "Selective distribution"],
        "jawaban_benar": "A direct marketing channel"
    },

    # Q17–64: Non-article questions
    {
        "pertanyaan": "You are comparing multiple laptops across different websites before making a purchase decision. This product is best classified as a:",
        "pilihan": ["Convenience product", "Specialty product", "Unsought product", "Shopping product", "Industrial product"],
        "jawaban_benar": "Shopping product"
    },
    {
        "pertanyaan": "A consumer drives 40 minutes out of their way to buy a specific brand of guitar they are loyal to. This product is best classified as:",
        "pilihan": ["Convenience product", "Shopping product", "Unsought product", "Specialty product", "Augmented product"],
        "jawaban_benar": "Specialty product"
    },
    {
        "pertanyaan": "The [BLANK] of a product mix refers to how many different product lines a company carries.",
        "pilihan": ["Depth", "Length", "Consistency", "Width", "Height"],
        "jawaban_benar": "Width"
    },
    {
        "pertanyaan": "When Coca-Cola introduces a new flavour under its existing Coca-Cola brand name, this is an example of:",
        "pilihan": ["Product line stretching", "A line extension", "New product development", "Co-branding", "Downward stretching"],
        "jawaban_benar": "A line extension"
    },
    {
        "pertanyaan": "The brand name 'Snapple' is considered effective primarily because it is:",
        "pilihan": ["Descriptive and technical", "Distinctive and memorable", "Named after the founder", "Identical to competitor names", "Based on a scientific term"],
        "jawaban_benar": "Distinctive and memorable"
    },
    {
        "pertanyaan": "A supermarket sells products under its own 'Home Brand' label. These are examples of:",
        "pilihan": ["Manufacturer brands", "Licensed brands", "Co-brands", "National brands", "Private label brands"],
        "jawaban_benar": "Private label brands"
    },
    {
        "pertanyaan": "During the introduction stage of the product life cycle, a company should focus primarily on:",
        "pilihan": ["Reminder advertising", "Price reductions", "Creating consumer awareness", "Managing decline", "Diversifying the product mix"],
        "jawaban_benar": "Creating consumer awareness"
    },
    {
        "pertanyaan": "During the maturity stage of the product life cycle, which of the following actions is most appropriate?",
        "pilihan": ["Introducing the product for the first time", "Harvesting the product immediately", "Modifying the product, market, or marketing mix", "Withdrawing all promotional spending", "Dropping the product line entirely"],
        "jawaban_benar": "Modifying the product, market, or marketing mix"
    },
    {
        "pertanyaan": "Which product life cycle stage is typically the longest?",
        "pilihan": ["Introduction", "Decline", "Growth", "Maturity", "Product development"],
        "jawaban_benar": "Maturity"
    },
    {
        "pertanyaan": "A hotel chain offers guests complimentary breakfast and free Wi-Fi. These additions represent which product level?",
        "pilihan": ["Core product", "Actual product", "Augmented product", "Industrial product", "Convenience product"],
        "jawaban_benar": "Augmented product"
    },
    {
        "pertanyaan": "Consumer perceptions of what a product is worth — rather than the seller's cost — are the key to [BLANK] pricing.",
        "pilihan": ["Cost-plus", "Target-return", "Competition-based", "Customer value-based", "Captive-product"],
        "jawaban_benar": "Customer value-based"
    },
    {
        "pertanyaan": "A new tech company launches its smartwatch at a very high price to attract early adopters before lowering the price for the mass market. This is:",
        "pilihan": ["Penetration pricing", "Competitive pricing", "Bundle pricing", "Cost-plus pricing", "Price skimming"],
        "jawaban_benar": "Price skimming"
    },
    {
        "pertanyaan": "A new streaming service enters the market at $1.99/month to rapidly gain subscribers. This is an example of:",
        "pilihan": ["Price skimming", "Captive-product pricing", "Market penetration pricing", "Bundle pricing", "Prestige pricing"],
        "jawaban_benar": "Market penetration pricing"
    },
    {
        "pertanyaan": "A printer is sold cheaply, but the ink cartridges that must be used are sold at a high margin. This is an example of:",
        "pilihan": ["Bundle pricing", "Psychological pricing", "Captive-product pricing", "Segmented pricing", "Dynamic pricing"],
        "jawaban_benar": "Captive-product pricing"
    },
    {
        "pertanyaan": "Concert tickets are priced higher on Friday nights than Tuesday afternoons for the same show. This is an example of:",
        "pilihan": ["Bundle pricing", "Allowance pricing", "Captive-product pricing", "Segmented pricing", "Cost-plus pricing"],
        "jawaban_benar": "Segmented pricing"
    },
    {
        "pertanyaan": "Which of the following correctly describes consumer demand elasticity?",
        "pilihan": ["Elastic demand means demand barely changes with price changes", "Inelastic demand means demand changes greatly with price changes", "Elastic demand means demand changes greatly with price changes", "Inelastic demand means consumers are very price-sensitive", "Price elasticity is unrelated to substitute products"],
        "jawaban_benar": "Elastic demand means demand changes greatly with price changes"
    },
    {
        "pertanyaan": "Which of the following is NOT part of the expanded 7Ps marketing mix?",
        "pilihan": ["People", "Physical evidence", "Processes", "Profit", "Product"],
        "jawaban_benar": "Profit"
    },
    {
        "pertanyaan": "The physical environment in which a service takes place — such as a bank's interior design and furniture — is known as the:",
        "pilihan": ["Atmospherics", "Touchpoint", "Servicescape", "Physical cue", "Value chain"],
        "jawaban_benar": "Servicescape"
    },
    {
        "pertanyaan": "A hair salon experiences inconsistent service quality because different stylists have different skills and attitudes. This reflects which service characteristic?",
        "pilihan": ["Intangibility", "Perishability", "Inseparability", "Heterogeneity", "Tangibility"],
        "jawaban_benar": "Heterogeneity"
    },
    {
        "pertanyaan": "A yoga class that cannot be stored and resold if no students show up on a given day illustrates:",
        "pilihan": ["Inseparability", "Intangibility", "Heterogeneity", "Perishability", "Variability"],
        "jawaban_benar": "Perishability"
    },
    {
        "pertanyaan": "An airline uses the promise 'You're in good hands with AirSafe' to reassure customers about service quality. This strategy addresses which service characteristic?",
        "pilihan": ["Heterogeneity", "Perishability", "Inseparability", "Intangibility", "Variability"],
        "jawaban_benar": "Intangibility"
    },
    {
        "pertanyaan": "Market segmentation is defined as:",
        "pilihan": ["Ignoring differences between customer groups", "Pursuing all customers with the same offer", "Dividing a total heterogeneous market into groups with similar needs", "Selecting a single target market for all products", "Creating one product for the entire market"],
        "jawaban_benar": "Dividing a total heterogeneous market into groups with similar needs"
    },
    {
        "pertanyaan": "A company targeting several different segments with separate offers for each is using:",
        "pilihan": ["Undifferentiated marketing", "Niche marketing", "Micromarketing", "Differentiated marketing", "Mass marketing"],
        "jawaban_benar": "Differentiated marketing"
    },
    {
        "pertanyaan": "A small artisan coffee brand targets only specialty coffee enthusiasts and ignores mass-market buyers. This is an example of:",
        "pilihan": ["Undifferentiated marketing", "Differentiated marketing", "Concentrated (niche) marketing", "Micromarketing", "Mass marketing"],
        "jawaban_benar": "Concentrated (niche) marketing"
    },
    {
        "pertanyaan": "Which of the following is a requirement for a market segment to be useful?",
        "pilihan": ["It must include the entire population", "It must be measurable, accessible, substantial, and actionable", "It must have identical needs to other segments", "It must not be profitable to competitors", "It must be based solely on geographic variables"],
        "jawaban_benar": "It must be measurable, accessible, substantial, and actionable"
    },
    {
        "pertanyaan": "A brand positions itself as 'More for More' — offering superior quality at higher prices. Which of the following is an example?",
        "pilihan": ["Kmart", "Aldi", "Rolex", "Spirit Airlines", "Costco"],
        "jawaban_benar": "Rolex"
    },
    {
        "pertanyaan": "A perceptual map is used to:",
        "pilihan": ["Track sales performance over time", "Analyse product positions relative to competitors based on consumer perceptions", "Design new product features", "Monitor employee productivity", "Set optimal prices"],
        "jawaban_benar": "Analyse product positions relative to competitors based on consumer perceptions"
    },
    {
        "pertanyaan": "A channel member that performs tasks such as information gathering, promotion, negotiation, and risk-taking is adding [BLANK] to the marketing system.",
        "pilihan": ["Conflict", "Inefficiency", "Value", "Inventory costs", "Noise"],
        "jawaban_benar": "Value"
    },
    {
        "pertanyaan": "Two competing retailers in the same shopping mall both selling the same product brand are experiencing [BLANK] channel conflict.",
        "pilihan": ["Vertical", "Multichannel", "Administered", "Horizontal", "Corporate"],
        "jawaban_benar": "Horizontal"
    },
    {
        "pertanyaan": "A manufacturer bypasses its usual wholesale and retail intermediaries and sells directly to consumers online. This is an example of:",
        "pilihan": ["Vertical integration", "Multichannel distribution", "Horizontal conflict", "Disintermediation", "Intensive distribution"],
        "jawaban_benar": "Disintermediation"
    },
    {
        "pertanyaan": "Selling through only one intermediary in a particular geographic region to maintain brand exclusivity is known as:",
        "pilihan": ["Intensive distribution", "Selective distribution", "Multichannel distribution", "Exclusive distribution", "Contractual distribution"],
        "jawaban_benar": "Exclusive distribution"
    },
    {
        "pertanyaan": "Which of the following describes direct marketing?",
        "pilihan": ["Advertising on television during prime time", "Interacting directly with targeted individual consumers to obtain an immediate response", "Distributing products through retail stores", "A salesperson visiting trade fairs", "Sponsoring large public events"],
        "jawaban_benar": "Interacting directly with targeted individual consumers to obtain an immediate response"
    },
    {
        "pertanyaan": "A company's most expensive promotional tool is typically:",
        "pilihan": ["Advertising", "Sales promotion", "Public relations", "Personal selling", "Direct mail"],
        "jawaban_benar": "Personal selling"
    },
    {
        "pertanyaan": "A promotional strategy that focuses on channel members — pushing products through the distribution channel — is called a:",
        "pilihan": ["Pull strategy", "Pulsing strategy", "Continuous strategy", "Push strategy", "Direct strategy"],
        "jawaban_benar": "Push strategy"
    },
    {
        "pertanyaan": "Which advertising appeal uses humour, fear, or warmth to influence emotions?",
        "pilihan": ["Rational appeal", "Documentary appeal", "Emotional appeal", "Technical appeal", "Factual appeal"],
        "jawaban_benar": "Emotional appeal"
    },
    {
        "pertanyaan": "Unsolicited and unwanted commercial email sent to large numbers of recipients is known as:",
        "pilihan": ["Viral marketing", "A blog post", "Spam", "Display advertising", "Retargeting"],
        "jawaban_benar": "Spam"
    },
    {
        "pertanyaan": "When two versions of a digital ad are tested simultaneously to see which performs better, this is called:",
        "pilihan": ["Viral testing", "Omnichannel analysis", "Psychographic analysis", "A/B testing", "Data mining"],
        "jawaban_benar": "A/B testing"
    },
    {
        "pertanyaan": "A digital marketing ad that appears to a consumer because they previously browsed a product on a website is called a:",
        "pilihan": ["Display ad", "Search ad", "Contextual ad", "Retargeting ad", "Sponsored post"],
        "jawaban_benar": "Retargeting ad"
    },
    {
        "pertanyaan": "Viral marketing is best described as the digital equivalent of:",
        "pilihan": ["Personal selling", "Public relations", "Word-of-mouth marketing", "Telemarketing", "Sales promotion"],
        "jawaban_benar": "Word-of-mouth marketing"
    },
    {
        "pertanyaan": "Which of the following promotional tools is described as immediate, customised, and interactive?",
        "pilihan": ["Television advertising", "Outdoor advertising", "Magazine advertising", "Direct marketing", "Publicity"],
        "jawaban_benar": "Direct marketing"
    },
    {
        "pertanyaan": "A contest is different from a sweepstake because a contest is a game of [BLANK], while a sweepstake is a game of [BLANK].",
        "pilihan": ["Chance; skill", "Skill; chance", "Luck; strategy", "Chance; chance", "Strategy; luck"],
        "jawaban_benar": "Skill; chance"
    },
    {
        "pertanyaan": "Which of the following is NOT a benefit of digital marketing for sellers?",
        "pilihan": ["Lower cost of reaching markets", "Global reach", "Flexibility to update campaigns quickly", "Forced face-to-face customer interaction", "Access to customer data and behaviour analytics"],
        "jawaban_benar": "Forced face-to-face customer interaction"
    },
    {
        "pertanyaan": "Omnichannel marketing strategy refers to:",
        "pilihan": ["Using only digital channels to reach consumers", "Combining online and offline channels to create a seamless customer experience", "Targeting one channel exclusively for maximum efficiency", "Eliminating physical stores entirely", "Using only social media to promote products"],
        "jawaban_benar": "Combining online and offline channels to create a seamless customer experience"
    },
    {
        "pertanyaan": "The 'people' variable in the 7Ps expanded marketing mix includes all of the following EXCEPT:",
        "pilihan": ["Service employees", "Customer-to-customer interactions", "Physical infrastructure and buildings", "Personnel training", "Co-creation by customers"],
        "jawaban_benar": "Physical infrastructure and buildings"
    },
    {
        "pertanyaan": "The use of music, lighting, and scent in a retail environment to influence customer perception is known as:",
        "pilihan": ["Servicescape design", "Tangible cueing", "Atmospherics", "Physical evidence mapping", "Sensory branding"],
        "jawaban_benar": "Atmospherics"
    },
    {
        "pertanyaan": "Which of the following best describes the process of integrated marketing communications (IMC)?",
        "pilihan": ["Using only one promotional tool at a time", "Coordinating all promotional activities to deliver a consistent message", "Focusing solely on advertising for brand building", "Managing inventory across multiple channels", "Setting pricing across international markets"],
        "jawaban_benar": "Coordinating all promotional activities to deliver a consistent message"
    },
    {
        "pertanyaan": "A customer journey map is primarily used to:",
        "pilihan": ["Track employee attendance", "Monitor warehouse inventory", "Understand the complete set of customer touchpoints and experiences with a brand", "Set the company's annual pricing strategy", "Develop manufacturing processes"],
        "jawaban_benar": "Understand the complete set of customer touchpoints and experiences with a brand"
    },
]

# =========================
# 6 ESSAY / SHORT ANSWER QUESTIONS
# =========================

essay_list = [
    {
        "nomor": 1,
        "pertanyaan": """Using the FreshBox NZ case as a reference, describe the THREE levels of a product and explain how each level applies to FreshBox's meal kit offering. In your answer, provide a specific example for each product level and explain why understanding all three levels is important for marketers. (12 marks)""",
        "panduan": "Suggested structure: (1) Define and apply the core product level [4 marks]; (2) Define and apply the actual product level [4 marks]; (3) Define and apply the augmented product level [4 marks]. Use specific FreshBox examples at each level."
    },
    {
        "nomor": 2,
        "pertanyaan": """FreshBox NZ delivers meal kits to customers' homes and relies heavily on its drivers, customer service staff, and social media team to build customer relationships. Using FOUR characteristics of services, describe how each characteristic applies to a meal kit delivery service like FreshBox, and identify ONE specific strategy FreshBox could use to address the marketing challenge created by each characteristic. (12 marks)""",
        "panduan": "Suggested structure: Address each of the 4 service characteristics (intangibility, inseparability, perishability, heterogeneity) with (a) how it applies to FreshBox, and (b) one specific strategy to overcome it. [3 marks per characteristic]"
    },
    {
        "nomor": 3,
        "pertanyaan": """FreshBox NZ has segmented its market into three groups: singles aged 18–30, families, and health-focused consumers aged 45–60. (a) Identify and explain the primary segmentation basis FreshBox is using, and describe TWO other segmentation bases it could also consider to better understand its customers. (b) Based on its segments, recommend a targeting strategy for FreshBox and justify your recommendation. (12 marks)""",
        "panduan": "Part (a): Identify the primary basis [2 marks]; describe 2 other bases with examples [4 marks]. Part (b): Name and define the targeting strategy [3 marks]; provide justification using FreshBox's context [3 marks]."
    },
    {
        "nomor": 4,
        "pertanyaan": """FreshBox NZ positions itself as a premium brand competing on quality, local sourcing, and sustainability rather than price. (a) Explain the difference between price competition and non-price competition, providing examples of each. (b) Identify and justify which VALUE PROPOSITION strategy (from the five discussed in lectures) best describes FreshBox's market position. (c) Discuss TWO pricing tactics FreshBox currently uses and explain how they support its overall pricing objectives. (12 marks)""",
        "panduan": "Part (a): Define both types of competition with examples [4 marks]. Part (b): Name and justify the value proposition with FreshBox evidence [4 marks]. Part (c): Identify 2 tactics (e.g. flexible/dynamic pricing, bundle pricing) and link to objectives [4 marks]."
    },
    {
        "nomor": 5,
        "pertanyaan": """FreshBox NZ is planning a promotional campaign to attract new customers in Auckland and retain existing subscribers. (a) Discuss FOUR elements of the promotional mix that FreshBox could use, explaining the specific role each element would play in the campaign and why it is appropriate for FreshBox's target market and product. (b) Explain whether FreshBox should use a push or pull promotional strategy, and justify your answer. (12 marks)""",
        "panduan": "Part (a): Identify 4 promotional mix elements (advertising, PR, personal selling, sales promotion, or direct/digital marketing). For each: describe the tool, explain its role for FreshBox, and justify why it suits the brand [2 marks each = 8 marks]. Part (b): Define both strategies and justify the appropriate one for FreshBox [4 marks]."
    },
    {
        "nomor": 6,
        "pertanyaan": """FreshBox NZ operates entirely through digital channels. (a) Discuss FOUR specific digital marketing channels or tools that FreshBox currently uses or could use, explaining the purpose and advantage of each for FreshBox's business. (b) Explain the concept of omnichannel marketing and evaluate whether FreshBox, as a digital-only brand, truly practices omnichannel marketing or not. Use evidence from the case to support your answer. (12 marks)""",
        "panduan": "Part (a): Identify 4 digital channels (e.g. social media, email, mobile app, marketing website, retargeting ads, influencer marketing). For each: explain its purpose and one advantage for FreshBox [2 marks each = 8 marks]. Part (b): Define omnichannel marketing [2 marks]; evaluate FreshBox's omnichannel status with case evidence [2 marks]."
    }
]

# =========================
# SESSION STATE
# =========================

if "submitted_mcq" not in st.session_state:
    st.session_state.submitted_mcq = False

if "submitted_essay" not in st.session_state:
    st.session_state.submitted_essay = False

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Section A – Multiple Choice"

def norm(x):
    return x.strip().lower() if x else ""

# =========================
# UI
# =========================

st.set_page_config(page_title="MKTG100 Exam Practice", layout="wide")

st.title("📘 MKTG100 Principles of Marketing – Exam Practice")
st.caption("64 Multiple Choice Questions + 6 Short Answer / Essay Questions")

tab1, tab2 = st.tabs(["📝 Section A – Multiple Choice (64 marks)", "✍️ Section B – Short Answer (36 marks)"])

# =========================
# SECTION A
# =========================

with tab1:
    st.markdown("### Please read the article below carefully, then answer all 64 multiple-choice questions.")
    
    with st.expander("📰 Click to read the FreshBox NZ article (Questions 1–16)", expanded=False):
        st.markdown(ARTICLE)

    st.markdown("---")
    st.markdown("#### Questions 1–16 are based on the article. Questions 17–64 are general.")
    st.markdown("---")

    mcq_score = 0
    mcq_total = len(mcq_list)

    for i, soal in enumerate(mcq_list):
        label_prefix = "📰 " if i < 16 else ""
        st.markdown(f"**Question {i+1}** {label_prefix}")
        key = f"mcq_{i}"
        st.radio(
            soal["pertanyaan"],
            soal["pilihan"],
            key=key,
            index=None,
            label_visibility="visible"
        )

        if st.session_state.submitted_mcq:
            user_ans = st.session_state.get(key)
            if user_ans == soal["jawaban_benar"]:
                mcq_score += 1
                st.success(f"✅ Correct: {soal['jawaban_benar']}")
            else:
                st.error(f"❌ Incorrect. Correct answer: **{soal['jawaban_benar']}**")

        st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Submit Section A", use_container_width=True, key="submit_mcq"):
            st.session_state.submitted_mcq = True
            st.rerun()

    if st.session_state.submitted_mcq:
        pct = mcq_score / mcq_total * 100
        st.success(f"### Section A Score: {mcq_score} / {mcq_total} ({pct:.1f}%)")

        with col2:
            if st.button("🔄 Reset Section A", use_container_width=True, key="reset_mcq"):
                for k in list(st.session_state.keys()):
                    if k.startswith("mcq_"):
                        del st.session_state[k]
                st.session_state.submitted_mcq = False
                st.rerun()

# =========================
# SECTION B
# =========================

with tab2:
    st.markdown("### Answer **all 6** short answer / essay questions. Each question is worth **12 marks**.")
    st.markdown("Write your answers in the text areas provided. Use the marking guidelines for self-assessment.")
    st.markdown("---")

    for essay in essay_list:
        st.markdown(f"### Question {essay['nomor']}")
        st.markdown(essay["pertanyaan"])
        key = f"essay_{essay['nomor']}"

        st.text_area(
            f"Your answer for Question {essay['nomor']}:",
            key=key,
            height=250,
            placeholder="Write your answer here..."
        )

        if st.session_state.submitted_essay:
            user_text = st.session_state.get(key, "").strip()
            if user_text:
                st.info(f"📋 **Marking Guideline:** {essay['panduan']}")
                word_count = len(user_text.split())
                st.caption(f"Word count: {word_count}")
            else:
                st.warning("⚠️ No answer provided for this question.")

        st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📤 Submit Section B", use_container_width=True, key="submit_essay"):
            st.session_state.submitted_essay = True
            st.rerun()

    if st.session_state.submitted_essay:
        answered = sum(
            1 for e in essay_list
            if st.session_state.get(f"essay_{e['nomor']}", "").strip()
        )
        st.success(f"Section B submitted! You answered {answered}/6 questions. Use the marking guidelines above to self-assess.")

        with col2:
            if st.button("🔄 Reset Section B", use_container_width=True, key="reset_essay"):
                for k in list(st.session_state.keys()):
                    if k.startswith("essay_"):
                        del st.session_state[k]
                st.session_state.submitted_essay = False
                st.rerun()

# =========================
# SIDEBAR SUMMARY
# =========================

with st.sidebar:
    st.markdown("## 📊 Exam Overview")
    st.markdown("""
    **Section A** – Multiple Choice  
    64 questions × 1 mark = **64 marks**
    
    **Section B** – Short Answer  
    6 questions × 12 marks = **36 marks**
    
    **Total: 100 marks**
    """)
    st.markdown("---")
    st.markdown("## 📚 Topics Covered")
    st.markdown("""
    - Product levels & classifications
    - Branding & packaging
    - Product life cycle (PLC)
    - Market segmentation & targeting
    - Positioning & differentiation
    - Pricing strategies & tactics
    - Distribution channels & retailing
    - Promotional mix & IMC
    - Services marketing (7Ps)
    - Digital & direct marketing
    """)

    if st.session_state.submitted_mcq:
        score = sum(
            1 for i, s in enumerate(mcq_list)
            if st.session_state.get(f"mcq_{i}") == s["jawaban_benar"]
        )
        pct = score / len(mcq_list) * 100
        st.markdown("---")
        st.markdown("## 🏆 Section A Result")
        st.metric("Score", f"{score}/{len(mcq_list)}", f"{pct:.1f}%")