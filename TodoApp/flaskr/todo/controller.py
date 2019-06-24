from flaskr.extension import sendResponse
from .models import *

def root():
    data = TodoItem.query.all()
    data = [each.get_json() for each in data] if data else []
    return sendResponse(data=data, status=1)

