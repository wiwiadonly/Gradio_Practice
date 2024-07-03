import gradio as gr

def change(user_name, height, isM, weight):
    if isM:
        bmi = weight / ((height)**2)
    else:
        bmi = weight / ((height / 100)**2)

    if bmi < 18.5:
        msg = "體重過輕"
    elif bmi < 25:
        msg = "體重正常"
    elif bmi < 30:
        msg = "體重過重"
    else:
        msg = "肥胖"

    return f"你的名字是 {user_name}", bmi, msg

iface = gr.Interface(
    fn=change,
    inputs=[
        gr.Textbox(label="輸入姓名"),
        gr.Number(label="你的身高（cm 或 m）"),
        gr.Checkbox(label="身高是否為公尺"),
        gr.Number(label="你的體重（kg）")
    ],
    outputs=[
        gr.Textbox(label="你的名字"),
        gr.Number(label="你的 BMI"),
        gr.Textbox(label="BMI 評價")
    ],
    title="BMI 計算器",
    description="輸入身高體重計算 BMI",
    article="BMI 是世界衛生組織作為衡量肥胖標準的依據。",
    allow_flagging="never",
    examples=[
        ["Alice", 1.58, True, 45],
        ["Bob", 158, False, 70]
    ],
    live=True
)

iface.queue()
iface.launch()