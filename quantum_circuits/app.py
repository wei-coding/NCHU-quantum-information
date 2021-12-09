from flask import Flask, render_template, request
from flask.helpers import send_file
from utils.logics import CNOTGate, Simulator


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def simulate():
    r = request.values["logicgates"]
    ori = request.values["logicgates"]
    # print(r)

    # run simulator
    gates_string = r.strip().split("\n")
    for i in range(len(gates_string)):
        gates_string[i] = gates_string[i].strip()
    # print(gates_string)
    gates = []
    for gate_string in gates_string:
        gates_param = [int(g) for g in gate_string.split(" ")]
        # print(gates_param)
        gates.append(CNOTGate(gates_param))
    sim = Simulator(gates)
    r = sim.run()
    # print(ori)
    return render_template('index.html', truth_table=r, original_gates=ori, graph=sim.get_graph())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)