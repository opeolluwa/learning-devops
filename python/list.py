names = ["alex", "mike", "miles"]

for index in range(len(names) - 1):
    print(f"the item in the {index} index is {names[index]}")
    # del names[index]


print(names[1:12])


exists = "alex" in names
notExits = "brad" not in names

print(exists)
print(notExits)

# find the index of an entry.
index = names.index("alex") or None


# has insert, append remove, remove to find the element and removet it at the present index, the sort to re-organize.

countries = ["spain", "germany", "creece"]
countries.sort()
print(countries)
