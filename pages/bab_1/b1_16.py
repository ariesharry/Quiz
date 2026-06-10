import streamlit as st

st.set_page_config(page_title="MGMT100 Exam Practice", layout="wide")

soal_list = [

# =========================
# 50 MULTIPLE CHOICE QUESTIONS
# W5 – Control & Environment
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following BEST defines the management function of control?",
    "pilihan": [
        "The process of motivating employees to achieve goals",
        "A systematic process of regulating organisational activities to make them consistent with plans, standards, and goals",
        "Assigning tasks to departments and individuals",
        "Setting long-term organisational objectives",
        "Communicating decisions to subordinates"
    ],
    "jawaban_benar": "A systematic process of regulating organisational activities to make them consistent with plans, standards, and goals"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A manager walks around the factory floor daily to observe employee performance firsthand. This practice is best described as:",
    "pilihan": [
        "Management by exception",
        "Management by walking around (MBWA)",
        "Decentralised authority",
        "Corrective action",
        "Quantitative measurement"
    ],
    "jawaban_benar": "Management by walking around (MBWA)"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In the 4-step control model, 'management by exception' occurs during which step?",
    "pilihan": [
        "Step 1 – Establish standards",
        "Step 2 – Measure performance",
        "Step 3 – Compare performance to standards",
        "Step 4 – Take corrective action",
        "Step 2 and Step 4 equally"
    ],
    "jawaban_benar": "Step 3 – Compare performance to standards"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is an example of an INPUT standard in the control process?",
    "pilihan": [
        "Number of units produced per hour",
        "Customer satisfaction scores",
        "Employee behaviour and conduct rules",
        "Revenue targets",
        "Delivery time benchmarks"
    ],
    "jawaban_benar": "Employee behaviour and conduct rules"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company's control system focuses exclusively on monthly sales figures, ignoring customer complaints and staff turnover. This is an example of which barrier to effective control?",
    "pilihan": [
        "Too much control",
        "Too little employee participation",
        "Overemphasis on means not ends",
        "Overemphasis on one measure only",
        "Lack of strategic orientation"
    ],
    "jawaban_benar": "Overemphasis on one measure only"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which role of control helps managers identify when unexpected opportunities should be pursued?",
    "pilihan": [
        "Adapt to change",
        "Reduce costs and add value",
        "Detect opportunities",
        "Decentralise authority",
        "Manage complexity"
    ],
    "jawaban_benar": "Detect opportunities"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A control system that allows branch managers to make decisions within defined boundaries without head office approval BEST illustrates:",
    "pilihan": [
        "Detecting irregularities",
        "Adapting to change",
        "Managing complexity",
        "Decentralising authority",
        "Reducing costs"
    ],
    "jawaban_benar": "Decentralising authority"
},

# W6 – Teams and HRM
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following BEST distinguishes a team from a group?",
    "pilihan": [
        "Teams have more than 10 members; groups have fewer",
        "Teams share complementary skills, a common goal, and mutual accountability; groups do not necessarily have these",
        "Groups have formal leaders; teams do not",
        "Teams are always temporary; groups are permanent",
        "Groups focus on individual performance; teams focus on profit"
    ],
    "jawaban_benar": "Teams share complementary skills, a common goal, and mutual accountability; groups do not necessarily have these"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A newly formed project team is polite but cautious; members are testing boundaries and getting to know each other. According to Tuckman's model, this team is in which stage?",
    "pilihan": [
        "Storming",
        "Norming",
        "Performing",
        "Forming",
        "Adjourning"
    ],
    "jawaban_benar": "Forming"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Conflict over different ideas about the best strategy to launch a product is classified as:",
    "pilihan": [
        "Relationship conflict",
        "Task/substantive conflict",
        "Emotional conflict",
        "Interpersonal conflict",
        "Social loafing"
    ],
    "jawaban_benar": "Task/substantive conflict"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Social loafing is MOST likely to increase when:",
    "pilihan": [
        "Individual contributions are clearly visible",
        "The task is highly important to each member",
        "Group size becomes larger and individual effort is harder to identify",
        "The team is in the performing stage",
        "Cohesiveness is very high"
    ],
    "jawaban_benar": "Group size becomes larger and individual effort is harder to identify"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A Realistic Job Preview (RJP) is primarily designed to:",
    "pilihan": [
        "Replace the formal interview process",
        "Give candidates an honest picture of both positive and negative aspects of a job to improve retention",
        "Screen candidates using psychometric tests",
        "Assess candidates' leadership potential",
        "Introduce new employees to company culture after hiring"
    ],
    "jawaban_benar": "Give candidates an honest picture of both positive and negative aspects of a job to improve retention"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "In a behavioural interview, a candidate is asked to describe a time they resolved a conflict at work. The interviewer is using which technique to structure the response?",
    "pilihan": [
        "MBWA",
        "STAR (Situation–Task–Action–Result)",
        "SWOT",
        "RJP",
        "BMC"
    ],
    "jawaban_benar": "STAR (Situation–Task–Action–Result)"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is a significant DISADVANTAGE of using AI tools in recruitment?",
    "pilihan": [
        "AI increases the cost of screening CVs",
        "AI reduces the efficiency of shortlisting candidates",
        "AI may embed algorithmic bias, raising ethical concerns",
        "AI cannot handle large volumes of applications",
        "AI eliminates the need for reference checks"
    ],
    "jawaban_benar": "AI may embed algorithmic bias, raising ethical concerns"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The correct sequence of the HRM process is:",
    "pilihan": [
        "Selection → Recruitment → Training → Orientation → Performance Management",
        "Recruitment → Selection → Orientation → Performance Management → Training & Rewards",
        "Orientation → Recruitment → Selection → Training → Performance Management",
        "Training → Recruitment → Selection → Orientation → Rewards",
        "Performance Management → Selection → Recruitment → Training → Rewards"
    ],
    "jawaban_benar": "Recruitment → Selection → Orientation → Performance Management → Training & Rewards"
},

# W7 – Business Ethics and CSR
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An ethical dilemma is characterised by:",
    "pilihan": [
        "A clear legal solution that resolves all moral questions",
        "Conflicting moral principles, no obviously correct answer, and significant consequences for stakeholders",
        "A situation where one option benefits everyone equally",
        "A disagreement between two employees about work procedures",
        "A legal question requiring a court ruling"
    ],
    "jawaban_benar": "Conflicting moral principles, no obviously correct answer, and significant consequences for stakeholders"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A manager decides to approve a small bribe to win a contract because 'everyone does it in this industry.' According to Kohlberg's stages of moral development, this reasoning BEST reflects:",
    "pilihan": [
        "Post-conventional reasoning",
        "Conventional reasoning",
        "Pre-conventional reasoning",
        "Principled reasoning",
        "Utilitarian reasoning"
    ],
    "jawaban_benar": "Pre-conventional reasoning"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The ethical principle of 'distributive justice' requires that managers:",
    "pilihan": [
        "Maximise overall happiness for the greatest number",
        "Protect every individual's fundamental rights",
        "Treat people fairly and impartially based on what they deserve",
        "Act in their own long-term self-interest",
        "Demonstrate personal honesty and integrity"
    ],
    "jawaban_benar": "Treat people fairly and impartially based on what they deserve"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "According to Carroll's CSR Pyramid, which level forms the FOUNDATION on which all other responsibilities rest?",
    "pilihan": [
        "Legal responsibilities",
        "Ethical responsibilities",
        "Discretionary/philanthropic responsibilities",
        "Economic responsibilities",
        "Environmental responsibilities"
    ],
    "jawaban_benar": "Economic responsibilities"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company donates 2% of profits to local schools and community sports clubs. This activity falls under which level of Carroll's CSR Pyramid?",
    "pilihan": [
        "Economic",
        "Legal",
        "Ethical",
        "Discretionary/Philanthropic",
        "Environmental"
    ],
    "jawaban_benar": "Discretionary/Philanthropic"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The sustainability concept of 'People–Planet–Profit' is also referred to as:",
    "pilihan": [
        "The Carroll Pyramid",
        "The Triple Bottom Line",
        "The Stakeholder Model",
        "The Ethical Intensity Framework",
        "The CSR Matrix"
    ],
    "jawaban_benar": "The Triple Bottom Line"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Ethical intensity refers to:",
    "pilihan": [
        "The number of laws a company must follow",
        "How strongly employees feel about the company's mission",
        "The degree of moral importance of an ethical issue based on dimensions such as magnitude of harm and social consensus",
        "The frequency with which ethical dilemmas occur",
        "The level of pressure from government regulators"
    ],
    "jawaban_benar": "The degree of moral importance of an ethical issue based on dimensions such as magnitude of harm and social consensus"
},

# W8 – Diversity and Organisational Culture
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following is a PRIMARY dimension of diversity?",
    "pilihan": [
        "Educational background",
        "Work experience",
        "Religious beliefs",
        "Ethnicity",
        "Marital status"
    ],
    "jawaban_benar": "Ethnicity"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A manager assumes that all candidates from a particular region will be poor communicators. This fixed, generalised belief is BEST described as:",
    "pilihan": [
        "Prejudice",
        "Discrimination",
        "Stereotype",
        "Ethnocentrism",
        "Social loafing"
    ],
    "jawaban_benar": "Stereotype"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company provides reserved parking spaces close to the entrance for employees with disabilities, while all other employees park in the general lot. This is an example of:",
    "pilihan": [
        "Discrimination",
        "Equality",
        "Equity",
        "Prejudice",
        "Primary diversity"
    ],
    "jawaban_benar": "Equity"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A manager refuses to promote a qualified female employee because of personal biases. This action is classified as:",
    "pilihan": [
        "Stereotype",
        "Ethnocentrism",
        "Prejudice",
        "Discrimination",
        "Social loafing"
    ],
    "jawaban_benar": "Discrimination"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "According to New Zealand pay gap data, Pasifika women earn approximately how much for every dollar earned by a Pākehā man?",
    "pilihan": [
        "95 cents",
        "90 cents",
        "85 cents",
        "75 cents",
        "60 cents"
    ],
    "jawaban_benar": "75 cents"
},

# W9 – Innovation & Entrepreneurship
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Entrepreneurship is BEST defined as:",
    "pilihan": [
        "Managing an existing organisation's operations",
        "Identifying opportunities and creating new ventures despite risk and uncertainty to create value",
        "Investing capital in established companies",
        "Franchising an existing brand",
        "Administering government policies"
    ],
    "jawaban_benar": "Identifying opportunities and creating new ventures despite risk and uncertainty to create value"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An employee at a large corporation develops and launches a new product line using company resources without leaving the organisation. This person is BEST described as:",
    "pilihan": [
        "An entrepreneur",
        "A franchise owner",
        "An intrapreneur",
        "A stakeholder",
        "A social enterprise owner"
    ],
    "jawaban_benar": "An intrapreneur"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The Business Model Canvas (BMC) is a tool used by entrepreneurs to:",
    "pilihan": [
        "Recruit and select employees",
        "Measure production output",
        "Describe how a venture creates, delivers, and captures value",
        "Plan marketing advertising spend",
        "Calculate tax obligations"
    ],
    "jawaban_benar": "Describe how a venture creates, delivers, and captures value"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An entrepreneur who spots a gap in the market for eco-friendly packaging is demonstrating which aspect of entrepreneurship?",
    "pilihan": [
        "Intrapreneurship",
        "Risk aversion",
        "Opportunity recognition",
        "Control management",
        "Supply chain integration"
    ],
    "jawaban_benar": "Opportunity recognition"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Which of the following statements BEST distinguishes calculated risk-taking from recklessness in entrepreneurship?",
    "pilihan": [
        "Calculated risk-taking involves no financial investment",
        "Recklessness always leads to innovation",
        "Calculated risk-taking involves assessing probabilities and planning contingencies, while recklessness ignores potential downsides",
        "Calculated risk-taking is only applicable to large corporations",
        "Recklessness is required to identify market opportunities"
    ],
    "jawaban_benar": "Calculated risk-taking involves assessing probabilities and planning contingencies, while recklessness ignores potential downsides"
},

# W10 – Operations Management
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A factory that makes custom, high-variety, low-volume products (e.g., bespoke furniture) would MOST likely use which facilities layout?",
    "pilihan": [
        "Product layout",
        "Fixed-position layout",
        "Cellular layout",
        "Process layout",
        "Just-in-time layout"
    ],
    "jawaban_benar": "Process layout"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An automobile assembly line where cars move continuously past work stations is an example of:",
    "pilihan": [
        "Process layout",
        "Fixed-position layout",
        "Product layout",
        "Cellular layout",
        "Rapid response layout"
    ],
    "jawaban_benar": "Product layout"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A factory produces 500 units using 50 hours of labour and $5,000 of materials. If only labour is used as input, what is labour productivity?",
    "pilihan": [
        "5 units/hour",
        "10 units/hour",
        "50 units/hour",
        "100 units/hour",
        "0.1 units/hour"
    ],
    "jawaban_benar": "10 units/hour"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Just-in-Time (JIT) inventory management aims to:",
    "pilihan": [
        "Maximise stock levels to prevent shortages",
        "Receive goods only as they are needed in the production process, reducing holding costs",
        "Purchase raw materials in large bulk quantities",
        "Maintain large finished goods warehouses",
        "Outsource all inventory management to suppliers"
    ],
    "jawaban_benar": "Receive goods only as they are needed in the production process, reducing holding costs"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company acquires one of its key suppliers to gain control over raw material supply. This is an example of:",
    "pilihan": [
        "Forward vertical integration",
        "Horizontal integration",
        "Backward vertical integration",
        "Outsourcing",
        "Low-cost strategy"
    ],
    "jawaban_benar": "Backward vertical integration"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "An operations strategy that competes by delivering orders faster than competitors is BEST described as:",
    "pilihan": [
        "Differentiation strategy",
        "Low-cost strategy",
        "Rapid response strategy",
        "Vertical integration",
        "Market-seeking strategy"
    ],
    "jawaban_benar": "Rapid response strategy"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Work-in-Progress (WIP) inventory refers to:",
    "pilihan": [
        "Finished products waiting to be shipped",
        "Maintenance, repair, and operations supplies",
        "Goods that are partially completed within the production process",
        "Raw materials stored in a warehouse",
        "Products returned by customers"
    ],
    "jawaban_benar": "Goods that are partially completed within the production process"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A retailer decides to open a new store at a high-traffic shopping mall rather than an industrial zone. This location decision is driven primarily by:",
    "pilihan": [
        "Minimising labour costs",
        "Maximising revenue through footfall and accessibility",
        "Reducing transport costs for raw materials",
        "Proximity to manufacturing plants",
        "Government subsidies"
    ],
    "jawaban_benar": "Maximising revenue through footfall and accessibility"
},

# W11 – International Business and Marketing
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A mining company expands into Africa primarily to access lithium deposits. This BEST illustrates which motive for internationalisation?",
    "pilihan": [
        "Market-seeking",
        "Efficiency-seeking",
        "Resource-seeking",
        "Talent-seeking",
        "Cultural-seeking"
    ],
    "jawaban_benar": "Resource-seeking"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A tech company shifts manufacturing to Vietnam to take advantage of lower labour costs. This is an example of:",
    "pilihan": [
        "Market-seeking motive",
        "Resource-seeking motive",
        "Efficiency-seeking motive",
        "Knowledge-seeking motive",
        "Promotional motive"
    ],
    "jawaban_benar": "Efficiency-seeking motive"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A foreign manager dismisses local business customs as inferior to those practiced in her home country. This attitude is called:",
    "pilihan": [
        "Cultural shock",
        "Power distance",
        "Ethnocentrism",
        "Uncertainty avoidance",
        "Collectivism"
    ],
    "jawaban_benar": "Ethnocentrism"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "According to Hofstede's dimensions, a society where employees expect managers to make decisions with little consultation and where hierarchical differences are widely accepted scores HIGH on:",
    "pilihan": [
        "Individualism",
        "Uncertainty avoidance",
        "Power distance",
        "Achievement orientation",
        "Long-term orientation"
    ],
    "jawaban_benar": "Power distance"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Japan's tendency to prefer group harmony, consensus, and loyalty to the company over individual achievement reflects HIGH:",
    "pilihan": [
        "Power distance",
        "Uncertainty avoidance",
        "Individualism",
        "Collectivism",
        "Achievement orientation"
    ],
    "jawaban_benar": "Collectivism"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A company sells its product at the same price worldwide to maintain a consistent global brand image. This pricing approach is called:",
    "pilihan": [
        "Cost-plus pricing",
        "Penetration pricing",
        "Adapted pricing",
        "Standardised pricing",
        "Skimming pricing"
    ],
    "jawaban_benar": "Standardised pricing"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A food company redesigns its product packaging and removes certain ingredients to comply with the regulations of a host country. This is a response to which international environment?",
    "pilihan": [
        "Economic environment",
        "Cultural environment",
        "Legal-political environment",
        "Promotional environment",
        "Infrastructure environment"
    ],
    "jawaban_benar": "Legal-political environment"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A country's GDP per capita, infrastructure quality, and consumer purchasing power are key indicators of which international environment?",
    "pilihan": [
        "Legal-political environment",
        "Cultural environment",
        "Economic environment",
        "Competitive environment",
        "Technological environment"
    ],
    "jawaban_benar": "Economic environment"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "The 'Place' element of the marketing mix in an international context is MOST affected by which environmental factor?",
    "pilihan": [
        "Promotional budget",
        "Product design preferences",
        "Legal, economic, and cultural environments shaping distribution channels",
        "Company headquarters location",
        "Standardised pricing policies"
    ],
    "jawaban_benar": "Legal, economic, and cultural environments shaping distribution channels"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "A society that prefers strict rules, structured environments, and is uncomfortable with ambiguity scores HIGH on Hofstede's dimension of:",
    "pilihan": [
        "Power distance",
        "Individualism",
        "Achievement orientation",
        "Uncertainty avoidance",
        "Long-term orientation"
    ],
    "jawaban_benar": "Uncertainty avoidance"
},


# =========================
# 10 USE CASE (ESSAY) QUESTIONS
# =========================

# USE CASE 1 – Control (W5)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 1,
    "judul": "Case 1 – Riverside Bakery Chain",
    "bacaan": """
Riverside Bakery Chain operates 12 outlets across New Zealand. The operations director, 
Marcus, has recently noticed inconsistencies in product quality and customer satisfaction 
across different branches. Some outlets are thriving; others are struggling.

To address this, Marcus introduces a formal control system. He begins by setting clear 
standards: each outlet must achieve a minimum customer satisfaction score of 85%, waste 
must not exceed 5% of daily production, and all staff must complete food safety training 
within 30 days of starting. Marcus then collects performance data monthly through customer 
surveys, POS system reports, and branch manager walk-throughs.

After comparing data across outlets, Marcus finds that three branches consistently fall 
below the customer satisfaction benchmark. Rather than intervening in every minor deviation, 
he focuses resources on these underperforming branches. He meets with their managers, 
investigates root causes, and implements targeted retraining programmes.

However, some branch managers have complained that the system is too rigid, leaving them 
no room to adapt to local customer preferences. One manager noted: 'We are so focused on 
hitting the 85% score that we forget what actually makes customers happy here.'
""",
    "pertanyaan": "Question: Identify and explain TWO roles that the control system plays in Riverside Bakery Chain. Then, using evidence from the case, identify ONE barrier to effective control that is evident and explain how Marcus could address it to improve the control system."
},

# USE CASE 2 – Teams & HRM (W6)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 2,
    "judul": "Case 2 – Pinnacle Software Solutions",
    "bacaan": """
Pinnacle Software Solutions recently formed a new product development team of eight 
members drawn from different departments — engineering, design, marketing, and finance. 
The team was brought together to develop a new customer management application within 
six months.

In the first two weeks, team members were polite but hesitant to share ideas, and 
most deferred to the team leader on all decisions. By week four, however, tensions 
surfaced. Engineers and designers disagreed sharply on the product's core features, 
with each side convinced their approach was superior. The team leader, Priya, held 
weekly meetings to air these concerns.

By the third month, the team had agreed on a shared design framework and members 
were collaborating effectively. Individual contributions were clearly visible through 
a shared project management board, which Priya believed helped maintain accountability. 
However, Priya noticed that one team member, Daniel, was consistently contributing 
less than others, relying on the rest of the team to deliver results.

To recruit the next project team, Priya plans to use AI-based CV screening to shortlist 
candidates more efficiently before conducting structured behavioural interviews.
""",
    "pertanyaan": "Question: Using Tuckman's stages of team development, identify and describe THREE stages evident in the case study, supporting each with specific evidence. Then, identify the team dynamic issue affecting Daniel and explain ONE strategy Priya could use to address it."
},

# USE CASE 3 – Business Ethics & CSR (W7)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 3,
    "judul": "Case 3 – GreenPower Energy",
    "bacaan": """
GreenPower Energy is a renewable energy company operating in Southeast Asia. The 
company recently secured a contract to build a large solar farm on land that is 
legally zoned for industrial use. However, the land borders a local village whose 
residents depend on the adjacent river for drinking water and agriculture. 
Environmental consultants warned that construction could risk contaminating the river.

The CEO, David, faces a difficult decision. Proceeding with the project will generate 
significant profits and create 200 local jobs. Abandoning it will cost the company the 
contract and disappoint shareholders. David considers several ethical principles. His 
legal team confirms the project is entirely lawful.

Despite being legal, several senior managers argue the company has a broader 
responsibility to the community. GreenPower's mission statement reads: 'We create 
energy for a better world — for people, planet, and profit.' The company also has an 
established annual programme donating 1.5% of profits to local environmental restoration 
projects.

After weeks of deliberation, David decides to redesign the construction plan to include 
water protection measures, even though this increases costs by 12%.
""",
    "pertanyaan": "Question: Explain the ethical dilemma facing GreenPower Energy. Then, identify and explain TWO of Carroll's CSR responsibilities evident in this case, providing evidence from the case study for each. Finally, identify ONE ethical principle that appears to guide David's final decision and justify your answer."
},

# USE CASE 4 – Diversity (W8)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 4,
    "judul": "Case 4 – Horizon Consulting Group",
    "bacaan": """
Horizon Consulting Group is a management consulting firm based in Auckland, New Zealand. 
The firm employs 120 staff across five offices. A recent internal audit revealed 
concerning patterns: women occupy only 18% of senior leadership roles despite 
comprising 52% of total staff. Pasifika and Māori employees earn on average 22% less 
than their Pākehā counterparts in equivalent roles.

The audit also found that recruitment interviews consistently favoured candidates 
who graduated from three specific universities, regardless of actual job performance 
data. One hiring manager, when asked about this pattern, stated: 'Those graduates 
just seem more professional — it's hard to explain.'

In response, the CEO announced several initiatives. All employees will now receive 
identical professional development budgets regardless of role or seniority. 
Additionally, the firm will introduce blind CV screening to remove names and 
university details before shortlisting.

One senior partner argued: 'Giving everyone the same budget is fair.' Another 
partner disagreed, suggesting that junior Pasifika staff needed greater investment 
to overcome existing disadvantages.
""",
    "pertanyaan": "Question: Identify and explain TWO forms of bias or discrimination evident in the Horizon Consulting Group case, supporting each with specific evidence. Then, explain the distinction between equality and equity using the professional development budget debate as your example, and justify which approach you believe would be more effective for Horizon Consulting Group."
},

# USE CASE 5 – Entrepreneurship (W9)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 5,
    "judul": "Case 5 – Kai Box",
    "bacaan": """
Nina Tane grew up watching her grandmother prepare traditional Māori kai (food) for 
community gatherings in Rotorua. After completing a business degree and working two 
years in corporate marketing, Nina felt disconnected from her culture and yearned for 
something more meaningful.

In 2022, Nina identified a gap in the market: busy urban New Zealanders, particularly 
those with Māori and Pacific backgrounds, had no convenient way to access traditional 
home-cooked meals. She launched 'Kai Box', a subscription meal-kit service delivering 
pre-portioned ingredients and recipe cards for authentic traditional New Zealand dishes.

Nina invested $15,000 of her savings and secured a $30,000 loan from a Māori 
development fund. She partnered with local suppliers — many of them small Māori-owned 
farms — to source ingredients. Nina openly acknowledged that she was entering a crowded 
meal-kit market, but believed her cultural differentiation and community connections 
gave Kai Box a unique advantage.

Within 18 months, Kai Box had 3,500 subscribers and had partnered with two 
supermarket chains for limited retail distribution. Nina continues to reinvest profits 
into expanding the recipe range and hiring local Māori chefs to develop new products.
""",
    "pertanyaan": "Question: Identify and explain THREE components of the entrepreneurial process evident in the Kai Box case study. For each component, provide specific evidence from the case to justify your answer."
},

# USE CASE 6 – Operations Management (W10)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 6,
    "judul": "Case 6 – TechPrint Manufacturing",
    "bacaan": """
TechPrint Manufacturing produces customised electronic circuit boards for industrial 
clients. Each order is unique, requiring different configurations, components, and 
testing protocols. Production runs are typically small — between 5 and 50 units per 
order — but the range of products is vast, with over 400 different board types 
manufactured in any given month.

The operations manager, Lena, organises the factory so that all drilling machines 
are grouped together in one area, soldering stations in another, and quality testing 
stations in a third. Operators are skilled specialists in their respective stations.

Lena is now evaluating whether to outsource the soldering process to a specialist 
subcontractor in Malaysia, which would reduce per-unit soldering costs by 30%. However, 
this would mean losing direct oversight of a critical quality-sensitive process. Lena 
also recently invested in automated testing equipment, which has improved defect 
detection by 40% and reduced rework time by 25%.

TechPrint measures productivity monthly. Last month, the factory produced 8,000 boards 
using 400 hours of labour and $120,000 of materials and overheads combined.
""",
    "pertanyaan": "Question: Identify and justify the facilities layout used at TechPrint Manufacturing, providing evidence from the case. Then, calculate TechPrint's single-factor labour productivity and multi-factor productivity for last month, showing your working. Finally, discuss the make-or-buy decision facing Lena regarding the soldering process, explaining the key trade-offs she should consider."
},

# USE CASE 7 – Supply Chain (W10)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 7,
    "judul": "Case 7 – FreshFlow Grocers",
    "bacaan": """
FreshFlow Grocers is a supermarket chain operating 35 stores throughout New Zealand. 
The company has built a reputation for fresh, locally sourced produce delivered daily 
to each store. To maintain this, FreshFlow operates a just-in-time (JIT) replenishment 
system, where suppliers deliver fresh produce directly to distribution centres each 
morning based on the previous day's sales data.

Recently, FreshFlow acquired PureRoots, a small organic farm cooperative that had 
been supplying 40% of its fresh produce. The acquisition was driven by concerns about 
supply reliability and rising wholesale prices.

The company is also considering whether to acquire TransLink, a national transport and 
logistics company that currently handles 60% of FreshFlow's deliveries. This would give 
FreshFlow full control over its delivery scheduling, reduce dependence on third-party 
logistics, and potentially lower delivery costs in the long run.

Some board members have raised concerns about expanding outside the company's core 
retail competency, arguing that managing farms and transport fleets introduces 
complexity and risk that could distract from serving customers.
""",
    "pertanyaan": "Question: Explain how FreshFlow's JIT system functions as a supply chain strategy and identify ONE advantage and ONE disadvantage of this approach for FreshFlow. Then, classify the acquisition of PureRoots and the proposed acquisition of TransLink using integration strategy concepts, explaining the strategic rationale for each. Finally, evaluate the board members' concern, using supply chain management concepts to support your argument."
},

# USE CASE 8 – International Business (W11)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 8,
    "judul": "Case 8 – Kiwi Sport Co.",
    "bacaan": """
Kiwi Sport Co. is a New Zealand-based sporting goods manufacturer that has decided 
to expand into three new markets: Germany, Indonesia, and the United Arab Emirates (UAE).

Before entering each market, the management team conducted thorough environmental 
analyses. In Germany, strict consumer protection laws and product safety regulations 
required the company to redesign its helmet range. In Indonesia, the management team 
discovered that consumers had lower average purchasing power, and reliable logistics 
infrastructure was limited outside major cities. In the UAE, the team found that 
business relationships were built on personal trust and long-term connections, and 
that Emirati business culture placed high importance on respect for hierarchy.

The company plans to sell its products at a consistent global price to maintain brand 
prestige. However, the marketing team is proposing that promotional campaigns be 
tailored to each market's cultural values — for example, emphasising team spirit and 
collective achievement in Indonesia, while focusing on individual performance and 
personal records in Germany.

One senior manager expressed frustration: 'We should just market the same way 
everywhere — what works at home should work abroad.'
""",
    "pertanyaan": "Question: For EACH of the three markets (Germany, Indonesia, UAE), identify the specific international environment (legal-political, economic, or cultural) most evident in the case and explain how it affects Kiwi Sport Co.'s operations. Then, explain TWO of Hofstede's cultural dimensions that are relevant to Kiwi Sport Co.'s experience in Indonesia and the UAE, applying them to the case. Finally, evaluate the senior manager's comment about standardising marketing, using evidence from the case to support your answer."
},

# USE CASE 9 – HRM & Selection (W6)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 9,
    "judul": "Case 9 – Summit Hotels Group",
    "bacaan": """
Summit Hotels Group is a luxury hotel chain recruiting Guest Experience Managers for 
its five Auckland properties. The HR manager, Talia, is redesigning the selection 
process after a high turnover rate among recently hired managers — 60% left within 
their first year.

Talia's investigation revealed several problems with the previous process. Candidates 
had been told only about the positive aspects of the role during interviews — the 
exciting events, the career growth opportunities, and the prestige of the brand. No 
mention was made of the demanding shift work, high-pressure guest complaints, or the 
requirement to work public holidays. Most departing managers cited 'unmet expectations' 
as their primary reason for leaving.

The previous selection process involved only a CV review and a single informal 
interview. There were no reference checks and no formal testing. Talia proposes a 
revised process: structured behavioural interviews using the STAR technique, a 
situational judgement test, reference checks, and a revised job advertisement that 
honestly describes both the rewards and the challenges of the role.

Additionally, Talia is considering using an AI platform to pre-screen CVs to manage 
the high volume of applications. A colleague warns that AI screening tools have 
produced biased shortlists in the hospitality industry.
""",
    "pertanyaan": "Question: Explain the concept of a Realistic Job Preview (RJP) and discuss how the absence of an RJP contributed to Summit Hotels' turnover problem. Then, describe how the STAR technique should be applied in Summit Hotels' behavioural interviews, providing a specific example question and an ideal response structure relevant to the Guest Experience Manager role. Finally, critically evaluate Talia's proposal to use AI for CV pre-screening, identifying ONE advantage and ONE significant risk, and recommend whether Summit Hotels should proceed."
},

# USE CASE 10 – Ethics & Diversity (W7 + W8)
{
    "tipe": "use_case_essay",
    "nomor_kasus": 10,
    "judul": "Case 10 – ClearPath Pharmaceutical",
    "bacaan": """
ClearPath Pharmaceutical is a mid-sized company that manufactures generic medicines 
for developing markets. The company recently developed a low-cost malaria treatment 
that could save thousands of lives annually in Sub-Saharan Africa. However, to 
distribute the product, ClearPath must obtain regulatory approval in each target country.

In one country, a government official privately told ClearPath's regional manager 
that approval could be 'fast-tracked' in exchange for a consulting fee paid to 
the official's private company. The regional manager believes this is a common 
practice in the region and could save six months of delays. The company's legal 
team confirms that while the payment might violate the company's own code of conduct, 
it may not technically breach local law in that jurisdiction.

Meanwhile, ClearPath's internal diversity audit found that all 12 members of its 
executive leadership team are men over 50, and that the company's performance 
appraisal system consistently rates female scientists lower than male peers — despite 
equivalent publication records and project outcomes. Female scientists reported 
feeling that their contributions were less valued, and several high-performing women 
had resigned in the past year.

The CEO, Robert, acknowledges both issues but is unsure how to prioritise and 
address them given limited time and resources.
""",
    "pertanyaan": "Question: Identify and explain the ethical dilemma facing ClearPath's regional manager regarding the 'consulting fee', applying at least TWO of the five principles of ethical decision-making to evaluate the appropriate course of action. Then, identify and explain TWO diversity and inclusion issues present at ClearPath Pharmaceutical, providing evidence from the case for each. Finally, using Carroll's CSR Pyramid, explain which level of responsibility ClearPath is failing to meet in each of the two situations, and recommend one concrete action for each."
},

]

# =========================
# PAGE HEADER
# =========================
st.title("📚 MGMT100 Exam Practice Quiz")
st.markdown("**Weeks 5–11 | 50 Multiple Choice + 10 Use Case Essay Questions**")
st.markdown("---")

# =========================
# SESSION STATE
# =========================
if "submitted_mc" not in st.session_state:
    st.session_state.submitted_mc = False
if "submitted_uc" not in st.session_state:
    st.session_state.submitted_uc = False

# Separate into MCQ and use case
mcq_list = [s for s in soal_list if s["tipe"] == "pilihan_ganda"]
uc_list = [s for s in soal_list if s["tipe"] == "use_case_essay"]

tab1, tab2 = st.tabs(["📝 Part A – Multiple Choice (50 Questions)", "📖 Part B – Use Case Essays (10 Questions)"])

# =========================
# TAB 1: MULTIPLE CHOICE
# =========================
with tab1:
    st.markdown("### Instructions")
    st.info("Select the best answer for each question. Click **Submit Answers** when finished to see your score and feedback.")
    st.markdown("---")

    score = 0
    total = len(mcq_list)

    for i, soal in enumerate(mcq_list):
        week_labels = {
            0: "W5", 1: "W5", 2: "W5", 3: "W5", 4: "W5", 5: "W5", 6: "W5",
            7: "W6", 8: "W6", 9: "W6", 10: "W6", 11: "W6", 12: "W6", 13: "W6", 14: "W6",
            15: "W7", 16: "W7", 17: "W7", 18: "W7", 19: "W7", 20: "W7",
            21: "W8", 22: "W8", 23: "W8", 24: "W8", 25: "W8",
            26: "W9", 27: "W9", 28: "W9", 29: "W9", 30: "W9",
            31: "W10", 32: "W10", 33: "W10", 34: "W10", 35: "W10", 36: "W10", 37: "W10", 38: "W10",
            39: "W11", 40: "W11", 41: "W11", 42: "W11", 43: "W11", 44: "W11", 45: "W11", 46: "W11", 47: "W11", 48: "W11", 49: "W11"
        }
        label = week_labels.get(i, "")
        st.markdown(f"**Question {i+1}** `{label}`")
        key = f"mc_{i}"
        st.radio(soal["pertanyaan"], soal["pilihan"], key=key, index=None)

        if st.session_state.submitted_mc:
            user = st.session_state.get(key)
            if user == soal["jawaban_benar"]:
                score += 1
                st.success("✅ Correct")
            else:
                st.error(f"❌ Incorrect. Correct answer: **{soal['jawaban_benar']}**")

        st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Submit MCQ Answers", use_container_width=True, key="submit_mc"):
            st.session_state.submitted_mc = True
            st.rerun()

    if st.session_state.submitted_mc:
        percent = score / total * 100
        if percent >= 80:
            st.success(f"🎉 Your Score: **{score}/{total} ({percent:.1f}%)**")
        elif percent >= 60:
            st.warning(f"📊 Your Score: **{score}/{total} ({percent:.1f}%)** — Keep studying!")
        else:
            st.error(f"📉 Your Score: **{score}/{total} ({percent:.1f}%)** — Review your notes and try again.")

        with col2:
            if st.button("🔄 Reset MCQ", use_container_width=True, key="reset_mc"):
                for k in list(st.session_state.keys()):
                    if k.startswith("mc_"):
                        del st.session_state[k]
                st.session_state.submitted_mc = False
                st.rerun()

# =========================
# TAB 2: USE CASE ESSAYS
# =========================
with tab2:
    st.markdown("### Instructions")
    st.warning("""
**This section requires written essay responses.**  
Read each case study carefully, then write a structured essay answer in the text area provided.  
Your answer should:
- **Define** relevant concepts
- **Apply** them directly to the case study using specific evidence
- **Explain** the connection clearly
- Use **examples from the case** to justify your points

After submitting, use the **model answer guide** to self-assess your response.
""")
    st.markdown("---")

    for i, soal in enumerate(uc_list):
        st.markdown(f"## Case Study {soal['nomor_kasus']}: {soal['judul']}")

        with st.expander("📄 Read the Case Study", expanded=True):
            st.markdown(f"""
<div style='background-color:#f0f4f8; padding:20px; border-radius:8px; border-left:4px solid #2563eb; font-size:15px; line-height:1.7'>
{soal["bacaan"]}
</div>
""", unsafe_allow_html=True)

        st.markdown(f"**📝 {soal['pertanyaan']}**")

        key = f"uc_{i}"
        st.text_area(
            "Write your essay answer here:",
            key=key,
            height=300,
            placeholder="Start your answer here. Aim for a structured response: define concepts → apply to case → use evidence → explain significance."
        )

        st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💾 Save My Essays", use_container_width=True, key="submit_uc"):
            st.session_state.submitted_uc = True
            st.rerun()

    if st.session_state.submitted_uc:
        st.success("✅ Essays saved! Use the self-assessment checklist below to review your responses.")
        with st.expander("📋 Self-Assessment Checklist", expanded=True):
            st.markdown("""
**Use this checklist to evaluate each of your essay responses:**

- ☐ Did I **define** the key concept(s) accurately and in my own words?
- ☐ Did I **identify** the specific concept, framework, or model required by the question?
- ☐ Did I **apply** the concept directly to the case study — not just describe it generally?
- ☐ Did I **use specific evidence** (names, events, quotes) from the case to support my points?
- ☐ Did I **explain** the significance or impact of the concept for the organisation?
- ☐ Did I address **all parts** of the question (e.g., if asked for two examples, did I give two)?
- ☐ Is my response **well-structured** (clear introduction, body, conclusion or logical flow)?
- ☐ Have I **avoided** simply summarising the case without linking to theory?
            """)

        with col2:
            if st.button("🔄 Reset Essays", use_container_width=True, key="reset_uc"):
                for k in list(st.session_state.keys()):
                    if k.startswith("uc_"):
                        del st.session_state[k]
                st.session_state.submitted_uc = False
                st.rerun()