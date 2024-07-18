"""Main file"""

from api import app, api
from app.routers.routers import ns

api.add_namespace(ns)

if __name__ == '__main__':
    app.run()
