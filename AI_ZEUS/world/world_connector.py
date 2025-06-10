class WorldConnector:
    def __init__(self):
        self.connections = {}

    def connect(self, name, api_client):
        self.connections[name] = api_client

    def send(self, name, data):
        if name in self.connections:
            return self.connections[name].send(data)
        return None
