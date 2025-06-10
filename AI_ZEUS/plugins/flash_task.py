class Skill:
    def execute(self, **kwargs):
        from time import time
        start = time()
        result = "⚡ Flash executed: " + str(kwargs)
        elapsed = (time() - start) * 1000
        return f"{result} in {elapsed:.2f}ms"
