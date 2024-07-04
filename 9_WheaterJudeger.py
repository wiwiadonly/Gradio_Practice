import gradio as gr

def wheater(unit, degree):
    image = [
        ["https://img.freepik.com/premium-vector/handsome-young-man-suffering-from-heat-wave-stoke-very-hot-weather-temperature_535862-729.jpg"],
        ["https://cdn.sanity.io/images/eztzxh9q/production/632e71aa265e618689b4fd3bebd1af3d03aa03aa-2120x1414.jpg?w=3840&q=75&fit=clip&auto=format"]
    ]
    if unit == '華氏':
        degree = (degree - 32) * 5 / 9 

    if degree >= 30:
        return f'現在 {degree:.2f} 度', image[0][0]
    else:
        return f'現在 {degree:.2f} 度', image[1][0]

iface = gr.Interface(
    fn=wheater,
    inputs=[gr.Radio(label='計算單位', choices=["攝氏", "華氏"]),
            gr.Slider(label='溫度', minimum=-100, maximum=100, value=0)],
    outputs=[gr.Textbox(label='計算結果'), gr.Image(label='天氣情況')],
    title="溫度換算",
    live=True
)

if __name__ == "__main__":
    iface.queue()
    iface.launch()