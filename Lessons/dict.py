"""practice with dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 7, "vanilla": 3} #or you can initialize it as {"chocolate": 12, "vanilla": 8} syntax {"name": value}
ice_cream["mint"] = 3

#adding and removing elements from the dictionary
print("äfter adding mint: ")
print(ice_cream)
ice_cream.pop("mint")
print("after removing mint: ")
print(ice_cream)

#accessing
print(f"number of vanilla orders: {ice_cream['vanilla']}")
ice_cream["vanilla"] += 1
print("after adding 1 vanilla")
print(ice_cream)
#checking if in dictionary

print("mint" in ice_cream)
print("chocolate" in ice_cream)

