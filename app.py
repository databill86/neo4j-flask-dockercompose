import db

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        query = request.args.get('query')
        params = request.args.to_dict()
        params.pop('query', None)

        results = db.run(query, params)

        l = []
        for result in results:
            d = {}
            for key, value in result.items():
                d[key] = decode(value)
            l.append(d)


        return jsonify(l)

    except Exception as e:
        abort(400, str(e))

def decode(value):
    if isinstance(value, list):
        return [decode(v) for v in value]
    elif isinstance(value, dict):
        return {k : decode(v) for k, v in value.items()}
    elif isinstance(value, str):
        return value
    elif isinstance(value, (str, bool, int, float)):
        return value
    else:
        return str(value)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
