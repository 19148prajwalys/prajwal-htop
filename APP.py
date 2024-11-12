from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get server's username
    username = os.getlogin()
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    # Get `top` output
    top_output = subprocess.getoutput("top -b -n 1 | head -n 10")
    # Define HTML output
    output = f"""
    <html>
    <head><title>Htop Info</title></head>
    <body>
        <h1>Htop Information</h1>
        <p><strong>Name:</strong> Your Full Name</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time in IST:</strong> {current_time}</p>
        <pre><strong>Top Output:</strong><br>{top_output}</pre>
    </body>
    </html>
    """
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
