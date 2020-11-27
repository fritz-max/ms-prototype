# autobahn + twisted(event handling lib in python)
from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks

# from dir
from fake_instrument_driver import Instrument
from ms_model import load_ms_model
service = load_ms_model()


component = Component(transports=service.router_url,
                      realm=service.router_realm)


@component.on_join
@inlineCallbacks
def joined(session, details):
    instrument = Instrument()
    publish_interval = 0.1
    while instrument.heartbeat:
        measurement = instrument.get_measurement()
        session.publish(service.publish_topics["gps"], *measurement)
        session.publish(service.publish_topics['heartbeat'], instrument.ID)
        yield sleep(publish_interval)


if __name__ == '__main__':
    run([component])
