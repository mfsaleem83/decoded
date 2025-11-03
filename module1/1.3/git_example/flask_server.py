from flask import Flask, request, jsonify

app = Flask(__name__)

# POST /echo endpoint
# TODO: Insert the appropriate HTTP method e.g. "GET", "POST"


@app.route("/echo", methods=["POST"])
def echo():
    # TODO: Get JSON data from the request
    data = request.get_json()

    # TODO: Print the received data for debugging
    # (This helps us confirm what's arriving in the API)
    print(data)
    ...

    # Validate that JSON exists and contains a "message" key
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message'"}), 400

    # Return the same data back
    return jsonify(data)

# Add a simple /status endpoint


@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "ok"}), 200


@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get('name', default="Stranger")
    print(name)
    if name is None:
        return jsonify({"status": "Hello Stranger"}), 400
    return jsonify({"status": f"Hello {name}"}), 200

# STRETCH TODO: Add a GET /greet?name=YourName route
# It should return: {"message": "Hello, YourName!"}
# If no name is provided, return: {"message": "Hello, stranger!"}

# Run the app


@app.route('/')
def home():
    return jsonify(message="Hello from the Flask app!")


if __name__ == '__main__':
    # ---- DECODED URL GENERATOR ----
    import socket
    print("https://lab{0}{1}.labs.decoded.com:8100".format(
        *socket.gethostbyname(socket.gethostname()).split('.')[2:]
    ))
    # ---- /DECODED URL GENERATOR ----
    app.run(host="0.0.0.0", port=8100, debug=True)
