import streamlit as st
st.set_page_config(page_title="傻逼检测器")
st.title("傻逼检测器")

name = st.text_input("请输入您的名字")
if name =="林君锐" or name == "ljr" or name == "lwh" or name == "林伟豪":
    st.text_write("大傻逼")
elif name == "xyx" or name == "薛煜翔" or name == "lzy" or name == "林子瑶":
    st.text_write("不是傻逼")
else:
    st.text_write("挺傻逼")
    