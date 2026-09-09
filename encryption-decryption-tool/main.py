from flask import Flask, render_template, request, jsonify
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
import base64, os, time

app = Flask(__name__)

# --- AES helpers ---
def aes_encrypt(plaintext, password):
    salt = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(salt + cipher.iv + ct).decode()

def aes_decrypt(token, password):
    raw = base64.b64decode(token)
    salt, iv, ct = raw[:16], raw[16:32], raw[32:]
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

# --- RSA helpers (demo keypair generated once at startup) ---
rsa_key = RSA.generate(2048)
rsa_public = rsa_key.publickey()

def rsa_encrypt(plaintext):
    cipher = PKCS1_OAEP.new(rsa_public)
    return base64.b64encode(cipher.encrypt(plaintext.encode())).decode()

def rsa_decrypt(token):
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(base64.b64decode(token)).decode()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    text = data.get("text", "")
    password = data.get("password", "")
    algo = data.get("algo", "aes")
    try:
        if algo == "aes":
            result = aes_encrypt(text, password)
        else:
            result = rsa_encrypt(text)  # RSA only fits short text (~190 bytes)
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()
    token = data.get("text", "")
    password = data.get("password", "")
    algo = data.get("algo", "aes")
    try:
        if algo == "aes":
            result = aes_decrypt(token, password)
        else:
            result = rsa_decrypt(token)
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error="Decryption failed - check key/ciphertext"), 400

@app.route("/compare", methods=["POST"])
def compare():
    data = request.get_json()
    text = data.get("text", "test message for benchmarking")
    password = "benchmark-password"

    start = time.perf_counter()
    aes_encrypt(text, password)
    aes_time = (time.perf_counter() - start) * 1000

    start = time.perf_counter()
    try:
        rsa_encrypt(text[:100])  # RSA size-limited
        rsa_time = (time.perf_counter() - start) * 1000
    except Exception:
        rsa_time = None

    return jsonify(aes_ms=round(aes_time, 3), rsa_ms=round(rsa_time, 3) if rsa_time else "text too long")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)