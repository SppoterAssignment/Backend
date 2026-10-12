# Vercel function for /api/plan
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _wsgi import app  # noqa: E402,F401
