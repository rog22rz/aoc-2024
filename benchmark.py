import importlib.util
import os
import time
from contextlib import redirect_stdout

import click
from pathlib import Path

@click.command()
@click.argument("input_file")
def cli(input_file):
    rootdir = Path(os.getcwd())
    files = sorted([f for f in rootdir.glob("day*/aoc*_p*.py") if f.is_file()])

    for file in files:
        spec = importlib.util.spec_from_file_location("script", file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        with open(os.devnull, "w") as fnull:
            with redirect_stdout(fnull):
                total_time = 0
                iterations = 500
                for i in range(iterations):
                    start_time = time.perf_counter()
                    module.processFile(os.path.join(os.path.dirname(file), input_file))
                    end_time = time.perf_counter()
                    total_time += end_time - start_time

        click.echo(f"[{os.path.basename(file)}] Average execution over {iterations} iterations is {round(total_time / iterations, 5)}")


if __name__ == "__main__":
    cli()
