import gradio as gr

def hello(user_name):
    return user_name+"你好"

iface = gr.Interface(
    fn=hello,
    inputs='text',
    outputs='text'
)

iface.queue()
iface.launch(share=True)