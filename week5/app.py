from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hellohello():
    response = {
        "message": "Hello COMP216 W25 Class!",
        "status": "Success"
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5444) # standard port: 5000
