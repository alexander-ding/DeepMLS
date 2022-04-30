from pathlib import Path
import os

DATA_DIR = Path('/mnt/hdd1/chairs')
for i in range(25, 101, 25):
    d = DATA_DIR / 'comfort' / str(i)
    for p in d.glob('*.obj'):

        if p.name[0] == '.':
            os.remove(p)
        name = p.stem.split('_')[0]
        os.rename(p, d / f'{name}.obj')
