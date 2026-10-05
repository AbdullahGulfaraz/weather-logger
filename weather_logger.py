def summarize(temps):
    min_val = min(temps)
    max_val = max(temps)
    avg_val = sum(temps) / len(temps)

    # Format integers cleanly if whole numbers (e.g. 25 instead of 25.0)
    if min_val.is_integer():
        min_val = int(min_val)
    if max_val.is_integer():
        max_val = int(max_val)

    return {"minimum": min_val, "maximum": max_val, "average": avg_val}

temps = []

while True:
    entry = input("Enter temperature ('done' to stop): ")
    if entry == "done":
        break
    temps.append(float(entry))

result = summarize(temps)
print(result)