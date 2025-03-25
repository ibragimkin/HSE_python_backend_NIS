from flask import Flask, jsonify, request
from dotenv import dotenv_values
from controllers import operation

app = Flask(__name__)

def get_port() -> int:
    """
    Функция получает порт из файла конфигурации .env.
    Если параметр PORT найден, возвращается его значение (приведённое к int),
    иначе возвращается порт по умолчанию 5000.
    """
    config = dotenv_values(".env")
    if "PORT" in config:
        try:
            return int(config["PORT"])
        except ValueError:
            pass
    return 5000

@app.route("/")
def server_info():
    return "My server"

@app.route("/author")
def author():
    author_info = {
        "name": "Stas",
        "course": 3,
        "age": 21,
    }
    return jsonify(author_info)

@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})

if __name__ == "__main__":
    app.run(debug=True, port=get_port())
