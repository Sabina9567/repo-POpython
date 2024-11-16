import json

def task() -> float:
    try:
        with open('input.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: input.json not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

    total_product = 0
    for item in data:
        score = item.get("score")
        weight = item.get("weight")

        if score is not None and weight is not None:
            try:
                total_product += score * weight
            except TypeError:
                print("Error: 'score' or 'weight' is not a number.")
                return None

    return round(total_product, 3)

if __name__ == "__main__":
        result = task()
        if result is not None:
            print(result)
