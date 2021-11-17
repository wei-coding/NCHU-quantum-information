
class CNOTGate:
    """ 0 means active at low, 1 means active at high,
    2 means NOT gate
    """
    def __init__(self, gates):
        self.gates = gates
        self.n_bits = len(self.gates)

    def run(self, bits):
        inverted = 1
        target = 0
        for i, gate in enumerate(self.gates):
            if gate != 2:
                if gate == 1 and bits[i] == 1:
                    inverted &= 1
                elif gate == 0 and bits[i] == 0:
                    inverted &= 1
                elif gate == 3:
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
        result = ""
        for i in range(2**self.n_bits):
            r = [int(b) for b in bin(i)[2:]]
            if len(r) < self.n_bits:
                for _ in range(self.n_bits - len(r)):
                    r.insert(0, 0)
            org = list(r[:])
            for gate in self.gates:
                r = gate.run(r)
            # print(org, "->", r)
            result += f"{org} -> {r}\n"
        return result

class GateParametersException(Exception):
    pass