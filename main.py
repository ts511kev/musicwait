from musicwait import Music, MusicWait

from tqdm import tqdm
import time

with MusicWait(music=Music.OH_SUSANNA, lyrics=False):
    for _ in tqdm(range(100)):
        time.sleep(0.3)

print("Done!")
