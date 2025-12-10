import json
import subprocess
from pathlib import Path
from string import Template
import os


def compile_tex(tex_path: Path):
    """Volitelně: přeloží .tex na .pdf pomocí pdflatex."""
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", tex_path.name],
        cwd=tex_path.parent,
        check=True,
    )

    # remove aux/log files
    for ext in [".aux", ".log", ".out", ".toc", ".synctex.gz"]:
        f = tex_path.with_suffix(ext)
        if f.exists():
            f.unlink()


if __name__ == '__main__':
    OUTPUT_DIR = Path('out_tests')

    f = open("variants.json")
    variants = json.loads(f.read())
    f.close()

    template_str = Path("template_zadani.tex").read_text(encoding="utf-8")
    tmpl = Template(template_str)

    for idx, variant in enumerate(variants):
        tex_filled = tmpl.substitute(
            FIGURE_FILE=variant["figure_file"],
            TASK_SHORT=variant["task_type"],
            INDEX1=variant["parameter_index1"],
            INDEX2=variant["parameter_index2"]
        )

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        tex_path = OUTPUT_DIR / f"test_{idx}.tex"
        tex_path.write_text(tex_filled, encoding="utf-8")

        compile_tex(tex_path)

