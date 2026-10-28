class Worker:
    def __init__(self, id, name, position, energy=100):
        self.id = id
        self.name = name
        self.position = position
        self.energy = energy

    def work(self, hours):
        self.energy -= 10 * hours

class Boss:
    def __init__(self, name):
        self.name = name

    def order(self, worker, hours=1):
        worker.work(hours)
        print(f"{self.name} ordered {worker.name} to work for {hours} hours. Worker energy left is {worker.energy}")



mermaid = Worker(11225, "Mermaid", "Lumper")
poseidon = Boss("Poseidon")

poseidon.order(mermaid, 3)
