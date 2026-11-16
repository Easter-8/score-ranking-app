
import streamlit as st

# 设置网页标题
st.set_page_config(page_title="成绩排名查询系统")
st.title("🏆 成绩排名查询系统")

# 网页上的输入框
raw_text = st.text_input("请输入查询数据（用空格隔开）：", "")

if st.button("✅ 校验并生成排名"):
    if not raw_text.strip():
        st.warning("输入不能为空，请重新输入！")
    else:
        user_input = raw_text.split()
        nums = []
        errors = []

        # 校验逻辑
        for n in user_input:
            try:
                num = float(n)
                if num >= 0:
                    nums.append(num)
                else:
                    errors.append(f"'{num}' 是负数")
            except ValueError:
                errors.append(f"'{n}' 不是纯数字")

        # 弹窗报错
        if errors:
            error_str = "，".join(errors)
            st.error(f"❌ 输入有误：{error_str}。请重新输入！")
        elif not nums:
            st.warning("没有有效的正数可以排名！")
        else:
            # 排名逻辑
            ranking = sorted(nums, reverse=True)
            result_text = "--- 🏆 成绩排名榜 ---\n\n"
            rank = 1
            prev_score = None

            for i in range(len(ranking)):
                current_score = ranking[i]
                if current_score != prev_score:
                    rank = i + 1
                    prev_score = current_score
                result_text += f"第 {rank} 名：{current_score}\n"

            # 在网页上显示结果
            st.success("数据全部合格，排名如下：")
            st.text(result_text)










