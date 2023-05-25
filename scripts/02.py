import whisper
import time

print("Hello!")
perf = time.perf_counter()

print("working ...")
model = whisper.load_model("large-v2")
result = model.transcribe("download/audio.wav", word_timestamps=True)

print(result["text"])


meta_content = f"""
title ===========
{result["text"]}
"""
with open('download/result-1.txt', 'a') as f:
    f.write(meta_content)
print("done!")
