from pathlib import Path

d = Path()

with open("latex.tex", "w") as f:
    for file in d.glob("*.py"):

        if str(file.name) == "generate_latex.py":
            continue
        filename = str(file.name).replace("_", "\_")
        content = file.open("r").read()
        f.write(
            "Файл \\textbf{%s}\n\n\\begin{lstlisting}[language=Python]\n%s\n\\end{lstlisting}\n\n"
            % (filename, content)
        )
        print("\\testit{%s}\n" % file.name)
