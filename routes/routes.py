import os

import colorgram

from flask import Blueprint, request, render_template, send_file
from PIL import Image


def make_palette(input_name, output_name):
    dish = Image.open(input_name).resize((897, 567))

    img = Image.new('RGB', (960, 791), '#FFFFFF')

    colors = colorgram.extract(input_name, 10)
    colors.sort(key=lambda c: c.rgb.r)

    img.paste(dish, (34, 34))

    for i in range(10):
        img.paste(colors[i].rgb, (34 + (i * 93), 610, 94 + (i * 93), 751))

    img.save(output_name)


def create_routes(input_name, output_name):
    bp = Blueprint('api_routes', __name__)

    @bp.route('/healthcheck', methods=['GET'])
    def healthcheck():
        return 'Alive', 200

    @bp.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @bp.route('/submit', methods=['POST'])
    def submit():
        if 'file' in request.files:
            os.remove(output_name)

            img = request.files['file']
            img.save(input_name)

            make_palette(input_name, output_name)
            os.remove(input_name)

            return send_file(os.path.abspath('routes/results/result.png'))

        return '', 400

    return bp
