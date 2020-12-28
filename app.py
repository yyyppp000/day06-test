import time
from flask import Flask

app = Flask(__name__)
hit = 0
def get_hit_count():
  retries = 5
  while True:
    try:
      global hit
      hit += 1
      return hit
    except redis.exceptions.ConnectionError as exc:
      if retries == 0:
        raise exc
      retries -= 1
      time.sleep(0.5)

@app.route('/')
def hello():
  count = get_hit_count()
  return 'Hello World! I have been seen {} times.\n'.format(count)
