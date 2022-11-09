import warnings

from face_verify import face_analyze, find_face_in_base, get_similar_faces
import requests

warnings.filterwarnings("ignore")

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from flask import Flask, jsonify, request, make_response

import argparse
import uuid
import json
import time
from tqdm import tqdm
from deepface import DeepFace

app = Flask(__name__)

@app.route('/analyze')
def analyze():
    body = request.get_json()
    res = face_analyze(body['img1'])

    return jsonify(res)


@app.route('/find')
def find():
    body = request.get_json()
    res = find_face_in_base(body['img1'])

    return jsonify(res)


@app.route('/getsimilar')
def get_similar():
    body = request.get_json()
    res = get_similar_faces(body['img1'], body['img2'])

    return jsonify(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=5000,
        help='Port of serving api')
    args = parser.parse_args()
    app.run(host='127.0.0.1', port=args.port)
