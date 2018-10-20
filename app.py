from flask import Flask, jsonify, request, abort, make_response
from flask import render_template
import os
from multiprocessing import Pool
from multiprocessing import cpu_count
from psutil import virtual_memory


TEMPLATES_FOLDER = 'templates'
STATICS_FOLDER = 'static'
app = Flask(__name__, static_url_path='', static_folder=STATICS_FOLDER, template_folder=TEMPLATES_FOLDER)

BACKGROUND_IMAGE = "under_water.png"
CSS_FILE =  "blue"

def f(x):
    while True:
        x*x

# @app.route("/")
# def main():
#     return render_template('hello.html')

@app.route('/')
def main():
    return render_template('index.html', theme=CSS_FILE, background_image='../images/'+BACKGROUND_IMAGE)

@app.route("/resource_count")
def resource_count():
    processes = cpu_count()
    mem = virtual_memory()
    print ("Memory=" + str(mem.total))  # total physical memory available
    result = {
        "cpu": processes,
        "memory": mem.total
    }
    return jsonify(result)


@app.route("/load")
def generate_load():
    processes = cpu_count()
    print('utilizing %d cores\n' % processes)
    pool = Pool(processes)
    pool.map(f, [0,1,2])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    # processes = cpu_count()
    # mem = virtual_memory()
    # print("Memory=" + str(mem.total/1024/1024/1024))  # total physical memory available
    # print('utilizing %d cores\n' % processes)
    #generate_load()
