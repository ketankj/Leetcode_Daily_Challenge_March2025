# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.

 

# Example 1:

# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# Example 2:

# Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# Example 3:

# Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

from collections import deque, defaultdict

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        # Set of supplies we already have
        available = set(supplies)
        # Result list to store the recipes we can create
        result = []
        
        # Map ingredients to their corresponding recipe indices for easy lookup
        recipe_map = {recipe: ingredients[i] for i, recipe in enumerate(recipes)}
        
        # Queue to process recipes that can be created
        queue = deque()
        
        # Start by adding all the recipes that can be made from initial supplies
        for i, recipe in enumerate(recipes):
            if all(ingredient in available for ingredient in ingredients[i]):
                queue.append(recipe)
                available.add(recipe)  # Add the recipe to available supplies
                
        # Process the queue until it's empty
        while queue:
            current_recipe = queue.popleft()
            result.append(current_recipe)  # Add the recipe to the result
            
            # Check all recipes and try to make them with the available supplies
            for i, recipe in enumerate(recipes):
                if recipe not in available and all(ingredient in available for ingredient in ingredients[i]):
                    queue.append(recipe)
                    available.add(recipe)
                    
        return result

        


s = Solution()
recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
print(s.findAllRecipes(recipes))  
