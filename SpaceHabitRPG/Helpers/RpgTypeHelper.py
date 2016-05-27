import json

def convert_rpgtype_to_json(model):
    id = model.id
    model._dict['_id']= str(id)
    j = json.dumps(model._dict)
    model._dict['_id']= id
    return j