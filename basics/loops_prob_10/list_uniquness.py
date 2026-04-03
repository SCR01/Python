items = ["apple", "banana", "orange", "apple", "grape"]

# unique_items = []
# for item in items:
#     if item not in unique_items:
#         unique_items.append(item)

# print("Unique items:", unique_items) for the uniqe items

#for duplicates
# duplicates = []
# for i in items:
#     if items.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)

# print("Duplicate items:", duplicates)

unique = set()

for item in items:
    if item is unique:
        print("item is:", item)
        break
    unique.add(item)

print("Unique items:", unique)