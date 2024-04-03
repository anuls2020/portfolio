import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Anu L Sasidharan")
    content = """
    This is my portfolio website. Driven by results and enthusiasm, I bring over 14 years of extensive experience 
    in directing Hadoop Cluster Administration, CDP-Cloudera Data Platform, Backup and Disaster Recovery, 
    Hadoop Security, and Cloud services such as AZURE, AWS, and GCP. I have a stellar reputation for delivering projects
    within scope, maintaining quality, and meeting deadlines. My expertise includes managing big data frameworks like 
    Hadoop (HDFS + MapReduce) and its components like YARN, HIVE, HBase, Spark, and Kafka, along with proficiency in 
    Python and Bash scripting. I have hands-on experience in implementing Hadoop security measures such as 
    Kerberos (Active Directory & MIT), TLS/SSL, Sentry, Knox, Ranger, Encryption (At Rest and Motion), and managing 
    HDFS and HBase ACLs. With a detail-oriented approach, I excel in multitasking within competitive, multiplatform, 
    and fast-paced environments.
    """
    st.info(content)

content2 = """
Below you can find some app which I have developed in Python. Feel free to contact me!..
"""
st.header(content2)
# st.write(content2)

# accessing the data.csv file to import the data into the website.

df = pd.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])