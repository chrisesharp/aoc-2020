def remove(ingredient, allergens):
    result = set()
    for k in allergens:
        if len(allergens[k])>1 and ingredient in allergens[k]:
            allergens[k].remove(ingredient)
            if len(allergens[k])==1:
                result |= allergens[k]
    return result

class Allergens:
    def __init__(self, data):
        all_allergens = {}
        all_ingredients = []
        for entry in data:
            ingredients, allergens = entry.rstrip(")").split("(contains ")
            ingredients = ingredients.split()
            all_ingredients.append(ingredients)
            for a in allergens.split(", "):
                if a not in all_allergens: 
                    all_allergens[a] = set(ingredients)
                else:
                    all_allergens[a] &= set(ingredients)
        self.all_allergens = all_allergens
        self.all_ingredients = all_ingredients

    def sum(self):
        all_allergens = set(i for ingredients in self.all_allergens.values() for i in ingredients)
        return sum(i not in all_allergens for ingredients in self.all_ingredients for i in ingredients)

    def pt2(self):
        single_ingredients = next(list(v) for v in self.all_allergens.values() if len(v)==1)
        while single_ingredients: 
            single_ingredients += list(remove(single_ingredients.pop(), self.all_allergens))
        return ','.join(str(i.pop()) for a,i in sorted((k,v) for k,v in self.all_allergens.items()))

if __name__ == '__main__':
    data = open('input.txt').read().splitlines()
    allergens = Allergens(data)
    print("Part 1:", allergens.sum())
    print("Part 2:", allergens.pt2())