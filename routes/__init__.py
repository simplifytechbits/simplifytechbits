"""
Initialize routes package.
"""
from .notes import notes_bp
from .main import main_bp

all_blueprints = [
    notes_bp,
    main_bp,
]