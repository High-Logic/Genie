import genie_tts as genie
import time

# 首次运行时会自动从网络下载所需文件
genie.load_predefined_character('misono_mika')

genie.tts(
    character_name='misono_mika',
    text='どうしようかな……やっぱりやりたいかも……！',
    play=True,  # 直接播放生成的音频
)

time.sleep(10)  # 由于音频播放是异步的，这里添加一个延时以确保音频能够完整播放完毕。