import os

# (Optional) We recommend manually specifying the Hubert path for Genie.
# You can download the model at https://huggingface.co/High-Logic/Genie
# Note: If this line is not set, Genie will automatically download the model from Huggingface.
os.environ['HUBERT_MODEL_PATH'] = r"<PATH_TO_HUBERT_ONNX_MODEL>"

# (Optional) We recommend manually specifying the dictionary path for pyopenjtalk.
# You can download the dictionary here: https://huggingface.co/High-Logic/Genie
# Note: If this line is not set, pyopenjtalk will automatically download the dictionary.
os.environ['OPEN_JTALK_DICT_DIR'] = r"<PATH_TO_OPEN_JTALK_DICT>"

# (Optional) You can set the number of cached character models and reference audios.
os.environ['Max_Cached_Character_Models'] = '3'
os.environ['Max_Cached_Reference_Audio'] = '10'

# Make sure to set environment variables before importing Genie.
import genie_tts as genie
import time

genie.load_character(
    character_name='<CHARACTER_NAME>',  # Replace with your character name
    onnx_model_dir=r"<PATH_TO_CHARACTER_ONNX_MODEL_DIR>",  # Replace with the folder containing the ONNX model
)

genie.set_reference_audio(
    character_name='<CHARACTER_NAME>',  # Use the same character name as above
    audio_path=r"<PATH_TO_REFERENCE_AUDIO>",  # Replace with path to your reference audio file
    audio_text="<REFERENCE_AUDIO_TEXT>",  # Replace with the text corresponding to the reference audio
)

genie.tts(
    character_name='<CHARACTER_NAME>',  # Use the same character name
    text="<TEXT_TO_SYNTHESIZE>",  # Replace with the text you want to synthesize
    play=True,  # Whether to play the audio immediately
    split_sentence=True,  # Whether to split sentences before TTS
    save_path="<OUTPUT_AUDIO_PATH>",  # Replace with path to save the audio file
)

time.sleep(10)  # Since play=True, wait for playback to finish
