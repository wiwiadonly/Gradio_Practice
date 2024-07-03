import gradio as gr

def Bill(Buyer, Volume, Flavor, isMember):
    price = 0
    if isMember == "外系":
        price = 15 * Volume
    elif isMember == "本系成員":
        price = 12 * Volume
    else:
        price = 10 * Volume
        
    return Buyer, Flavor, price

iface = gr.Interface(
    fn=Bill,
    inputs=[
        gr.Textbox(label="輸入姓名", placeholder="趙祖威"),
        gr.Slider(label="購買份數", minimum=1, maximum=50, step=1, value=3),
        gr.CheckboxGroup(label="口味", choices=["草莓", "巧克力", "抹茶"], info="口味口挑但數量隨機"),
        gr.Radio(label="你的身分", choices=["外系", "本系成員", "本系會員"])
    ],
    outputs=[
        gr.Textbox(label="你的名字"),
        gr.Textbox(label="口味"),
        gr.Number(label="帳單金額")
    ],
    title="餅乾金額試算表",
    description="""⏰設攤時間：2023/05/31(三)-2023/06/02(五) 10:00～17:00\n
⏰領取時間：2023/06/08(三)10:00～17:00\n
🎪擺攤地點：六教一樓座椅區\n
💲外系每份15元 本系成員每份12元 本系會員每份10元""",
    article="活動主辦方保有變更活動之權利",
    allow_flagging="never",
    examples=[
        ["趙祖威", 15, ["巧克力"], "本系會員"],
    ],
    live=True
)

iface.queue()
iface.launch()