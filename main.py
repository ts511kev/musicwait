from musicwait import Music, MusicWait

from tqdm import tqdm
import time

with MusicWait(music=Music.THE_ENTERTAINER, bpm=10, lyrics=False):
    for _ in tqdm(range(200)):
        time.sleep(1)

print("Done!")
