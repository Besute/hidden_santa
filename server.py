from flask import Flask, request, jsonify, send_from_directory
from waitress import serve
from for_logger import *
import sys
import subprocess

PIPE = subprocess.PIPE


def workWithCommand(lst: list):
    process = subprocess.Popen(lst, stdout=PIPE, stderr=PIPE)
    stdoutput, stderroutput = process.communicate()
    if len(stderroutput) > 0:
        print("Error:\n{} - {}".format(lst, str(stderroutput)[2:-3]))
    return stdoutput, stderroutput


app = Flask(__name__)


@app.route("/get")
def get_stat():
    args = request.args
    one = args.get('one')
    two = args.get('two')
    three = args.get('three')
    four = args.get('four')
    Log.get().info(f"Huray {one} {two} {three} {four}")

    if four is not None and three is not None and two is not None and one is not None:
        out, err = workWithCommand(["python3", "main.py", one, two, three, four])
    elif three is not None and two is not None and one is not None:
        out, err = workWithCommand(["python3", "main.py", one, two, three])
    elif two is not None and one is not None:
        out, err = workWithCommand(["python3", "main.py", one, two])
    elif one is not None:
        out, err = workWithCommand(["python3", "main.py", one])

    Log.get().info(f"result main.py {out} {err}")
    return jsonify(f"{one} {two} {three} {four}")


if __name__ == '__main__':
    Log.get().info("Server has been started")
    serve(app, host="0.0.0.0", port=5678)
