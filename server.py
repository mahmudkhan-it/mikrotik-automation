from flask import Flask, render_template, request, jsonify
import main
import result_output
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
        if main.dev_name == "Mahmud Khan":
            main.routerConfig()
        # CSV OUTPUT
        result_output.outputToCSV(main.outputDataCSV)
        # Clear router and cmd
        main.ROUTERS=[]
        main.cmdList=[]
        main.outputLog=[]
        main.outputDataCSV=[]
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
    print(main.banner)
    app.run(debug=True,port=8080)