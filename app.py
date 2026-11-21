from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return {"mensaje": "API REST funcionando"}, 200

if __name__ == "__main__":
    app.run(debug=True)