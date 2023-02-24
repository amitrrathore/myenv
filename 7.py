import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
st.write("""
# File Picker
""")
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = uploaded_file.getvalue().decode('utf-8').splitlines()         
    st.session_state["preview"] = ''
    
df = pd.read_csv(uploaded_file, delimiter='\t',header = None,names=range(82))

# st.write(df)
df = df.iloc[:, [0, 1,3,50]]


# st.write(df.dtypes)

# st.write(df)
index = df.index[df.iloc[:, 0] == 'Sample Name'][0]
df = df.iloc[index:]
df = df.reset_index(drop=True)
df.columns = df.iloc[0]
df = df.drop(df.index[0])
df = df.dropna(subset=['Sample Comment'])
df = df.sort_values('Sample ID')
df=df.replace(to_replace=["No Peak","< 0"],
           value=int(0))
# st.write(df.dtypes)
# df['Sample Comment'] = df['Sample Comment'].astype(float)
# st.write(df.dtypes)
df["Sample Comment"] = df["Sample Comment"].astype(float)

df=df.sort_values(by=['Sample ID','Sample Name','Sample Comment'],ascending=[True,True,True])


# st.write(df.dtypes)


# display the chart in streamlit
# st.altair_chart(chart, use_container_width=True)

# st.write(df)

chart=alt.Chart(df).mark_line(point=True).encode(
    y='Calculated Concentration (ng/mL)',
    x='Sample Comment:N',
    color='Sample ID',
).properties(
    width=1000,
    height=600,
)

st.altair_chart(chart)

l1=[]
for i in df['Sample ID']:
    if i not in l1:
        l1.append(i)

df1 = df[df['Sample ID'] == l1[0]]
# st.write(df1)
df1 = df1.reset_index(drop=True)
# st.write(df1)
df1["Sample Comment"] = df1["Sample Comment"].astype(float)
df=df.sort_values(by=['Sample ID','Sample Name','Sample Comment'],ascending=[True,True,True])
# # display the chart in streamlit
# # st.altair_chart(chart, use_container_width=True)
# st.write(df)

chart1=alt.Chart(df1).mark_line(point=True).encode(
    y='Calculated Concentration (ng/mL)',
    x='Sample Comment:N',
    color='Sample ID',
).properties(
    width=1000,
    height=500,
)
st.altair_chart(chart1)




















df2 = df[df['Sample ID'] == l1[1]]
# st.write(df2)
df2= df2.reset_index(drop=True)
# st.write(df2)
df2["Sample Comment"] = df2["Sample Comment"].astype(float)
df=df.sort_values(by=['Sample ID','Sample Name','Sample Comment'],ascending=[True,True,True])
# # display the chart in streamlit
# # st.altair_chart(chart, use_container_width=True)
# st.write(df)

chart2=alt.Chart(df2).mark_line(point=True).encode(
    y='Calculated Concentration (ng/mL)',
    x='Sample Comment:N',
    color='Sample ID',
).properties(
    width=1000,
    height=500,
)
st.altair_chart(chart2)



df3 = df[df['Sample ID'] == l1[2]]
# st.write(df2)
# df3= df2.reset_index(drop=True)
# st.write(df2)
df3["Sample Comment"] = df3["Sample Comment"].astype(float)
df3=df3.sort_values(by=['Sample ID','Sample Name','Sample Comment'],ascending=[True,True,True])
# # display the chart in streamlit
# # st.altair_chart(chart, use_container_width=True)
# st.write(df)

chart3=alt.Chart(df3).mark_line(point=True).encode(
    y='Calculated Concentration (ng/mL)',
    x='Sample Comment:N',
    color='Sample ID',
).properties(
    width=1000,
    height=500,
)
st.altair_chart(chart3)


df4 = df[df['Sample ID'] == l1[3]]
# st.write(df2)
# df3= df2.reset_index(drop=True)
# st.write(df2)
df4["Sample Comment"] = df4["Sample Comment"].astype(float)
df4=df4.sort_values(by=['Sample ID','Sample Name','Sample Comment'],ascending=[True,True,True])
# # display the chart in streamlit
# # st.altair_chart(chart, use_container_width=True)
# st.write(df)

chart4=alt.Chart(df4).mark_line(point=True).encode(
    y='Calculated Concentration (ng/mL)',
    x='Sample Comment:N',
    color='Sample ID',
).properties(
    width=1000,
    height=500,
)
st.altair_chart(chart4)


