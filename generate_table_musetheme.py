from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    directory = Path("musetransformer")
    files = sorted([i for i in directory.rglob("*.wav")])
    for type_m in ["35min", "2days", "25min", "1hour30min", "1hour"]:
        result = list(filter(lambda x: type_m in str(x), files))
        with open(f"result_{type_m}.md", "w") as f:
            f.write("<table>\n<tr><th>Model</th><th>1</th><th>2</th><th>3</th></tr>\n")
            for i in result:
                x = str(i).split("/")[-1].replace("15000_epochs", "15000epochs")
                vector = x.split("_")[4]
                muse_model = x.split("_")[3]
                if vector == "1":
                    f.write("<tr>\n")
                    f.write(f"<td>{muse_model}</td>\n")
                audio = f"""        <audio controls="controls">
                  <source type="audio/mp3" src="{i}" />
                  <p>Your browser does not support the audio element.</p>
                </audio>"""
                f.write(f"<td>{audio}</td>")
                if vector == "3":
                    f.write("</tr>\n")
            f.write("</table>\n")
