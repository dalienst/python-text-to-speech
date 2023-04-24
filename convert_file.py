import google.cloud.texttospeech as tts


def text_to_wav(voice_name: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_file = open(input("File: "), "r")
    text = text_file.read()
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = f"{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')


text_to_wav("en-AU-Neural2-A")

# def read_text_file():
#     text_file = open(input("File: "), "r")
#     text = text_file.read()
#     print(text)

# read_text_file()
