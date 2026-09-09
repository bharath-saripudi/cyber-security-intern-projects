# Encryption/Decryption Tool

A Flask-based web application demonstrating symmetric (AES) and asymmetric (RSA) encryption algorithms.

## Features

- **AES Encryption/Decryption**: Symmetric encryption using AES-256 in CBC mode with PBKDF2 key derivation
- **RSA Encryption/Decryption**: Asymmetric encryption using RSA-OAEP with 2048-bit keys
- **Performance Comparison**: Benchmark tool to compare AES vs RSA encryption speeds
- **Web Interface**: Simple Flask-based UI for testing encryption/decryption

## How It Works

### AES Implementation
- Uses PBKDF2 to derive a 32-bit key from a password and random salt
- AES-256 in CBC mode with random IV for each encryption
- Salt + IV + ciphertext are base64-encoded for storage/transmission

### RSA Implementation
- Generates a 2048-bit RSA key pair at startup
- Uses PKCS#1 OAEP padding for secure encryption
- Note: RSA is limited to encrypting small amounts of data (~190 bytes with 2048-bit key)

## Requirements

```
Flask==2.3.2
pycryptodome==3.18.0
```

Install with:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python main.py
```

2. Open your browser to `http://127.0.0.1:5001`

3. Use the web interface to:
   - Encrypt text with AES or RSA
   - Decrypt previously encrypted text
   - Compare encryption performance between AES and RSA

## Security Notes

- This is a demonstration tool for educational purposes
- In production applications, consider:
  - Using established libraries like cryptography.io
  - Proper key management systems
  - Authenticated encryption modes (GCM) instead of CBC
  - Secure random number generation for keys/nonces
  - Protection against side-channel attacks

## Files

- `main.py`: Flask application with encryption/decryption endpoints
- `templates/index.html`: Web interface
- `requirements.txt`: Python dependencies

## Educational Purpose

This tool helps understand:
- Differences between symmetric and asymmetric encryption
- Key derivation functions (PBKDF2)
- Block cipher modes (CBC)
- RSA padding schemes (OAEP)
- Performance trade-offs between encryption algorithms