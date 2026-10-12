"""
Shared WSGI app for the Vercel functions in this folder.

Vercel maps files to URLs (api/plan.py serves /api/plan), so no rewrites are
needed and Django receives the real request path. Files starting with "_" are
not exposed as functions, which is why this helper lives here.
"""
import sys
from pathlib import Path

# Make the backend root importable (for `myproject` and `routeplanner`).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from myproject.wsgi import application  # noqa: E402

BUILD = 'file-routes-1'  # bump to confirm which version is deployed


def app(environ, start_response):
    def start_with_build_header(status, headers, exc_info=None):
        return start_response(status, [*headers, ('X-App-Build', BUILD)], exc_info)
    return application(environ, start_with_build_header)
