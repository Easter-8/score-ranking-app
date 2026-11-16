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

            # 数据准备完毕，开始展示
            st.success("数据全部合格！")
            
            # 创建两个标签页
            tab1, tab2 = st.tabs(["📝 文本排名", "📊 Excel 表格预览"])
            
            with tab1:
                # 原来纯文本展示
                st.text(result_text)
                
            with tab2:
                # 将数据转为 DataFrame 用于表格预览
                df = pd.DataFrame(rows)
                # 使用 st.dataframe 显示表格，外观类似 Excel
                st.dataframe(df, use_container_width=True, hide_index=True)
                
                # 尝试生成真正的 Excel 文件供下载
                try:
                    buffer = io.BytesIO()
                    # 这里需要 openpyxl 库
                    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                        df.to_excel(writer, index=False, sheet_name="成绩排名")
                    excel_data = buffer.getvalue()
                    
                    st.info("您可以在上方预览表格。如果需要保存到电脑，请点击下方按钮：")
                    st.download_button(
                        label="⬇️ 下载 Excel 文件",
                        data=excel_data,
                        file_name="成绩排名.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    )
                except ImportError:
                    st.error("⚠️ 缺少 openpyxl 库，暂时无法提供下载。请确保 requirements.txt 中包含 openpyxl 并重启应用。")
