class DummyBackend:
    def run(self, task):
        return f"Ran task: {task}"

class ComputeFabric:
    def __init__(self):
        self.backends = {"dummy": DummyBackend()}

    def register_backend(self, name, backend):
        self.backends[name] = backend

    def dispatch_task(self, task, prefer_quantum=False):
        return self.backends["dummy"].run(task)
