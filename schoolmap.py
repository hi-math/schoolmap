#10_schoolmap.py

import streamlit as st
import pandas as pd



st.title("서울 학교 위치 검색")

df = pd.read_csv("학교정보.csv")

with st.sidebar.form("학교정보"):
    st.write("학교정보검색")
    school_name = st.text_input("학교이름","")
    school_level = st.multiselect("학교급",df["학교종류명"].unique())
    foundation = st.multiselect("설립구분",df["설립구분"].unique())
    school_gender = st.multiselect("남녀공학구분",df["남녀공학구분명"].unique())
    open_year = st.slider("설립 연도",
         int(round(df["설립일자"].min()/10000,0)-1),
         int(round(df["설립일자"].max()/10000,0)+1),
         (int(round(df["설립일자"].min()/10000,0)-1),int(round(df["설립일자"].max()/10000,0)+1))
         )
    button = st.form_submit_button("검색")

print(school_name)

if button:
    
    if school_name=="":
        pass
    else:
        df = df[df["학교명"].str.contains(school_name)]

    if school_level:    
        df = df[df["학교종류명"].isin(school_level)]
    
    if foundation:    
        df = df[df["설립구분"].isin(foundation)]
    
    if school_gender :
        df = df[df["남녀공학구분명"].isin(school_gender)]
    
    if open_year:
        df = df[(df["설립일자"]>open_year[0]*10000) & (df["설립일자"]<open_year[1]*10000)]
        
    df = df.reset_index()
    
    st.write(df)
    
    st.map(df,latitude='latitude',longitude='longitude',color='color', size=150)

with st.expander("색상구분"):
    st.write(":red[고등학교], :blue[중학교], :green[초등학교]")



