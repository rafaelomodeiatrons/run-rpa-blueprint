import json
import time
import requests
from typing import Any, Dict, List

ENDPOINT = "http://localhost:3000/automations/blueprint-runner/activate"
TENANT_ID = "0192d800-65a7-7f49-83aa-80739accb137"

# Ajuste aqui (segundos)
SLEEP_MINUTES = 0

# Arquivo com os 671 itens (o que você gerou)
JSON_FILE_PATH = "blueprints_belo_horizonte_mg_indice_2026-02-17.json"


def load_items(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("O JSON precisa ser um array (lista) de objetos.")
    return data


def normalize_payload(item: Dict[str, Any]) -> Dict[str, Any]:
    """
    Se o item vier no formato wrapper (tem chave 'blueprint'),
    retorna somente o objeto blueprint (formato que o endpoint espera).
    Caso contrário, retorna o item como está.
    """
    if (
        isinstance(item, dict)
        and "blueprint" in item
        and isinstance(item["blueprint"], dict)
    ):
        return item["blueprint"]
    return item


def post_activate(payload: Dict[str, Any]) -> requests.Response:
    headers = {
        "Content-Type": "application/json",
        "x-tenant-id": TENANT_ID,
    }
    return requests.post(ENDPOINT, headers=headers, json=payload, timeout=60)


def main() -> None:
    items = load_items(JSON_FILE_PATH)
    total = len(items)

    print(f"Carregado {total} itens do arquivo: {JSON_FILE_PATH}")
    print(f"Endpoint: {ENDPOINT}")
    print(f"Sleep: {SLEEP_MINUTES} minuto(s) entre requisições\n")

    for i, item in enumerate(items, start=1):
        payload = normalize_payload(item)

        # debug rápido pra garantir que está no formato certo
        blueprint_id = payload.get("id", "")
        tenant_in_body = (payload.get("ids") or {}).get("tenantId", "")
        indice = ""
        vars0 = (payload.get("variables") or [{}])[0]
        if isinstance(vars0, dict):
            indice = vars0.get("indice", "")

        print(
            f"[{i}/{total}] POST blueprint.id={blueprint_id} tenantId(body)={tenant_in_body} indice={indice}"
        )

        try:
            resp = post_activate(payload)
            print(f"  -> Status: {resp.status_code}")

            # Se quiser ver retorno:
            if resp.content:
                print(f"  -> Response: {resp.text[:300]}")

            # Se quiser parar ao primeiro erro HTTP:
            # resp.raise_for_status()

        except requests.RequestException as e:
            print(f"  !! Erro na requisição: {e}")

        if i < total:
            time.sleep(SLEEP_MINUTES)

    print("\nFinalizado!")


if __name__ == "__main__":
    main()
