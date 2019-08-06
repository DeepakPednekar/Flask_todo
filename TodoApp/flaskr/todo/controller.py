from flask_jwt import current_identity, jwt_required, request
from flaskr.extension import sendResponse, db
from .models import *

@jwt_required()
def root():
    user = current_identity
    if request.method.lower() =='get':
        data = Todo.query.filter_by(user_id=user.id).all()
        # print('query data | ', data)
        data = [each.get_json() for each in data] if data else []
        return sendResponse(data=data, status=1)

    elif request.method.lower() == 'post':
        data = request.get_json()
        if not data:
            return sendResponse(msg="No json found", status=0)

        data['user_id'] = user.id
        todoitem = Todo(**data)
        db.session.add(todoitem)
        db.session.commit()

        return sendResponse(status=1)


