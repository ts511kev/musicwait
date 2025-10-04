from musicwait import Music, MusicWait

from tqdm import tqdm
import time

with MusicWait(music=Music.OH_SUSANNA, bpm=8, lyrics=True):
    for _ in range(100):
        time.sleep(0.3)

print("Done!")
