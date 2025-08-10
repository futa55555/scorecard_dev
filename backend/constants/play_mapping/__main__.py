# backend/constants/play_mapping/__main__.py

from . import play_mapping

print(f"Total plays: {len(play_mapping)}")
for k, v in list(play_mapping.items())[:5]:
    print(k, v)
