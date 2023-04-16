from flask import Flask

app =Flask(__name__)

@app.route("/")
def hell0_world():
  return "hell0_world"



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)