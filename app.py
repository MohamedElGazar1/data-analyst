
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Setup ---
st.set_page_config(page_title="Employee Insights Dashboard", layout="wide")
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# --- Load and clean data ---
@st.cache_data
def load_data():
    df = pd.read_csv("C:\Users\mn\PycharmProjects\data_analyst\mergeddd_output.csv")  # Adjust path as needed
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.title("Filters")

# Dropdown filter for Seniority level
seniority_levels = ['All'] + sorted(df['Seniority level'].dropna().unique().tolist())
selected_seniority = st.sidebar.selectbox("Select Seniority Level", seniority_levels)

# Dropdown filter for Position
positions = ['All'] + sorted(df['Position'].dropna().unique().tolist())
selected_position = st.sidebar.selectbox("Select Position", positions)

# Dropdown filter for Gender
genders = ['All'] + sorted(df['Gender'].dropna().unique().tolist())
selected_gender = st.sidebar.selectbox("Select Gender", genders)

# Filter dataframe based on dropdown selections
filtered_df = df.copy()

if selected_seniority != 'All':
    filtered_df = filtered_df[filtered_df['Seniority level'] == selected_seniority]

if selected_position != 'All':
    filtered_df = filtered_df[filtered_df['Position'] == selected_position]

if selected_gender != 'All':
    filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]

# ===== Summary Metrics Section =====
st.markdown("## 🧾 Summary Metrics")

col1, col2, col6 = st.columns(3)
col4, col5, col3, col7 = st.columns(4)

with col1:
    total_salary = filtered_df["Yearly salary"].sum()
    st.metric(label="💰 Total Salary", value=f"${total_salary:,.0f}")

with col2:
    avg_age = filtered_df["Age"].mean()
    st.metric(label="👤 Average Age", value=f"{avg_age:.1f} years")

with col3:
    most_city = filtered_df["City"].mode().iat[0] if "City" in filtered_df.columns and not filtered_df["City"].mode().empty else "N/A"
    st.metric(label="🏙️ Most Common City", value=most_city)

with col4:
    most_main = filtered_df["main technology"].mode().iat[0] if not filtered_df["main technology"].mode().empty else "N/A"
    st.metric(label="🛠️ Most Used Main Tech", value=most_main)

with col5:
    most_seniority = filtered_df["Seniority level"].mode().iat[0] if not filtered_df["Seniority level"].mode().empty else "N/A"
    st.metric(label="🎓 Most Common Seniority", value=most_seniority)

with col6:
    avg_exp = filtered_df["Total years of experience"].mean()
    st.metric(label="📈 Avg Experience", value=f"{avg_exp:.1f} years")

with col7:
    avg_vacation = filtered_df["Number of vacation days"].mean()
    st.metric(label="🌴 Avg Vacation Days", value=f"{avg_vacation:.1f} days")

st.markdown("---")

# ===== Tabs =====
tab1, tab2, tab3, tab4 = st.tabs([
    "Age", "Top", "Average", "Salary"
])

with tab1:
    st.header("Age Insights")

    # Age Distribution
    st.subheader("Age Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df["Age"].dropna(), bins=20, kde=True, ax=ax1)
    ax1.set_title("Age Distribution")
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

    # Respondents by Age Group
    st.subheader("Respondents by Age Group")
    bins = [15, 25, 35, 45, 55, 65]
    labels = ['16–25', '26–35', '36–45', '46–55', '56+']
    filtered_df['Age Group'] = pd.cut(filtered_df['Age'], bins=bins, labels=labels, right=False)
    age_group_counts = filtered_df['Age Group'].value_counts().sort_index()
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    sns.barplot(x=age_group_counts.index, y=age_group_counts.values, palette='coolwarm', ax=ax2)
    ax2.set_title('Count of Respondents by Age Group')
    ax2.set_xlabel('Age Group')
    ax2.set_ylabel('Count')
    st.pyplot(fig2)

with tab2:
    st.header("Top Insights")

    st.subheader("Top 10 Job Positions")
    top_positions = filtered_df["Position"].value_counts().nlargest(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_positions.values, y=top_positions.index, ax=ax, palette="viridis")
    ax.set_title("Top 10 Job Positions")
    ax.set_xlabel("Number of Employees")
    ax.set_ylabel("Position")
    st.pyplot(fig)

    st.subheader("Top 10 Main Technologies")
    top_tech = filtered_df['main technology'].value_counts().nlargest(10).index
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(data=filtered_df[filtered_df['main technology'].isin(top_tech)], y='main technology', order=top_tech, palette='coolwarm', ax=ax)
    ax.set_title("Top 10 Main Technologies")
    st.pyplot(fig)

    st.subheader("Top 5 Technologies Used by Senior Employees")
    senior_df = filtered_df[filtered_df['Seniority level'].str.contains("Senior", case=False, na=False)]
    top_tech_senior = senior_df['main technology'].value_counts().nlargest(5)
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(x=top_tech_senior.values, y=top_tech_senior.index, palette='crest', ax=ax)
    ax.set_title('Top 5 Technologies Used by Senior Employees')
    ax.set_xlabel('Number of Employees')
    ax.set_ylabel('Main Technology')
    st.pyplot(fig)

    st.subheader("Top 3 Contract Durations")
    contract_counts = filtered_df['Contract duration'].value_counts().head(3)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(contract_counts, labels=contract_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    ax.set_title('Top 3 Contract Durations')
    ax.axis('equal')
    st.pyplot(fig)

with tab3:
    st.header("Average Metrics by Position")

    st.subheader("Average Experience by Position")
    top_positions = filtered_df['Position'].value_counts().nlargest(10).index
    filtered_top = filtered_df[filtered_df['Position'].isin(top_positions)]
    avg_exp_by_position = filtered_top.groupby('Position')['Total years of experience'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots()
    sns.barplot(x=avg_exp_by_position.index, y=avg_exp_by_position.values, palette='coolwarm', ax=ax)
    ax.set_title("Top 10 Positions by Average Years of Experience")
    ax.set_xlabel("Position")
    ax.set_ylabel("Average Years of Experience")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Average Vacation Days by Position")
    vacation_by_position = filtered_top.groupby('Position')['Number of vacation days'].mean()
    fig, ax = plt.subplots()
    sns.barplot(x=vacation_by_position.index, y=vacation_by_position.values, palette='cubehelix', ax=ax)
    ax.set_title('Average Number of Vacation Days (Top 10 Positions)')
    ax.set_xlabel('Position')
    ax.set_ylabel('Average Vacation Days')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab4:
    st.header("Salary Insights")

    st.subheader("Average Salary by Top 7 Positions")
    top_positions = filtered_df['Position'].value_counts().nlargest(7).index
    filtered_top = filtered_df[filtered_df['Position'].isin(top_positions)]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=filtered_top, x='Position', y='Yearly salary', estimator='mean', palette='coolwarm', ax=ax)
    ax.set_title("Average Salary by Top 7 Job Positions")
    ax.set_ylabel("Average Salary")
    plt.xticks(rotation=45)
    st.pyplot(fig)


