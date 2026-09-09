# Password Strength Analyzer

A Flask-based web application that evaluates password strength and provides feedback on how to improve weak passwords.

## Features

- **Password Strength Scoring**: Evaluates passwords based on length, character variety, and common patterns
- **Feedback System**: Provides specific suggestions for improving weak passwords
- **Crack Time Estimation**: Estimates how long it would take to brute-force the password
- **Common Password Detection**: Checks against a list of frequently used weak passwords
- **Secure Password Generation**: Generates cryptographically strong random passwords
- **Web Interface**: Simple Flask-based UI for testing passwords

## How It Works

### Evaluation Criteria
The checker evaluates passwords based on:
1. **Length**: Minimum 8 characters
2. **Character Variety**: 
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Digits (0-9)
   - Special characters (!@#$%^&*(),.?":{}|<>)
3. **Common Patterns**: Checks against a list of frequently used weak passwords
4. **Entropy Calculation**: Estimates crack time based on character set size and password length

### Scoring System
- Each criterion met adds 1 point to the score (max 4 points)
- Passwords matching common weak passwords automatically score 0
- Feedback is provided for each missing criterion

### Crack Time Estimation
Assumes an offline brute-force attack capability of 1 billion guesses per second:
- Calculates total possible combinations: charset^length
- Divides by guesses per second to get time in seconds
- Converts to appropriate units (seconds, minutes, hours, days, years)

## Requirements

```
Flask==2.3.2
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

2. Open your browser to `http://127.0.0.1:5000`

3. Use the web interface to:
   - Enter a password to see its strength score and feedback
   - Get an estimated crack time
   - Generate a secure random password

## API Endpoints

- `GET /` - Main page
- `POST /check_password` - Check password strength (JSON: {"password": "your_password"})
- `GET /generate_password` - Generate a secure random password

## Files

- `main.py`: Flask application with password analysis endpoints
- `templates/index.html`: Web interface
- `requirements.txt`: Python dependencies

## Educational Purpose

This tool helps understand:
- What makes a password strong or weak
- How password length and complexity affect security
- Why common passwords are dangerous
- Basic concepts of entropy and brute-force attacks
- The importance of using unique, complex passwords

## Notes for Security Awareness Training

- Never use real passwords in demonstration tools
- This estimator assumes offline attacks; online rates are much lower due to rate limiting
- Real-world attacks may use dictionaries, patterns, or leaked databases
- Consider using a password manager to generate and store strong, unique passwords