import os
import json
from flask import render_template, request

class ShowSurveysPageController:
    def index(self, app):
        manifest_path = os.path.join(app.static_folder, 'react', '.vite', 'manifest.json')
        with open(manifest_path) as f:
            manifest = json.load(f)
        js_file = manifest['index.html']['file']

        # Find the latest CSS file in the static/react/assets directory
        assets_dir = os.path.join(app.static_folder, 'react', 'assets')
        css_file = None
        if os.path.isdir(assets_dir):
            all_files = os.listdir(assets_dir)
            css_files = [f for f in all_files if f.startswith('index-') and f.endswith('.css')]
            if css_files:
                css_file = sorted(css_files)[-1]  # Use the latest by name

        # Get patient_id from querystring, default to False if not provided
        patient_id = request.args.get('patient_id', False)
        return render_template(
            'index.html',
            react_name=patient_id,
            react_js_file=js_file,
            react_css_file=css_file
        )
