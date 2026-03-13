import json
import copy

TEMPLATE_FILE = "blueprint_template.json"
OUTPUT_FILE = "cnd_bh_57.json"

REGISTROS = [
    {"indice": "100137401", "cpfOuCnpjOuEndereco": "9605511000101"},
    {"indice": "100170705", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "100170706", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "100172256", "cpfOuCnpjOuEndereco": "34291319000135"},
    {"indice": "2470446", "cpfOuCnpjOuEndereco": "12093990000139"},
    {"indice": "196797", "cpfOuCnpjOuEndereco": "7737816000141"},
    {"indice": "196800", "cpfOuCnpjOuEndereco": "7737816000141"},
    {"indice": "1973185", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "1973193", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "1973207", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "1973215", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "1973223", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "2072157", "cpfOuCnpjOuEndereco": "391"},
    {"indice": "2082764", "cpfOuCnpjOuEndereco": "644"},
    {"indice": "208868", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "208876", "cpfOuCnpjOuEndereco": "6541273000120"},
    {"indice": "233137", "cpfOuCnpjOuEndereco": "332"},
    {"indice": "251895", "cpfOuCnpjOuEndereco": "1345"},
    {"indice": "251909", "cpfOuCnpjOuEndereco": "61139718053"},
    {"indice": "2555980", "cpfOuCnpjOuEndereco": "23"},
    {"indice": "2555999", "cpfOuCnpjOuEndereco": "6710"},
    {"indice": "2556006", "cpfOuCnpjOuEndereco": "6706"},
    {"indice": "2556014", "cpfOuCnpjOuEndereco": "6698"},
    {"indice": "2556022", "cpfOuCnpjOuEndereco": "27"},
    {"indice": "2556030", "cpfOuCnpjOuEndereco": "23"},
    {"indice": "2556049", "cpfOuCnpjOuEndereco": "23"},
    {"indice": "2556057", "cpfOuCnpjOuEndereco": "23"},
    {"indice": "2556065", "cpfOuCnpjOuEndereco": "23"},
    {"indice": "2556073", "cpfOuCnpjOuEndereco": "23"},
    {"indice": "2556081", "cpfOuCnpjOuEndereco": "23"},
    {"indice": "256552", "cpfOuCnpjOuEndereco": "358"},
    {"indice": "260800", "cpfOuCnpjOuEndereco": "5012206000155"},
    {"indice": "2790769", "cpfOuCnpjOuEndereco": "41924940000"},
    {"indice": "3533050", "cpfOuCnpjOuEndereco": "31662030010"},
    {"indice": "472395", "cpfOuCnpjOuEndereco": "1335"},
    {"indice": "51020", "cpfOuCnpjOuEndereco": "18369508000127"},
    {"indice": "570001", "cpfOuCnpjOuEndereco": "88916549000171"},
    {"indice": "640417", "cpfOuCnpjOuEndereco": "2614"},
    {"indice": "640425", "cpfOuCnpjOuEndereco": "05674930082"},
    {"indice": "6650015", "cpfOuCnpjOuEndereco": "11457194000175"},
    {"indice": "6868800", "cpfOuCnpjOuEndereco": "401"},
    {"indice": "780847", "cpfOuCnpjOuEndereco": "92691765000133"},
    {"indice": "79162", "cpfOuCnpjOuEndereco": "1195"},
    {"indice": "79170", "cpfOuCnpjOuEndereco": "1195"},
    {"indice": "8811741", "cpfOuCnpjOuEndereco": "22627792000161"},
    {"indice": "9029281", "cpfOuCnpjOuEndereco": "4167"},
    {"indice": "9029303", "cpfOuCnpjOuEndereco": "4167"},
]


def normalize_registro(registro):
    if isinstance(registro, dict):
        return {
            chave: "" if valor is None else str(valor)
            for chave, valor in registro.items()
        }

    return {"indice": "" if registro is None else str(registro)}


def ensure_variables_dict(blueprint):
    variables = blueprint.get("variables")

    if not isinstance(variables, list) or not variables:
        blueprint["variables"] = [{}]
        return blueprint["variables"][0]

    if not isinstance(variables[0], dict):
        blueprint["variables"][0] = {}

    return blueprint["variables"][0]


with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template = json.load(f)

blueprints = []
for registro in REGISTROS:
    bp = copy.deepcopy(template)
    variables = ensure_variables_dict(bp)
    variables.update(normalize_registro(registro))
    blueprints.append(bp)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(blueprints, f, ensure_ascii=False, indent=2)

print(f"OK -> {OUTPUT_FILE} gerado com {len(blueprints)} itens")
