import json
with open("Note.json", "r") as f:
    jsone = json.loads(f)

    for i in jsone['notes']:
        print(i['Title'])

