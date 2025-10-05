from musicwait import Music, MusicWait

from tqdm import tqdm
import time

with MusicWait(music=Music.OH_SUSANNA+Music.CAMPTOWN_RACES, lyrics=False):
    for _ in tqdm(range(200)):
        time.sleep(0.3)

print("Done!")
