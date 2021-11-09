class CNOTGate:
    """ 0 means active at low, 1 means active at high,
    2 means NOT gate
    """
    def __init__(self, *args):
        self.gates = args

    def run(self, *args):
        inverted = 1
        target = 0
        for i, gate in enumerate(self.gates):
            if gate != 2:
                if gate == 1 and args[i] == 1:
                    inverted &= 1
                elif gate == 0 and args[i] == 0:
                    inverted &= 1
                else:
                    return list(args)
            else:
                target = i
        if inverted:
            r = list(args[:])
            r[target] = 1 if r[target] == 0 else 0
            return r
