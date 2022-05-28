from pathlib import Path

from more_itertools import chunked

materials = Path("materials")

s = list()
for i in materials.rglob("*.wav"):
    model_type = str(i.parent).split("/")[-1]
    audio_path = str(i.parent) + '/' + str(i.name)
    s.append((model_type, audio_path))

result = sorted(s, key=lambda x: int(x[0][:-1])**3 * int(x[1].split('/')[-1].replace('.wav', '')))

with open("result.md", 'w') as f:
    f.write("<table>\n")
    f.write("<tr><td>Num epochs</td><td>1</td><td>2</td><td>3</td></tr>")
    for i in chunked(result, 3):
        f.write(f"""<tr>
    <td>{i[0][0]}</td>\n""")

        for k in i:
            f.write(f"""    <td>
        <audio controls="controls">
          <source type="audio/mp3" src="{i[1]}" />
          <p>Your browser does not support the audio element.</p>
        </audio>
    </td>\n""")
        f.write("</tr>\n")
    f.write("</table>")
