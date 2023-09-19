import uvicorn


def __test__ ():
    uvicorn.run("prompt:app", host="127.0.0.1", port=5000, reload=True, log_level="debug")

def __main__ ():
    uvicorn.run("prompt:app", host="127.0.0.1", port=5000, reload=True, log_level="debug")