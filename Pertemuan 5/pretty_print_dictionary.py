profile = {
    "id": 2,
    "name":"john wick",
    "hobbies":["playing with pencil"],
    "is_female": False,
}

import pprint
pprint.pprint(profile)

import json
print(json.dumps(profile, indent=4))