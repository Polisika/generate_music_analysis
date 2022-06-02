from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    directory = Path("musetransformer")
    result = list(filter(lambda x: "25min" in str(x), sorted([i for i in directory.glob("*.wav")],
                                                             key=lambda x:
                                                             int(str(x).split("_")[3][:-1]) ** 2 *
                                                             int(str(x).split("_")[4] *
                                                                 int(str(x).split("_")[1].replace("min", "").replace(
                                                                     "hour", "."))))))
    with open("result.md", "w") as f:
        f.write("<table>\n<tr><th>Model</th><th>1</th><th>2</th><th>3</th></tr>\n")
        for i in result:
            x = str(i)
            vector = x.split("_")[4]
            muse_model = x.split("_")[3]
            if vector == "1":
                f.write("<tr>\n")
                f.write(f"<td>{muse_model}</td>\n")
            audio = f"""        <audio controls="controls">
              <source type="audio/mp3" src="{x}" />
              <p>Your browser does not support the audio element.</p>
            </audio>"""
            f.write(f"<td>{audio}</td>")
            if vector == "3":
                f.write("</tr>\n")
        f.write("</table>\n")

