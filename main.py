from musicwait import Music, MusicWait

from tqdm import tqdm
import time


with MusicWait(
    music= Music.OH_SUSANNA,
    speed=1.2,
    lyrics=False,
):
    for _ in tqdm(range(200)):
        time.sleep(1)

print("Done!")
