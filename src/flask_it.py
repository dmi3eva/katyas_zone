import os
import sys
import argparse

from flask import Flask, jsonify, request

INPUT_PATH = "../data/input/counter.txt"
OUTPUT_PATH = "../data/output/history.txt"

VALUE = 42
NAME = "Izabella"
CONDA = True
# TOST = os.environ["POSE"]
# raffic = os.environ['me']
# print(raffic)

app = Flask(__name__)


@app.route("/")
def usual():
    return "<p>I just start it...</p>"


@app.route('/hello')
def hello():
    return 'Hello'


@app.route('/value')
def value():
    return str(VALUE) + " " + NAME + " " + str(CONDA)  # + " " + str(TOST)


# @app.route('/tost')
# def tost():
#     return str(TOST)


@app.route('/counter')
def fileit():
    print('hello')
    with open(INPUT_PATH, 'r', encoding='utf-8') as inp:
        file_content = inp.read()
        number = int(file_content)
    print(number)
    with open(INPUT_PATH, 'w', encoding='utf-8') as outp:
        outp.write(str(number + 1))
    with open(OUTPUT_PATH, 'a', encoding='utf-8') as outp:
        outp.write(str(number + 1) + "\n")
    return str(number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        type=str,
        default="ru",
        help="Name"
    )
    parser.add_argument(
        "--value",
        type=int,
        default=38,
        help="Value"
    )
    parser.add_argument(
        "--conda",
        type=bool,
        default=False,
        help="Condition"
    )
    args = parser.parse_args(sys.argv[1:])
    VALUE = args.value
    NAME = args.name
    CONDA = args.conda
    app.run(host='0.0.0.0', port=1235)