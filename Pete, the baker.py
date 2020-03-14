def cakes(recipe, available):

    # if recipe ingredients are more than available ingredients then return 0
    if len(recipe) > len(available):
        return 0
    else:
        recipe_arr = []
        avl_arr = []
        
        # Store Recipies names in arrays
        for x in recipe:
            recipe_arr.append(x)
        for y in available:
            avl_arr.append(y)
        
        result = []
        
        #stores the dividing result in an array
        for z in recipe_arr:
            num = available[z] / recipe[z]
            result.append(num)
        
        # return the minimum result 
        return min(result)