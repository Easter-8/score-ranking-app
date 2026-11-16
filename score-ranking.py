import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="成绩排名查询系统")
st.title("🏆 成绩排名查询系统")

raw_text = st.text_input("请输入查询数据（用空格隔开）：", "")

if st.button("✅ 校验并生成排名"):
    if not raw_text.strip():
        st.warning("输入不能为空，请重新输入！")
    else:
        user_input = raw_text.split()
        nums = []
        errors = []

        for n in user_input:
            try:
                num = float(n)
                if num >= 0:
                    nums.append(num)
                else:
                    errors.append(f"'{num}' 是负数")
            except ValueError:
                errors.append(f"'{n}' 不是纯数字")

        if errors:
            error_str = "，".join(errors)
            st.error(f"❌ 输入有误：{error_str}。请重新输入！")
        elif not nums:
            st.warning("没有有效的正数可以排名！")
        else:
            ranking = sorted(nums, reverse=True)
            result_text = "--- 🏆 成绩排名榜 ---\n\n"
            rank = 1
            prev_score = None
            rows = []

            for i in range(len(ranking)):
                current_score = ranking[i]
                if current_score != prev_score:
                    rank = i + 1
                    prev_score = current_score
                result_text += f"第 {rank} 名：{current_score}\n"
                rows.append({"排名": rank, "分数": current_score})

            st.success("数据全部合格，排名如下：")
            st.text(result_text)

            # 自动把排名结果转成 Excel（放在内存里，不自动下载）
            df = pd.DataFrame(rows)
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="成绩排名")
            excel_data = buffer.getvalue()

            # 显示下载按钮：用户可以选择点（下载）或不点（不下载）
            st.info("排名结果已转为 Excel，您可以选择是否下载：")
            st.download_button(
                label="⬇️ 下载 Excel 文件",
                data=excel_data,
                file_name="成绩排名.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
