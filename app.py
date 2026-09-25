import streamlit as st
st.set_page_config(page_title="统计抽样计算器")
st.title("统计抽样计算器")

# 分层抽样
st.subheader("分层抽样")
male = st.number_input("男性人数", value=4892)
female = st.number_input("女性人数", value=4563)
sample_total = st.number_input("抽取总样本数量", value=2823)
total_pop = male + female
male_sample = male / total_pop * sample_total
st.write(f"应抽取男性样本：{male_sample:.2f}")

# 系统抽样
st.subheader("系统抽样")
start_num = st.number_input("起点编号", value=10)
interval = st.number_input("抽样间隔k", value=75)
result_list = [start_num + i * interval for i in range(6)]
st.write("6个抽样编号：", result_list)

# 简单随机抽样
st.subheader("简单随机抽样")
st.write("随机数表抽样")