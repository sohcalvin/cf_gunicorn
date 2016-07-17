from flask import Flask
# from werkzeug.contrib.fixers import ProxyFix ## For Gunicorn <<<-----------
import os
import json
app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def home():
    # vcap_svc = os.environ.get('VCAP_SERVICES')
    # vcap_svc= json.loads(json.dumps(vcap_svc))
    # return "home success {0}<hr> {1}<hr>{2}".format(vcap_svc, os.environ) ,200
    return "gunicorn says hello", 200

# app.wsgi_app = ProxyFix(app.wsgi_app) ## For Gunicorn <<<<<---------------
if __name__ == '__main__':
    # for index, each in enumerate(sorted(os.environ.items())):
    #                    print(index, each)

    port = int(os.getenv("PORT", 9099))

    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)
