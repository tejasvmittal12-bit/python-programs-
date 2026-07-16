pasta = ("Pasta Arrabbiata", "Italian" ,20, "Medium")
biryani = ("Veg Biryani", "Indian", 45, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])
all_recipes = [pasta, biryani]
print("\nFirst Recipe Name:", all_recipes[0][0])
print("Second Recipe Time   :", all_recipes[1][2], "mins")
print("Pasta Details (sliced):", pasta[1:3])

print("\nPasta Recipe Details:")
for detail in pasta:
    print(" -", detail)

pasta_ingredients = {"Pasta", "Tomato", "Chili", "Garlic", "Olive Oil"}
biryani_ingredients = {"Rice", "Vegetables", "Spices", "Yogurt", "Coriander"}
print("\nPasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)
print("Total Ingredients in Pasta:", len(pasta_ingredients))

pasta_ingredients.add("Parmesan")
pasta_ingredients.discard("Chili")
print("\nUpdated Pasta Ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nCommon Ingredients (union):", all_ingredients)
print("common Ingredients (intersection):", common)
print("only Pasta (difference):", only_pasta)
print("Not Shared (sym. difference):", unique_to_each)
