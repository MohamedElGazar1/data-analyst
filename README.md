# data-analyst
nsightful Analysis of IT Salaries Across Europe

📍 Overview
This project aims to analyze Job tilte and salary trends among IT professionals in various European countries over a three-year period using data collected from anonymous annual surveys. The goal is to extract meaningful insights into how factors like experience, job role, location, and tech stack influence compensation across the continent.

The dataset spans three years:

IT Salary Survey EU 2018.csv
T Salary Survey EU 2019.csv
IT Salary Survey EU 2020.csv
Each file contains anonymized responses from IT professionals, offering valuable information on demographics, job roles, salaries, company types, and etc...

🔍 Objectives
merge and clean datasets from 2018, 2019, and 2020.
Identify key patterns and correlations between salary and professional attributes.
Visualize geographic and occupational trends in IT earnings.
Compare salary growth year-over-year.
Provide actionable insights for HR departments, job seekers, and policymakers.
🧾 Dataset Highlights
Year	Key Features
2018	Age, Gender, Location, Job Title, Experience, Salary
2019	Seniority Level, Tech Stack, Industry, Company Size
2020	Employment Type, Remote Work Option, Bonus, Contract Type
🛠 Technical Approach
1. Data Cleaning
Handle missing or inconsistent values (e.g., drop or impute).
Convert currency and numeric fields to uniform formats.
Clean categorical variables (e.g., unify "Java" vs "java", "Full-stack" vs "Fullstack").
Remove outliers using statistical methods like IQR or Z-score.
2. Feature Engineering
Derive new metrics such as:
Salary per year of experience
Total Compensation = Base Salary + Bonus
Experience-to-Salary Ratio
Encode categorical features:
Use One-Hot Encoding for nominal categories (e.g., city, industry)
Use Ordinal Encoding for ordered categories (e.g., seniority levels)
3. Exploratory Data Analysis (EDA)
Calculate summary statistics (mean, median, min/max salaries).
Analyze salary distributions by:
Country/City
Job Role
Experience Level
Tech Stack
Explore relationships using correlation matrices and scatter plots.
Create grouped visualizations (e.g., average salary per job title in each country).
4. Visualization Strategy
Use *Matplotlib, **Seaborn, and optionally *Plotly for:
Heatmaps showing salary distribution across cities
Bar charts comparing top-paying roles
Line graphs tracking salary changes over time
Boxplots analyzing salary spread by experience level
Cluster maps identifying high-tech hubs
📦 Deliverables
A cleaned and merged dataset
Colab containing EDA and visualization code
Final report summarizing findings and trends
Optional: Interactive dashboard using Plotly/Dash or Streamlit
🧪 Tasks & Libraries
Task	Library
Data Manipulation	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Dashboard (Optional)	Plotly, Streamlit
Documentation	GitHub Pages
💡 Sample Research Questions
Question	Purpose
Which job titles earn the highest salaries?	Understand market demand for specific skills
How has salary changed from 2018 to 2020?	Track economic shifts and tech evolution
What are the top-paying cities in Europe?	Guide relocation decisions for developers
How does remote work affect compensation?	Analyze post-pandemic employment dynamics
Which programming languages correlate with higher pay?	Inform career development choices
📁 Folder Structure Proposal
it-salary-analysis/ │ ├── data/ │ ├── raw/ │ │ ├── IT_Salary_Survey_EU_2018.csv │ │ ├── T_Salary_Survey_EU_2019.csv │ │ └── IT_Salary_Survey_EU_2020.csv │ └── processed/ │ └── combined_salary_data.csv │ ├── notebooks/ │ ├── 1_data_integration.ipynb │ ├── 2_cleaning_and_preprocessing.ipynb │ ├── 3_exploratory_analysis.ipynb │ └── 4_visualization.ipynb │ ├── reports/ │ ├── findings_summary.md │ └── visual_dashboard.html (optional) │ └── README.md

✅ Benefits of This Analysis
Helps job seekers understand salary expectations based on their profile.
Assists companies in benchmarking competitive compensation packages.
Provides insights into which technologies are most valued in the job market.
Reveals geographic hotspots for IT opportunities.
