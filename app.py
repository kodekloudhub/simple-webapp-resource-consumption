from flask import Flask, jsonify, request, abort, make_response
from flask import render_template
import os
from multiprocessing import Pool
from multiprocessing import cpu_count
from psutil import virtual_memory
from kubernetes import client, config

config.load_incluster_config()
v1_core = client.CoreV1Api()

TEMPLATES_FOLDER = 'templates'
STATICS_FOLDER = 'static'
app = Flask(__name__, static_url_path='', static_folder=STATICS_FOLDER, template_folder=TEMPLATES_FOLDER)

BACKGROUND_IMAGE = "under_water.png"
CSS_FILE =  "blue"

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


@app.route("/load_cpu")
def generate_cpu_load():
    os.system("python cpu_task.py &")


@app.route("/load_memory")
def generate_memory_load():
    os.system("python mem_task.py &")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    # os.system("python cpu_task.py &")

    # os.spawnl(os.P_DETACH, 'python', 'cpu_task.py')
    # processes = cpu_count()
    # mem = virtual_memory()
    # print("Memory=" + str(mem.total/1024/1024/1024))  # total physical memory available
    # print('utilizing %d cores\n' % processes)
    #generate_load()
