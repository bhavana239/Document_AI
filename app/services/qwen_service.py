import requests
import json
import re


def parse_bom_with_qwen(headers, rows):

    print("\n✅ USING QWEN FOR BOM PARSING...\n")

    bom_table = "Headers:\n"
    bom_table += " | ".join(headers)
    bom_table += "\n\nRows:\n"

    for row in rows:
        bom_table += " | ".join(row) + "\n"

    prompt = f"""
You are an expert Mechanical Engineering BOM parser.
Map columns from the input BOM table to these specific output fields:
1. partNumber
2. description
3. material
4. grade
5. dimensions
6. quantity
7. uom
8. revision
9. drawingNumber
10. assemblyHierarchy
11. notes
12. finishCoating
13. manufacturer

Rules:
1. Map column names to the closest matching field. For example: "Part No." -> partNumber, "Name" -> description, "Material" -> material, "Qty" -> quantity.
2. If a field is not present in the table columns, return it as empty string "" (or 0 for quantity, and "NOS" for uom).
3. Do NOT modify the values. Return exact values.
4. Quantity must be returned as an integer.
5. Return ONLY valid JSON block.

Example:
If input is:
Headers:
Part No. | Name | Material | Qty
Rows:
1 | Crank | Forged Steel | 1

Output:
```json
{{
  "bom": [
    {{
      "partNumber": "1",
      "description": "Crank",
      "material": "Forged Steel",
      "grade": "",
      "dimensions": "",
      "quantity": 1,
      "uom": "NOS",
      "revision": "",
      "drawingNumber": "",
      "assemblyHierarchy": "",
      "notes": "",
      "finishCoating": "",
      "manufacturer": ""
    }}
  ]
}}
```

Now, map this engineering BOM table:

{bom_table}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    print("✅ RESPONSE RECEIVED FROM QWEN")

    output = result["response"].strip()

    # Robust extraction of JSON from markdown blocks or plain text
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", output, re.DOTALL | re.IGNORECASE)
    if json_match:
        json_str = json_match.group(1)
    else:
        # Fallback to finding the first { and last }
        start = output.find('{')
        end = output.rfind('}')
        if start != -1 and end != -1:
            json_str = output[start:end+1]
        else:
            json_str = output

    return json.loads(json_str.strip())
