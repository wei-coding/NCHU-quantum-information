from utils.logics import CNOTGate, Simulator

sim = Simulator([
    # CNOTGate([1, 1, 2]),
    CNOTGate([-1, 1, 2])
])

print(sim.run())