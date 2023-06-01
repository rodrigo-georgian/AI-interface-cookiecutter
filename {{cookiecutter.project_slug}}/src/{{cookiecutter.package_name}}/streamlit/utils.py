import sys
from contextlib import contextmanager
from time import perf_counter

import streamlit.components.v1 as components
from ansi2html import Ansi2HTMLConverter


class TeeStream:
    def __init__(self, original_stream, additional_target):
        self.original_stream = original_stream
        self.additional_target = additional_target

    def write(self, text):
        self.original_stream.write(text)
        self.additional_target.write(text)

    def flush(self):
        self.original_stream.flush()
        self.additional_target.flush()


@contextmanager
def redirect_stdout_copy(new_target):
    tee_stream = TeeStream(sys.stdout, new_target)
    old_target, sys.stdout = sys.stdout, tee_stream  # replace sys.stdout
    try:
        yield tee_stream  # run some code with the replaced stdout
    finally:
        sys.stdout = old_target  # restore to the previous value


@contextmanager
def catchtime() -> float:
    start = perf_counter()
    yield lambda: perf_counter() - start


def render_stdout(std_out: str):
    ansi_converter = Ansi2HTMLConverter()
    html_output = ansi_converter.convert(std_out)
    components.html(html_output, height=600, scrolling=True)
