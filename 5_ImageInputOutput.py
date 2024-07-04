import gradio as gr

def hello(image):
    return image

iface = gr.Interface(
    fn=hello,
    inputs=gr.Image(label="輸入圖片",sources=['upload','clipboard']),
    outputs=gr.Image(label="輸出圖片"),
    title="圖片輸入輸出"
)

if __name__ == "__main__":
    iface.queue()
    iface.launch()