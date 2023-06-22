from flask import Flask, render_template, request, jsonify
import main

app = Flask(__name__)


# =========================
# HOME PAGE
# =========================
@app.route("/")
def index():
    return render_template('index.html')

# =========================
# ROUTER AUTOMATION EXE
# =========================
output = []
@app.route('/ip', methods=['Post','Get'])
def ip():
    if request.method == 'POST':
        ipList = request.form['ipList']
        userName = request.form['userName']
        password = request.form['pass']
        command = request.form['cmd']

        # CMD in arr
        cmdArr = command.split("\n")
        for cmd in cmdArr:
            a = cmd.replace("\r","")
            main.cmdList.append(a)
            print(f"cmd add=> {a}")
        # for test
        summery = main.outputLog



        # input ip to array
        ipListarr = ipList.split()
        for ip in ipListarr:
            main.ipTOdic(ip,userName,password)
            print(f"router add")

        # start router configuration
        main.routerConfig()

        # Clear router and cmd
        main.ROUTERS=[]
        main.cmdList=[]
        main.outputLog=[]


        return render_template('test.html', data = summery)
    else:
        return render_template('ip.html')


@app.route("/log-api")
def logApi():
    return jsonify(main.outputLog)

# =========================
#   START SERVER
# =========================
if __name__ == '__main__':
    app.run(debug=True,port=8080)