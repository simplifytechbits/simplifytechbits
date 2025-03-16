from flask import Blueprint, render_template
import json
import os

main_bp = Blueprint("main", __name__)

def load_index():
    index_path = os.path.join("notes", "index.json")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

@main_bp.route("/")
def index():
    categories = load_index()
    return render_template("index.html", categories=categories)
