
class CNOTGate:
    """ 0 means active at low, 1 means active at high,
    2 means NOT gate
    """
    def __init__(self, gate):
        self.gate = gate
        self.n_bits = len(self.gate)

    def run(self, bits):
        inverted = 1
        target = 0
        for i, gate_param in enumerate(self.gate):
            if gate_param != 2:
                if gate_param == 1 and bits[i] == 1:
                    inverted &= 1
                elif gate_param == 0 and bits[i] == 0:
                    inverted &= 1
                elif gate_param == 3:
                    continue
                else:
                    return bits
            else:
                target = i
        if inverted:
            r = list(bits[:])
            r[target] = 1 if r[target] == 0 else 0
            return r

class Simulator:
    """run over all possibilities"""
    def __init__(self, gates):
        """take in a list of CNOT gates"""
        self.n_bits = gates[0].n_bits
        self.gates = gates
        
    def run(self):
        result = " ".join("q" for _ in range(self.n_bits))
        result += "    "
        result += "".join("q'" for _ in range(self.n_bits))
        result += "\n"
        result += " ".join([f"{n}" for n in range(self.n_bits)])
        result += " -> "
        result += " ".join([f"{n}" for n in range(self.n_bits)])
        result += "\n" + "-" * (self.n_bits * 5) + "\n"
        for i in range(2**self.n_bits):
            r = [int(b) for b in bin(i)[2:]]
            if len(r) < self.n_bits:
                for _ in range(self.n_bits - len(r)):
                    r.insert(0, 0)
            org = list(r[:])
            for gate in self.gates:
                r = gate.run(r)
            # print(org, "->", r)
            result += " ".join(map(str, org))
            result += " -> "
            result += " ".join(map(str, r))
            result += "\n"
        return result[:-1]

    def get_graph(self):
        r = []
        mapping = {
            0: "○",
            1: "●",
            2: "+"
        }
        for n in range(self.n_bits):
            r.append(f"q{n} --")
        for gate in self.gates:
            for i, gate_param in enumerate(gate.gate):
                r[i] += mapping[gate_param] + "--"
        return "\n".join(r)

class GateParametersException(Exception):
    pass