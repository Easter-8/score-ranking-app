import tkinter as tk
from  tkinter import messagebox


def process_data():
    raw_text = entry.get().strip()
    if not raw_text:
        messagebox.showinfo('提示','输入内容不能为空，请重新输入！')
        return






# while True:
    user_input = raw_text.split()
    # has_error = False
    nums = []
    errors = []
    # error_msg = ''
    for n in user_input:
        try:
            num = float(n)
            if num >= 0:
                nums.append(num)

            else:
                # has_error = True
                errors.append(f'({num})不为正数')
                # error_msg = f'输入的{num}不为正数'
                # print(f"恁输入的{num}不为正数，请重新输入：")
                break
        except ValueError:
            # has_error = True
            errors.append(f'({n})不为纯数字')
            # error_msg = f'输入的{n}不为纯数字'

            # print(f'恁输入的{n}不为纯数字，请重新输入：')
            # has_error = True
            # error_char = n
            # break

    if errors:
    # if has_error:
        error_str = ', '.join(errors)
        messagebox.showwarning('输入错误',f"❌ 恁输入的 {error_str} ，请重新输入：\n")
        # print(f"❌ 恁输入的 {error_str} ，请重新输入：\n")
        # print(f"❌ 您输入的 {error_msg}，请重新输入：\n")
        # continue
        return

    elif not nums:
        messagebox.showwarning("❌ 恁没有输入任何有效的正数，请重新输入！\n")
        # continue
        return

    result_text = ("\n✅ 输入全部合法，排名如下：")
    ranking = sorted(nums, reverse=True)
    result_text = "\n--- 🏆 成绩排名榜 ---\n\n"
    rank = 1
    prev_score = None

    for i in range(len(ranking)):
        current_score = ranking[i]
        if current_score != prev_score:
            rank = i + 1  # 并列排名逻辑
            prev_score = current_score
        # print(f'第 {rank} 名：{current_score}')
        result_text += f'第 {rank} 名：\t{current_score}\n'
    #
    # break
    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, result_text)
    result_box.tag_configure('center',justify='center')
    result_box.tag_add('center','1.0',tk.END)
    result_box.config(state="disabled")


    # else:
    #     ranking = sorted(nums,reverse=True)
    #     rank = 1
    #     pre_score = None
    #     for i in range(len(ranking)):
    #         current_score = ranking[i]
    #         if current_score != pre_score:
    #             rank = i+1
    #             pre_score = current_score
    #         print(f'第{rank}名，{current_score}')
    #     break


root = tk.Tk()
root.title('成绩排名查询系统')
root.geometry('450x550')
root.configure(padx=20,pady=20)

label_title = tk.Label(root,text='请输入数据（用空格隔开）：',font=('微软雅黑',12,'bold'))
label_title.pack(pady=(0,10))

entry = tk.Entry(root,font=('微软雅黑',12),width=35)
entry.pack(pady=5)

btn = tk.Button(root,text="✅ 校验并生成排名", font=("微软雅黑", 12, "bold"),
            bg="#4CAF50", fg="white", cursor="hand2", command=process_data)
btn.pack(pady=15)

# 5. 放餐桌（结果显示框）
result_box = tk.Text(root, font=("微软雅黑", 12), width=35, height=15, bg="#f9f9f9", state="disabled")
result_box.pack(pady=5)

# 6. 餐厅正式营业（让窗口一直开着，不闪退）
root.mainloop()









