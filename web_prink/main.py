# coding: utf-8

# https://proglib.io/p/rukovodstvo-po-rabote-s-gradio-sozdanie-veb-interfeysa-dlya-modeley-mashinnogo-obucheniya-2023-03-06

import json
import os
import sys

base_dir = os.path.dirname(__file__)
sys.path.insert(0, base_dir)

from . import __version__

import gradio as gr


def print_pdf(input_file):
    print(input_file.name)
    res = "Wait until printing will be finished."
    return res


def scan_file(pass_text):
    print(pass_text)
    file = "testfile.mp4"
    return file


def main():
    with gr.Blocks() as demo:

        with gr.Tab("Print"):
            input1 = gr.File(label="Choose pdf")
            output1 = gr.Textbox(label="Output")
            submit1 = gr.Button("Print pdf")
            submit1.click(print_pdf, inputs=input1, outputs=output1)

        with gr.Tab("Scan"):
            input2 = gr.Radio(["tiff", "png", "pdf"], label="Output format")
            output2 = gr.File(label="Download scanned file. ")
            submit2 = gr.Button("Scan")
            submit2.click(scan_file, inputs=input2, outputs=output2)

    demo.launch()

