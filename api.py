
from flask import Flask, jsonify, request
from flask_cors import CORS
from machine_learning import machine_learning_script
import json

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])

def api_function():
    data = json.loads(request.data)

    title = data['title']
    description = data['description']
    duration = data['duration']
    month = data['month']
    weekday = data['weekday']
    hour = data['hour']
    totalChannelViews = data['totalChannelViews']
    subscriberCount = data['subscriberCount']
    videoCount = data['videoCount']

    predictedLikes, predictedComments, predictedViews, probability = machine_learning_script(title, description, duration, month, weekday, hour, totalChannelViews, subscriberCount, videoCount)

    return jsonify({
        'predictedLikes': predictedLikes,
        'predictedComments': predictedComments,
        'predictedViews': predictedViews,
        'probability': probability
    })
    