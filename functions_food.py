def test_recipe(main, dessert):
    return "Delicious " + main + " and a mindblowing " + dessert + " as a dessert."

main = "quiche"
dessert = "creme_brule"
meal = test_recipe(main, dessert)
print(meal)