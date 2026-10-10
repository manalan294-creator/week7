items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

long_name_count = 0
for item in items:
    if len(item) > 4:
        long_name_count += 1

print(f"Number of items with more than 4 letters: {long_name_count}")

longest_item = items[0]
for item in items[1:]:
    if len(item) > len(longest_item):
        longest_item = item

print(f"Longest item name: {longest_item}")
