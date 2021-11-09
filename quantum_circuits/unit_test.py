from utils.logics import CNOTGate

c = CNOTGate(0, 1, 1, 2)

print(c.run(0, 1, 1, 0))
