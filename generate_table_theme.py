from pathlib import Path
from generate_table_musegan import write_audio_cell

dct = {"1hour30min": "214 epochs (1h 30m)",
       "1hour": "514 epochs (1h)",
       "25min": "214 epochs (25m)",
       "15000": "15000 epochs (29h)",
       "2days": "20290 epochs (48h)"}
order = ["25min", "1hour", "1hour30min", "15000", "2days"]
r = [0, 1, 2, 3, 4]
if __name__ == '__main__':
    directory = Path("theme_transformer")
    for file in directory.rglob("*.wav"):
        melody = str(file.parent).split("/")[-1]
        model_type = str(file.name).split("_")[1]
        r[order.index(model_type)] = (model_type, file)

    with open("result.md", "w") as f:
        f.write("<table>\n")
        f.write("<tr><td>Model type</td><td>874 melody</td></tr>")
        for model_type, file in r:
            f.write("<tr>\n")
            f.write(f"<td>{dct[model_type]}</td>")
            f.write(f"""    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="{file}" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>\n""")
            f.write("</tr>\n")
        f.write("</table>\n")



