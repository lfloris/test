from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis

app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/> \
           <b>I have just updated this app with an automated CICD pipeline!</b> "
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())
    return 'My hostname is %s'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
