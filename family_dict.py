my_family = {
    "father": {
        "name": "David",
        "age": 55
    },
    "mother": {
        "name": "Brenda",
        "age": 53
    },
    "sister": {
        "name": "Shelby",
        "age": 26
    }
}

for (member, info) in my_family.items():
    print(f"{info['name']} is my {member} and is {str(info['age'])} years old.")