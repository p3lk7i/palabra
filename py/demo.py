from parse import parse_plb

sample = """
[1:]Cars
    [2:Brand]Tesla
        [3:Model]Model S
            [4:Battery]100 kWh
            [4:Autopilot]Full Self-Driving
    [2:Brand]Toyota
        [3:Model]Prius
            [4:Engine]Hybrid
// that's it
"""

import json, sys
print(json.dumps(parse_plb(sample), indent=2))
