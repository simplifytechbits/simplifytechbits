from flask import Blueprint, render_template, abort
import os
import json
import markdown

notes_bp = Blueprint("notes", __name__)

# 读取 index.json
def load_index():
    index_path = os.path.join("notes", "index.json")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

@notes_bp.route("/notes/<category>")
def category_page(category):
    """显示某个技术类别下的所有笔记"""
    index = load_index()
    
    if category not in index:
        return f"分类 '{category}' 不存在", 404

    return render_template("category.html", category=category, notes=index[category])

@notes_bp.route("/notes/<category>/<note_id>")
def view_note(category, note_id):
    """渲染 Markdown 笔记"""
    index = load_index()

    if category not in index:
        return f"分类 '{category}' 不存在", 404
    
    # 查找对应的文件名
    note = next((n for n in index[category] if n["id"] == note_id), None)
    if not note:
        return f"笔记 '{note_id}' 不存在", 404

    note_path = os.path.join("notes", category, note["file"])
    
    if not os.path.exists(note_path):
        return f"笔记 '{note['title']}' 文件不存在", 404

    # 读取 Markdown 并转换为 HTML
    with open(note_path, "r", encoding="utf-8") as f:
        content = f.read()
        html_content = markdown.markdown(content)

    return render_template("note.html", category=category, note_title=note["title"], content=html_content)
