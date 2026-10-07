profile = {
    "id": 2,
    "name":"mario",
    "hobbies":["playing with luigi","saving the mushroom kingdom"],
    "is_female": False,
    "affiliations": [
        {
            "name":"luigi",
            "affiliations":"brother"
        },
        {
            "name": "mushroom kingdom",
            "affiliations":"protector"
        },
    ]
}

print("name:", profile["name"])
print("hobbies:", profile["hobbies"])
print("affiliations:")

for item in profile["affiliations"]:
    print(" -> %s(%s)" % (item["name"],item["affiliations"]))
