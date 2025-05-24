import whisper

class WhisperTranscriber:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path):
        return self.model.transcribe(audio_path)["text"]