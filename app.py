from flask import Flask, jsonify

from Services import number_service
from config import PORT_NUMBER

app = Flask(__name__)


@app.route('/total')
def get_total():
    lst = number_service.get_list()
    result = {'total': sum(lst)}
    return jsonify(result)


if __name__ == '__main__':
    app.config.from_object('config')
    app.run(port=PORT_NUMBER)
