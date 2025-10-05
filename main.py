from musicwait import Music, MusicWait

from tqdm import tqdm
import time

with MusicWait(music=Music.RING_RING_DE_BANJO, bpm=10, lyrics=False):
    for _ in tqdm(range(200)):
        time.sleep(0.3)

print("Done!")
