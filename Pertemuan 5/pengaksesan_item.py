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

print("id:", profile["id"])

print("name:", profile.get("name"))
