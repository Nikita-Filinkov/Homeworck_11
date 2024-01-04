import json


def load_candidates_from_json():
    with open('candidates.json', 'r') as file:
        data = json.load(file)
        return data


def all_name():
    names = []
    for item in load_candidates_from_json():
        names.append(item["name"])
    return names


def get_candidate(uid):
    for item in load_candidates_from_json():
        if item["id"] == uid:
            return {
                "name": item["name"],
                "position": item["position"],
                "picture": item["picture"],
                "skills": item["skills"],
            }
    return {"Not found": "Ушёл на обед"}


def get_candidate_by_name(name):
    candidates_from_name = []
    for item in load_candidates_from_json():
        if name.lower() in item["name"].lower():
            candidates_from_name.append(item)
    return candidates_from_name


def get_candidate_by_skill(skills):
    candidates_from_skills = []
    for item in load_candidates_from_json():
        if skills.lower() in item["skills"].lower():
            candidates_from_skills.append(item)
    return candidates_from_skills
