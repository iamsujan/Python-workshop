list1 = ["Black", "Red", "Maroon", "Yellow"]
list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color': f, 'code': c} for f, c in zip(list1, list2)])