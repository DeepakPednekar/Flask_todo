from flaskr.extension import sendResponse

def root():
    ## in this view return all the todo items
    return sendResponse(msg="its root", status=1)

def test():
    return sendResponse(status=1)
