import random

import gradio as gr


def picture():
    images = [
        (random.choice(
            [
                "https://www.demonslayer.com.tw/wp-content/uploads/2020/12/Agatsuma-Zenitsu-6.jpg",
                "https://scontent.ftpe14-1.fna.fbcdn.net/v/t39.30808-6/302443284_468316988639951_4043971039249421128_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=HBeYutBBy9IQ7kNvgHFdqin&_nc_ht=scontent.ftpe14-1.fna&oh=00_AYBZumBGO6DLeMUyByMviUdr6ZBC8EhKSF2E1mGliJb9hg&oe=668C2714",
                "https://www.niusnews.com/upload/imgs/default/202306_Noah/0607/1/02.jpg",
                "https://www.niusnews.com/upload/imgs/default/202306_Noah/0607/1/03.jpg",
                "https://www.niusnews.com/upload/imgs/default/202306_Noah/0607/1/cMPHVUT.jpeg",
            ]
        ), f"label {i}")
        for i in range(3)
    ]
    return images


with gr.Blocks() as iblock:
    gallery = gr.Gallery(
        label="Generated images", show_label=False, elem_id="gallery"
    , columns=[3], rows=[1], object_fit="contain", height="auto")
    btn = gr.Button("Generate images", scale=0)

    btn.click(picture, None, gallery)

if __name__ == "__main__":
    iblock.launch()