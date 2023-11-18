import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="amitryptyline", auth_level=func.AuthLevel.ANONYMOUS)
def amitryptyline(req: func.HttpRequest) -> func.HttpResponse:
    try:
        j = req.get_json()
        return func.HttpResponse(json.dumps(j), status_code=200, headers={"Content-Type": "application/json"})
    except ValueError:
        pass

@app.route(route="RockyFn", auth_level=func.AuthLevel.FUNCTION)
def RockyFn(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=202
        )