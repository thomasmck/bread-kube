#!/usr/bin/env python3.8

from flask import Flask
from redis import Redis, RedisError

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
