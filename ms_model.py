import json

class MicroService:
    def __init__(self, path):
        file = open(path)
        model = json.load(file)
        file.close()

        self.router_url = "ws://crossbar_router:8080/ws"
        self.router_realm = "realm"

        subs, pubs = {}, {}

        for topic in model['subscribe-topics']:
            subs[topic] = f"com.airvisor/{topic}"

        for topic in model['publish-topics']:
            pubs[topic] = f"com.airvisor/{topic}"

        self.subscribe_topics = subs
        self.publish_topics = pubs

def load_ms_model(path='model.json'):
    return MicroService(path)
