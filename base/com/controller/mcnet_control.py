from flask import render_template,request,jsonify,Response
from base import app
from base.com.controller.mcnet_analysis import start_analysis,get_particle_interaction
import time
import json
import os
@app.route('/uploadlhe', methods=['POST'])
def uploadlhe():
    file = request.files['file']
    all_events = start_analysis(file)
    # time.sleep(2)
    with open(os.getcwd()+'/base/static/data.json', "w", encoding="utf-8") as json_file:
        json.dump(all_events, json_file, indent=4)
    return render_template('mcnet.html',result_img='../../static/top_quarks.png',all_events = all_events)

@app.route('/particle', methods=['GET'])
def particle():
    get_particle_interaction()
    return render_template('event_graph.html')

@app.route('/jsonview', methods=['GET'])
def jsonview():
    return render_template('json_view.html')

@app.route('/event', methods=['POST'])
def event():
    file = request.files['file']
    data = json.load(file)
    formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
    return Response(formatted_json, mimetype="text/plain")
