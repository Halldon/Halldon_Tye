
from flask_cors import cross_origin
from flask import Flask, request, Response, jsonify
from http import HTTPStatus
import json
import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
sys.path.append(API_PATH)

from api.ui_config import UIConfig
from api.gpt import set_openai_key, Example
from api.model_lookup import modelLookup, models


CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"

def server():
    """Creates Flask app to serve the React app."""
    app = Flask(__name__)

    app.config.from_envvar(CONFIG_VAR)
    set_openai_key(app.config[KEY_NAME])

    @app.route('/models', methods=["GET"])
    @cross_origin()
    def get_models():
        modelList = list(map(lambda m: m.id, models))
        return jsonify(modelList)

    @app.route("/models/<string:model_id>/params", methods=["GET"])
    @cross_origin()
    def get_params(model_id):
        model = modelLookup[model_id]
        response = model.config.json()
        return response

    def error(err_msg, status_code):
        return Response(json.dumps({"error": err_msg}), status=status_code)

    def get_example(model, example_id):
        """Gets a single example or all the examples."""
        gpt = model.gpt
        # return all examples
        if not example_id:
            return json.dumps(gpt.get_all_examples())

        example = gpt.get_example(example_id)
        if not example:
            return error("id not found", HTTPStatus.NOT_FOUND)
        return json.dumps(example.as_dict())

    def post_example(model):
        """Adds an empty example."""
        gpt = model.gpt
        new_example = Example("", "")
        gpt.add_example(new_example)
        return json.dumps(gpt.get_all_examples())

    def put_example(args, model, example_id):
        """Modifies an existing example."""
        gpt = model.gpt
        if not example_id:
            return error("id required", HTTPStatus.BAD_REQUEST)

        example = gpt.get_example(example_id)
        if not example:
            return error("id not found", HTTPStatus.NOT_FOUND)

        if "input" in args:
            example.input = args["input"]
        if "output" in args:
            example.output = args["output"]

        # update the example
        gpt.add_example(example)
        return json.dumps(example.as_dict())

    def delete_example(model, example_id):
        """Deletes an example."""
        gpt = model.gpt
        if not example_id:
            return error("id required", HTTPStatus.BAD_REQUEST)

        gpt.delete_example(example_id)
        return json.dumps(gpt.get_all_examples())

    @app.route(
        "/models/<string:model_id>/examples",
        methods=["GET", "POST"],
        defaults={"example_id": ""},
    )
    @app.route(
        "/models/<string:model_id>/examples/<example_id>",
        methods=["GET", "PUT", "DELETE"],
    )
    @cross_origin()
    def examples(model_id, example_id):
        model = modelLookup[model_id]
        method = request.method
        args = request.json
        if method == "GET":
            return get_example(model, example_id)
        if method == "POST":
            return post_example(model)
        if method == "PUT":
            return put_example(args, model, example_id)
        if method == "DELETE":
            return delete_example(model, example_id)
        return error("Not implemented", HTTPStatus.NOT_IMPLEMENTED)

    @app.route("/models/<string:model_id>/translate", methods=["GET", "POST"])
    @cross_origin()
    def translate(model_id):
        # pylint: disable=unused-variable
        model = modelLookup[model_id]
        gpt = model.gpt
        prompt = request.json["prompt"]
        response = gpt.submit_request(prompt)
        offset = 0
        if not gpt.append_output_prefix_to_query:
            offset = len(gpt.output_prefix)
        return {'text': response['choices'][0]['text'][offset:]}

    app.run()

server()