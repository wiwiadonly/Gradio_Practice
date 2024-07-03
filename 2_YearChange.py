import gradio as gr

def change(user_name, year, isAD):
    year = int(year)
    if isAD==False:
        year += 1911
    return f"你的名字是 {user_name}，你的生日為: {year} 年"

iface = gr.Interface(
    fn=change,
    inputs=['text', 'text', 'checkbox'],
    outputs='text'
)

iface.queue()
iface.launch()