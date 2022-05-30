from pathlib import Path
from generate_table_musegan import write_audio_cell

dct = {"1hour30min": "214 epochs (1h 30m)",
       ""}
"""
    \item 214 эпохи (25 минут)
    \item 300 эпох (35 минут)
    \item 514 эпох (1 час)
    \item 771 эпоха (1 час 30 минут)
    \item 15000 эпох (29 часов)
    \item 20290 эпох (48 часов)
"""

if __name__ == '__main__':
    directory = Path("theme_transformer")
    with open("result.md", "w") as f:
        for file in directory.rglob("*.wav"):
            melody = str(file.parent).split("/")[-1]
            model_type = str(file.name).split("_")[1]



