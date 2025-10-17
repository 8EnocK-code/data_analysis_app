import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Student Performance Dashboard", page_icon="📊", layout="wide")
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>📘 Student Performance Dashboard</h1>
    <h4 style='text-align: center; color: gray;'>Analyze performance, trends & insights</h4>
    <hr style='border: 1px solid #eee;'>
""", unsafe_allow_html=True)

# File uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("📂 Upload your CSV file", type=["csv"])

# Default fallback dataset
@st.cache_data
def load_default_data():
    return pd.read_csv("Sales_converted.csv")

# Conditional logic for uploaded file
if uploaded_file is not None:
    # Don't cache uploads — they change often
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("✅ New file uploaded successfully!")
else:
    df = load_default_data()
    st.sidebar.info("ℹ️ Using default dataset")



st.write("📊 Calculating insights...")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)
st.success("✅ Analysis complete!")

uploaded = st.sidebar.file_uploader("Upload a CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.success("File uploaded successfully!")


df['Total_Marks'] = (df['English'] +  df['Maths'] + df['Kiswahili'] + df['Biology'] + df['Physics'] + df['Chemistry'] + df['History'] + df['Business'])
dr = df.sort_values(by= "Mean_Score", ascending=False)

def all_students():
    if st.sidebar.button('All_students'):
        st.title("End term overall ranking")
        st.write(dr.head(130))
all_students()
def top_ten():
    if st.sidebar.button('Top_students'):
        st.write("---------TOP TEN ANALYSIS--------------")
        st.write(dr.head(10))
        st.write(dr.head(10).describe().round(0))
        st.title("Count of each gender in top ten")
        st.write(dr.head(10)['Gender'].value_counts())
        st.title("Average mean for each subject")
        st.bar_chart(dr.head(10).describe().mean())
top_ten()

def bottom_ten():
    if st.sidebar.button('Bottom_students'):
        st.write("---------BOTTOM TEN ANALYSIS--------------")
        st.write(dr.tail(10))
        st.write(dr.tail(10).describe().round(0))
        st.title("Count of each gender in bottom ten")
        st.write(dr.tail(10)['Gender'].value_counts())
        st.title("Average mean for each subject")
        st.bar_chart(dr.tail(10).describe().mean())

bottom_ten()

gender_filter = st.sidebar.multiselect("Filter by Gender", df["Gender"].unique())
if gender_filter:
    df = df[df["Gender"].isin(gender_filter)]

def overall_insight():
    if st.sidebar.button('Conclusions'):
        st.subheader("📊 Overall Insights")
        st.markdown("""
### 💡 **Overall Insights**
- 👩 **Female students** performed better than **male students**
- 📚 Academic performance was **highly influenced by gender**
- 🧠 **Math & Biology** were top-performing subjects
- 🗣️ Top students excelled more in **Kiswahili** than English
- ⚠️ **Bottom students** performed weakest in **Kiswahili**
""")
overall_insight()

st.markdown("""
<hr>
<p style='text-align: center; color: gray;'>
Built with ❤️ by enockETH | Powered by Streamlit
</p>
""", unsafe_allow_html=True)
