import wave
import io
from AppKit import NSSound


wave_output = io.BytesIO()
wave_shell = wave.open(wave_output, mode="wb")
file_path = 'SINE.WAV'
input_audio = wave.open(file_path)
input_audio_frames = input_audio.readframes(input_audio.getnframes())

wave_shell.setnchannels(input_audio.getnchannels())
wave_shell.setsampwidth(input_audio.getsampwidth())
wave_shell.setframerate(input_audio.getframerate())

seconds_multiplier = input_audio.getnchannels() * input_audio.getsampwidth() * input_audio.getframerate()

wave_shell.writeframes(input_audio_frames[second_multiplier:second_multiplier*5])

wave_shell.close()

wave_output.seek(0)
wave_data = wave_output.read()
audio_stream = NSSound.alloc()
audio_stream.initWithData_(wave_data)
audio_stream.play()
