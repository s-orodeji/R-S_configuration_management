""""This is a simple nornir automation script"""
from nornir import Initnornir #pylint: disable=import-error
from nornir.plugins.tasks.networking import napalm_get #pylint: disable=import-error
from nornir.plugins.functions.text import print_results #pylint: disable=import-error

NR = Initnornir(config_file="config.yaml")

RESULTS = NR.run(
			 napalm_get,
			 getters=['get_facts'])

print_results(RESULTS)
