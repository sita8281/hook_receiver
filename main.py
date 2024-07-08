from flask import Flask, request
import git
import os

app = Flask(__name__)


@app.route('/hook-xjfGfGPytrFfgHJJeq74hfj.rh8.ehdhf4851fhgj', methods=['post'])
def main():
    hook = request.json
    if hook['ref'] == 'refs/heads/main':
        print('push-event')
        g = git.cmd.Git('/home/deil_admin/flask_app')
        g.pull()
        print('git-push-success')
        os.system('systemctl restart deil-server')
        print('deil-server-restarted')

    return 'OK', 200


app.run(host='0.0.0.0', port=57113)
