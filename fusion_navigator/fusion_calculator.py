#!/usr/bin/env python
# coding: utf-8
# In[ ]:


# open json file and read contenta as a list of dictionaries
with open('personae.json', 'r') as fp:
    personae = json.load(fp)

with open('combos2.json', 'r') as fp:
    arcana2Combos = json.load(fp)

with open('combos3.json', 'r') as fp:
    arcana3Combos = json.load(fp)

with open('specialCombos.json', 'r') as fp:
    specialCombos = json.load(fp)


# In[3]:


class PersonaCompendiumExtracted:
    def __init__(self, name, level, skills):
        self.name = name
        self.level = level
        self.skills = skills

import json

# Load the JSON file
with open('persona_compendium_save_file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
# Create Persona objects
personas_compendium_extracted = [PersonaCompendiumExtracted(item['name'], item['level'], item['skills']) for item in data]

for persona in personae:
    persona['base_level+5'] = persona['level'] + 5 # max social links lead to a +5 bonus
    persona['base_level'] = persona['level']

# overwrite 'personae' with the new list
for persona_compendium_extracted in personas_compendium_extracted:
    for persona in personae:
        if persona_compendium_extracted.name.lower() == persona['name'].lower():
            persona['level'] = persona_compendium_extracted.level
            persona['skills'] = persona_compendium_extracted.skills
            break


print(personae)


# In[4]:


for persona in personae:
    # if persona does not have 'skills' key print the name
    if 'skills' not in persona:
        print(persona['name'])


# In[12]:


import math


def generate_arcana_rank(personae):
    arcana_rank = {}
    rank = 0
    last_arcana = None
    for persona in personae:
        if persona['arcana'] == last_arcana:
            continue
        last_arcana = persona['arcana']
        arcana_rank[persona['arcana']] = rank
        rank += 1
    return arcana_rank

# Assuming 'personae' is a list of dictionaries with an 'arcana' key.
# You need to define or import this list from your data.
arcana_rank = generate_arcana_rank(personae)

def generate_personae_by_name(personae):
    personae_by_name = {}
    for persona in personae:
        personae_by_name[persona['name']] = persona
    return personae_by_name

personae_by_name = generate_personae_by_name(personae)

def generate_personae_by_arcana(personae):
    personae_by_arcana = {}
    for persona in personae:
        arcana = persona['arcana']
        if arcana not in personae_by_arcana:
            personae_by_arcana[arcana] = []
        personae_by_arcana[arcana].append(persona)
    return personae_by_arcana

# Assuming 'personae' is a list of dictionaries with at least an 'arcana' key.
# You need to define or import this list from your data.
personae_by_arcana = generate_personae_by_arcana(personae)




class CalcCtrl:
    def __init__(self, persona_name, is_intermediate_fusion=False):
        self.ceil = math.ceil
        
        self.level_key = 'base_level'

        if is_intermediate_fusion:
            self.current_level_key = 'base_level+5'
        else:
            self.current_level_key = 'level'

        self.persona = personae_by_name.get(persona_name)

        self.all_recipes = []  # Consider renaming this to just 'recipes' for consistency with other methods
        if self.persona:
            self.get_recipes()
            self.all_recipes.sort(key=lambda x: x['cost'])
            self.max_cost = max(recipe['cost'] for recipe in self.all_recipes) if self.all_recipes else 0

    @staticmethod
    def get_rank(persona):
        return arcana_rank[persona['arcana']]

    def add_recipe(self, recipe):
        recipe['cost'] = sum((27 * source[self.level_key]**2 + 126 * source[self.level_key] + 2147) for source in recipe['sources'])
        recipe['sources'].sort(key=lambda x: (-x[self.level_key], self.get_rank(x)))
        self.all_recipes.append(recipe)

    def fuse2(self, arcana, persona1, persona2):
        level = 1 + (persona1[self.level_key] + persona2[self.level_key]) // 2
        personae = personae_by_arcana[arcana]

        for i, persona in enumerate(personae):
            if persona[self.level_key] >= level:
                if persona.get('special'):
                    continue
                break

        if persona1['arcana'] == persona2['arcana']:
            i -= 1
        if i < len(personae) and (personae[i] == persona1 or personae[i] == persona2):
            i -= 1

        return personae[max(i, 0)]  # Ensure i doesn't go below 0

    def fuse3(self, arcana, persona1, persona2, persona3):
        level = 5 + (persona1[self.level_key] + persona2[self.level_key] + persona3[self.level_key]) // 3
        personae = personae_by_arcana[arcana]

        found = False
        for i, persona in enumerate(personae):
            if persona[self.level_key] >= level:
                if persona.get('special'):
                    continue
                found = True
                break

        if not found:
            return None

        # In same arcana fusion, skip over the ingredients.
        if persona1['arcana'] == arcana and persona2['arcana'] == arcana and persona3['arcana'] == arcana:
            while (i < len(personae) and (persona1['name'] == personae[i]['name'] or
                                          persona2['name'] == personae[i]['name'] or
                                          persona3['name'] == personae[i]['name'])):
                i += 1
                if i >= len(personae):
                    return None

        return personae[i] if i < len(personae) else None
    
    def persona3_is_valid(self, persona1, persona2, persona3):
        if persona3 == persona1 or persona3 == persona2:
            return False
        
        if persona1['name'] == 'siegfried' and persona2['name'] == 'kali' and persona3['name'] == 'orthrus':
            print('here')

        if persona1['name'] == 'kali' and persona2['name'] == 'siegfried' and persona3['name'] == 'orthrus':
            print('here')
        
        if persona1['name'] == 'siegfried' and persona2['name'] == 'orthrus' and persona3['name'] == 'kali':
            print('here')
        
        if persona1['name'] == 'orthrus' and persona2['name'] == 'siegfried' and persona3['name'] == 'kali':
            print('here')
        
        if persona1['name'] == 'orthrus' and persona2['name'] == 'kali' and persona3['name'] == 'siegfried':
            print('here')
        
        if persona1['name'] == 'kali' and persona2['name'] == 'orthrus' and persona3['name'] == 'siegfried':
            print('here')


        if persona3[self.current_level_key] < persona1[self.current_level_key] or persona3[self.current_level_key] < persona2[self.current_level_key]:
            return False

        if persona3[self.current_level_key] == persona1[self.current_level_key]:
            return arcana_rank[persona3['arcana']] < arcana_rank[persona1['arcana']]

        if persona3[self.current_level_key] == persona2[self.current_level_key]:
            return arcana_rank[persona3['arcana']] < arcana_rank[persona2['arcana']]

        return True

    def find_3way_recipes(self, arcana1, arcana2):
        step1_recipes = self.get_arcana_recipes(arcana1)
        for step1_recipe in step1_recipes:
            persona1 = step1_recipe['sources'][0]
            persona2 = step1_recipe['sources'][1]
            personae = personae_by_arcana[arcana2]

            for persona3 in personae:
                if self.persona3_is_valid(persona1, persona2, persona3):
                    result = self.fuse3(self.persona['arcana'], persona1, persona2, persona3)
                    if not result or result['name'] != self.persona['name']:
                        continue

                    # filter if persona1,persona2 or persona3 name are equal to result
                    if persona1['name'] == result['name'] or persona2['name'] == result['name'] or persona3['name'] == result['name']:
                        continue

                    self.add_recipe({'sources': [persona1, persona2, persona3]})

    def get_recipes(self):
        # if persona is the target of a special combo, add the recipe
        if self.persona.get('special'):
            for combo in specialCombos:
                if self.persona['name'] == combo['result']:
                    recipe = {'sources': [personae_by_name[source] for source in combo['sources']]}
                    self.add_recipe(recipe)
                    return
        
        # Define filter_2way inside get_recipes
        def filter_2way(persona1, persona2, result):
            # Note: 'self' is accessible here because this is an inner function
            if persona1['name'] ==  self.persona['name']:
                return True
            if persona2['name'] ==  self.persona['name']:
                return True
            if result['name'] ==  self.persona['name']:
                return False
            return True
        

        # first get all normal spread (2 way fusions)
        recipes = self.get_arcana_recipes(self.persona['arcana'], filter_2way)
        for recipe in recipes:
            self.add_recipe(recipe)

        # Consider triangle fusion
        combos = [combo for combo in arcana3Combos if combo['result'] == self.persona['arcana']]
        for combo in combos:
            self.find_3way_recipes(combo['source'][0], combo['source'][1])
            if combo['source'][1] != combo['source'][0]:
                self.find_3way_recipes(combo['source'][1], combo['source'][0])
    
    def get_arcana_recipes(self, arcana_name, filter_callback=None):
        recipes = []
        combos = [x for x in arcana2Combos if x['result'] == arcana_name]

        for combo in combos:
            personae1 = personae_by_arcana[combo['source'][0]]
            personae2 = personae_by_arcana[combo['source'][1]]

            for i, persona1 in enumerate(personae1):
                for j, persona2 in enumerate(personae2):
                    if persona1['arcana'] == persona2['arcana'] and j <= i:
                        continue
                    result = self.fuse2(combo['result'], persona1, persona2)
                    if not result:
                        continue
                    if filter_callback and filter_callback(persona1, persona2, result):
                        continue

                    recipes.append({'sources': [persona1, persona2]})

        return recipes

calc_ctrl = CalcCtrl('chi you', is_intermediate_fusion=False)
#calc_ctrl = CalcCtrl('orpheus telos', is_intermediate_fusion=True)
print(calc_ctrl.all_recipes)


def print_sources(recipes, file):
    for recipe in recipes:
        print("Recipe:", file=file)
        for source in recipe['sources']:
            name = source.get('name', 'Unknown')
            level = source.get('level', 'Unknown')
            arcana = source.get('arcana', 'Unknown')
            special = ' (special)' if source.get('special') else ''
            print(f"  - {name}, Level: {level}, Arcana: {arcana}{special}", file=file)
        cost = recipe.get('cost', 'Unknown')
        print(f"Total Cost: {cost}\n", file=file)




# In[16]:





# In[17]:


# open dataframe located in "/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv"
import pandas as pd
df = pd.read_csv("/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv")


print(df)

skill_type_dict = df.set_index('skill')['type'].to_dict()


# given a skill name return the skill type
def get_skill_type(skill_name):
    return skill_type_dict[skill_name]

print(get_skill_type('Agidyne'))

persona_name = 'chi you'

# load '/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/inheritance.csv' into a dataframe
inheritance_df = pd.read_csv('/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/inheritance.csv')
# load '/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/personas_inheritance.csv' into a dataframe
persona_inheritance_df = pd.read_csv('/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/personas_inheritance.csv')

# get the type of the persona 'chi you' in the persona_inheritance_df
persona_inherit_type = persona_inheritance_df.loc[persona_inheritance_df['Persona'] == persona_name, 'Type'].iloc[0]


# Convert the DataFrame to a dictionary where each key is an inheritance type
# and its value is another dictionary of skill types and their probabilities.
inheritance_dict = inheritance_df.set_index('Inheritance Type').T.to_dict('dict')



# given a skill type return the skill inheritance probability for a given persona type
def get_inheritance_probability(skill_type, persona_inheritance_type):
    # Access the nested dictionary directly for the value
    # Check if the persona_inheritance_type exists to avoid KeyErrors
    if persona_inheritance_type in inheritance_dict:
        # Return the probability value for the given skill_type and persona_inheritance_type
        return inheritance_dict[persona_inheritance_type].get(skill_type, 0)  # Returns 0 if skill_type is not found


print(get_inheritance_probability('Almighty', persona_inherit_type))

#https://web.archive.org/web/20131213184851/http://www.gamefaqs.com/ps2/937269-shin-megami-tensei-persona-3-fes/faqs/52531
''' 
 ============================
 |   Pre-Fusion | Post-Fusion |
 | Total Skills |   Inherited |
  -----------------------------
 |         < 6  |           1 |
 |         6-8  |           2 |
 |        9-11  |           3 |
 |       12-23  |           4 |
 |       24-31  |           5 |
 |   32-39 (?)  |           6 |
 |   40-47 (?)  |           7 |
 |      48 (?)  |           8 |
  ----------------------------
'''

def get_ammount_of_inherited_skills(skills):
    if len(skills) < 6:
        return 1
    elif len(skills) < 9:
        return 2
    elif len(skills) < 12:
        return 3
    elif len(skills) < 24:
        return 4
    elif len(skills) < 32:
        return 5
    elif len(skills) < 40:
        return 6
    elif len(skills) < 48:
        return 7
    else:
        return 8
    
def create_desired_skills_probability_dict(desired_skills):
    desired_skills_probability_dict = {}
    for s in desired_skills:
        skill_type = get_skill_type(s)
        desired_skills_probability_dict[s] = get_inheritance_probability(skill_type, persona_inherit_type)
    return desired_skills_probability_dict
    
def get_best_recipe(desired_skills, recipes_list):

    best_ratio = 0
    best_ratio_max = 0
    best_recipe = recipes_list[0]
    best_set = None

    best_ratio_max = 0
    best_recipe_max = best_recipe
    best_set_max = best_set
    best_skills_max = best_set

    biggest_ammount_of_inherited_skills = 0

    for i in range(len(recipes_list)):
        current_skills = []
        dont_have = False

        lucifer = False
        norn = False
        baal_zebul = False

        for j in range(len(recipes_list[i]['sources'])):
            # if 'skills' key does not exist continue
            if 'skills' not in recipes_list[i]['sources'][j]:
                dont_have = True
                continue
            for s in recipes_list[i]['sources'][j]['skills']:
                current_skills.append(s)
            if recipes_list[i]['sources'][j]['name'] == 'lucifer':
                lucifer = True
            if recipes_list[i]['sources'][j]['name'] == 'norn':
                norn = True
            if recipes_list[i]['sources'][j]['name'] == 'baal zebul':
                baal_zebul = True
            if lucifer and baal_zebul and norn:
                #print('hello')
                None
            
        
        if dont_have:
            continue

        ammount_of_inherited_skills = get_ammount_of_inherited_skills(current_skills)

        

        if ammount_of_inherited_skills > biggest_ammount_of_inherited_skills:
            best_ratio_max = 0
            best_recipe_max = None
            best_set_max = None
            biggest_ammount_of_inherited_skills = ammount_of_inherited_skills
            

        set_current_skills = list(set(current_skills))
        
        #count how many skills of the desired skills are in the current skills
        desired_count = 0
        
        # while 'ammount_of_inherited_skills' is not reached count as many 'desired_skills' as possible. If space still remais count 'noise_skills'
        for s in set_current_skills:
            skill_type = get_skill_type(s)
            if s in desired_skills:
                ratio_skill = get_inheritance_probability(skill_type, persona_inherit_type)
                if ratio_skill > 0:
                    desired_count += 1
        
        
        current_desired_skills = []

        #count how many skills of the desired skills are in the current skills
        desired_count_ratio = 0
        noise_count_ratio = 0
        for s in set_current_skills:
            # get the skill type from the dataframe
            skill_type = get_skill_type(s)

            ratio_skill = get_inheritance_probability(skill_type, persona_inherit_type)
            if s in desired_skills:
                current_desired_skills.append(s)
                desired_count_ratio += ratio_skill
            else:
                noise_count_ratio += ratio_skill

        # should it be 1 or something between? should i switch nominator and denominator?   
        ratio = desired_count_ratio / max(noise_count_ratio,1)

        # the bigger the ratio the better
        if ratio > best_ratio:
            best_ratio = ratio
            best_recipe = recipes_list[i]
            best_set = set_current_skills
            best_desired_skills_prob_dict = create_desired_skills_probability_dict(current_desired_skills)
        
        if desired_count >= biggest_ammount_of_inherited_skills and ammount_of_inherited_skills == biggest_ammount_of_inherited_skills and ratio > best_ratio_max:
            best_ratio_max = ratio
            best_recipe_max = recipes_list[i]
            best_set_max = set_current_skills
            best_skills_max = current_skills
            best_desired_skills_prob_dict_max = create_desired_skills_probability_dict(current_desired_skills)

        if 2185 == i:
            running_ratio = ratio
            running_recipe = recipes_list[i]
            running_set = set_current_skills

    return best_ratio, best_recipe, best_set, best_desired_skills_prob_dict, biggest_ammount_of_inherited_skills, best_ratio_max, best_recipe_max, best_set_max, best_skills_max, best_desired_skills_prob_dict_max, running_ratio, running_recipe, running_set


chi_you_base = CalcCtrl(persona_name, is_intermediate_fusion=False).all_recipes



mandatory_skills = [
'High Counter',
'Unshaken Will',
'Panta Rhei',
]

optional_skills = [
'Wind Boost',
'Wind Amp',
'Spell Master',
'Mind Charge',
'Salvation',
]

desired_skills = mandatory_skills + optional_skills

best_ratio, best_recipe, best_set, best_desired_skills_prob_dict, biggest_ammount_of_inherited_skills, best_ratio_max, best_recipe_max, best_set_max, best_skills_max, best_desired_skills_prob_dict_max, running_ratio, running_recipe, running_set = get_best_recipe(desired_skills=desired_skills, recipes_list=chi_you_base)

print('best')
print(best_ratio)
print(best_recipe)
print(len(best_set))
print(best_set)
print(best_desired_skills_prob_dict)

#print(running_ratio)
#print(running_recipe)
#print(len(running_set))
#print(running_set)

print('bigest')
print(biggest_ammount_of_inherited_skills)
print(best_ratio_max)
print(best_recipe_max)
print(len(best_set_max))
print(best_set_max)
print(len(best_skills_max))
print(best_desired_skills_prob_dict_max)



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)





# In[2]:


get_ipython().system('jupyter nbconvert --to script fusion_calculator.ipynb')


# In[ ]:





# In[16]:


import pandas as pd
# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\inheritable_skills_with_levels.csv')

#print all lines of the dataframe
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)


# In[19]:


import ast

class UnlockableSkill:
    def __init__(self, name, level=None):
        self.name = name
        self.level = level

    def __repr__(self):
        if self.level:
            return f"('{self.name}', lv{self.level})"
        else:
            return f"('{self.name}')"

# Sample data with skills as a string representation of a list
data = {
    'persona': ['abaddon', 'alice'],
    'skill': [
        "['Weary Thrust', 'Evil Smile', 'High Counter']",
        "['Die for Me!(59)', 'Spirit Drain']"
    ]
}

def extract_skills(data):
    skill_dict = {}
    for persona, skills_str in zip(data['persona'], data['skill']):
        # Safely evaluate the string as a list
        skills = ast.literal_eval(skills_str)
        skill_list = []
        for skill in skills:
            # Check if there's a level specified in the skill string
            if '(' in skill and ')' in skill:
                name, level_str = skill.rsplit('(', 1)
                level = int(level_str[:-1])  # Remove the closing parenthesis and convert to int
            else:
                name, level = skill, None

            skill_list.append(UnlockableSkill(name.strip(), level))
        
        skill_dict[persona] = skill_list

    return skill_dict

skill_dict = extract_skills(df)
for persona, skills in skill_dict.items():
    None
    #print(f"{persona}: {skills}")


# verify if for any persona in the dictionary, if it's skills have level numbers that repeat
for persona, skills in skill_dict.items():
    levels = [skill.level for skill in skills]
    # remove 'None' values from the list
    levels = [level for level in levels if level is not None]
    if len(levels) != len(set(levels)):
        print(f"Persona {persona} has repeated levels: {levels}")



# In[22]:


mandatory_skills = [
'High Counter',
'Unshaken Will',
'Panta Rhei',
]

optional_skills = [
'Wind Boost',
'Wind Amp',
'Spell Master',
'Mind Charge',
'Salvation',
]

def separate_keys(previous_skills):
    # Initialize the dictionaries
    accumulated_mandatory_skills = {}
    accumulated_optional_skills = {}
    accumulated_noise_skills = {}

    # Separate the keys into the three dictionaries
    for key, value in previous_skills.items():
        if key in mandatory_skills:
            accumulated_mandatory_skills[key] = value
        elif key in optional_skills:
            accumulated_optional_skills[key] = value
        else:
            accumulated_noise_skills[key] = value
    
    return accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills




class Persona:
    
    def __init__(self, name) -> None:
        self.name = name.lower()
        self.calc_ctrl = CalcCtrl(self.name, personae_by_name, personae_by_arcana, specialCombos, arcana_rank)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, o: object) -> bool:
        return self.name == o.name

    def __hash__(self) -> int:
        return hash(self.name)
    
class Recipe:

    def __init__(self, personas,accumulated_mandatory_skills, accumulated_optional_skills,accumulated_noise_skills , previous_recipe = None) -> None:
        self.personas = personas # list of personas
        self.accumulated_mandatory_skills =  accumulated_mandatory_skills # dict of accumulated mandatory skills
        self.accumulated_optional_skills = accumulated_optional_skills # dict of accumulated optional skills
        self.accumulated_noise_skills = accumulated_noise_skills # dict of accumulated noise skills
        self.previous_recipe = previous_recipe # previous recipe
        self.next_recipes = [] # list of next recipes

    
    def __str__(self) -> str:
        return str(self.personas)


def count_true_values(dictionary):
    return list(dictionary.values()).count(True)

class BFS:

    def __init__(self,initial_persona, mandatory_skills, optional_skills ) -> None:
        self.mandatory_skills = mandatory_skills
        self.optional_skills = optional_skills
        self.initial_persona = initial_persona
        self.all_personas = {initial_persona.name : initial_persona}
        self.current_level_list_of_recipies = None
        self.first_recipie = None
    
    def get_persona_skills(self,persona,accumulated_mandatory_skills,accumulated_optional_skills, accumulated_noise_skills):
        
        persona_skills = persona_skills_dict.get(persona.name, None)
        for skill in persona_skills:
            # check if its in the keys of accumulated_mandatory_skills
            if skill in accumulated_mandatory_skills:
                # increment `accumulated_mandatory_skills[skill]``
                accumulated_mandatory_skills[skill] += 1
            # do the same for accumulated_optional_skills
            elif skill in accumulated_optional_skills:
                accumulated_optional_skills[skill] += 1
            #skill not part of mandatory or optional skills
            else:
                noise_skill_count = accumulated_noise_skills.get(skill, 0)
                accumulated_noise_skills[skill] = noise_skill_count + 1
            
        # return all dictionaries
        return accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills

    def convert_all_recepies_list_to_recipe_object_list(self,all_recepies,accumulated_mandatory_skills,accumulated_optional_skills,accumulated_noise_skills, previous_recipe = None):
        recipes = []
        for recipe in all_recepies:
            personas = []
            current_recipe_accumulated_mandatory_skills = accumulated_mandatory_skills.copy()
            current_recipe_accumulated_optional_skills = accumulated_optional_skills.copy()
            current_recipe_accumulated_noise_skills = accumulated_noise_skills.copy()
            for parent in recipe['sources']:
                name = parent.get('name', 'Unknown')
                if name not in self.all_personas:
                    persona = Persona(name)
                    self.all_personas[name] = persona
                else:
                    persona = self.all_personas[name]
                current_recipe_accumulated_mandatory_skills, current_recipe_accumulated_optional_skills , current_recipe_accumulated_noise_skills = self.get_persona_skills(persona,current_recipe_accumulated_mandatory_skills,current_recipe_accumulated_optional_skills, current_recipe_accumulated_noise_skills)

                personas.append(persona)

            recipes.append(Recipe(personas, current_recipe_accumulated_mandatory_skills, current_recipe_accumulated_optional_skills,current_recipe_accumulated_noise_skills, previous_recipe = previous_recipe))
        return recipes
    
    def compare_dictionary_of_skills(self, previous_accumulated_mandatory_skills,previous_accumulated_optional_skills, previous_accumulated_noise_skills,
                                     current_accumulated_mandatory_skills, current_accumulated_optional_skills, current_accumulated_noise_skills,
                                        best_accumulated_mandatory_skills, best_accumulated_optional_skills, best_accumulated_noise_skills):
        # get the key of 'previous_dict' that has the lowest value
        min_key = min(previous_accumulated_mandatory_skills, key=previous_accumulated_mandatory_skills.get)

        # return 'True' if 'new_dict_1_no_desired_skills' has the least ammount of unique keys than 'new_dict2_no_desired_skills'
        if current_accumulated_mandatory_skills[min_key] > best_accumulated_mandatory_skills[min_key]:
            return True
        return False
            
    
    
    def select_best_recipes(self, list_of_lists_of_recipes, previous_accumulated_mandatory_skills, previous_accumulated_optional_skills, previous_accumulated_noise_skills, next_recipes = []):
        #TODO solve the combination of recipies that maximizes the number of skills
        #TODO update acummulated_optional_skills and acummulated_mandatory_skills
        #TODO leave only recipies part of the optmiized solution

        # merge dictionaries 'accumulated_mandatory_skills' and 'accumulated_optional_skills' into one dictionary
        # Merge the dictionaries
        merged_previous_skills = {**previous_accumulated_mandatory_skills, **previous_accumulated_optional_skills, **previous_accumulated_noise_skills}

        previous_skills = merged_previous_skills

        maximal_combination = []
        for list_of_recipes in list_of_lists_of_recipes:
            maximal_combination.append(list_of_recipes[0])

        index_list_of_lists_of_recipes = 0
        for list_of_recipes in list_of_lists_of_recipes:
            for recipe in list_of_recipes:

                merged_current_skills = {**(recipe.accumulated_mandatory_skills), **(recipe.accumulated_optional_skills), **(recipe.accumulated_noise_skills)}
                merged_best_skills = {**(maximal_combination[index_list_of_lists_of_recipes].accumulated_mandatory_skills), **(maximal_combination[index_list_of_lists_of_recipes].accumulated_optional_skills), **(maximal_combination[index_list_of_lists_of_recipes].accumulated_noise_skills)}
                
                if self.compare_dictionary_of_skills(previous_accumulated_mandatory_skills,previous_accumulated_optional_skills, previous_accumulated_noise_skills,
                recipe.accumulated_mandatory_skills,recipe.accumulated_optional_skills, recipe.accumulated_noise_skills,
                maximal_combination[index_list_of_lists_of_recipes].accumulated_mandatory_skills,maximal_combination[index_list_of_lists_of_recipes].accumulated_optional_skills, maximal_combination[index_list_of_lists_of_recipes].accumulated_noise_skills):
                    maximal_combination[index_list_of_lists_of_recipes] = recipe

            
            # finalizing 'for' loop
            ## update previous skills for next list of recipe
            previous_skills = {**(maximal_combination[index_list_of_lists_of_recipes].accumulated_mandatory_skills), **(maximal_combination[index_list_of_lists_of_recipes].accumulated_optional_skills), **(maximal_combination[index_list_of_lists_of_recipes].accumulated_noise_skills)}
            
            ## updating reference for next recipes
            if maximal_combination[index_list_of_lists_of_recipes].previous_recipe is not None:
                maximal_combination[index_list_of_lists_of_recipes].previous_recipe.next_recipes.append(maximal_combination[index_list_of_lists_of_recipes])
            
            index_list_of_lists_of_recipes += 1
        
        # finalizing 'for' loop
        
        accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills = separate_keys(previous_skills)

        return maximal_combination, accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills

    
    def find_personas_with_skills(self, max_layer = 4):
        accumulated_mandatory_skills = {}
        for skill in self.mandatory_skills:
            accumulated_mandatory_skills[skill] = 0

        accumulated_optional_skills = {}
        for skill in self.optional_skills:
            accumulated_optional_skills[skill] = 0
        
        accumulated_noise_skills = {}

        self.accumulated_mandatory_skills, self.accumulated_optional_skills, self.accumulated_noise_skills = self.get_persona_skills(self.initial_persona,accumulated_mandatory_skills,accumulated_optional_skills, accumulated_noise_skills)

        initial_recipies = self.initial_persona.calc_ctrl.all_recipes

        # make a list of recipies for each recipie in initial_recipies
        initial_recipies_list = self.convert_all_recepies_list_to_recipe_object_list(initial_recipies, accumulated_mandatory_skills,accumulated_optional_skills, accumulated_noise_skills, previous_recipe = None)

        current_level_list_of_lists_of_recipies = [initial_recipies_list]
        next_level_list_of_lists_of_recipies = []

        self.current_level_list_of_recipies, self.accumulated_mandatory_skills, self.accumulated_optional_skills, self.accumulated_noise_skills  = self.select_best_recipes(current_level_list_of_lists_of_recipies, accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills, next_recipes = [])


        self.first_recipie = self.current_level_list_of_recipies[0]
        bfs_layer = 0

        while bfs_layer < max_layer: #major BFS Loop. made on a fixed number of iterations
            print('layer ', bfs_layer)        
            # loop while current_level_queue is not empty
            while self.current_level_list_of_recipies:
                current_recipe = self.current_level_list_of_recipies.pop(0)

                for current_persona in current_recipe.personas:
                    new_persona_recipes_list = []
                    current_persona_recipies = current_persona.calc_ctrl.all_recipes
                    current_persona_recipies_list = self.convert_all_recepies_list_to_recipe_object_list(current_persona_recipies,current_recipe.accumulated_mandatory_skills,current_recipe.accumulated_optional_skills, current_recipe.accumulated_noise_skills, previous_recipe=current_recipe)

                    for recipe in current_persona_recipies_list:
                        new_persona_recipes_list.append(recipe)
                    next_level_list_of_lists_of_recipies.append(new_persona_recipes_list)

            #TODO solve the combination of recipies that maximizes the number of skills
            #TODO update acummulated_optional_skills and acummulated_mandatory_skills
            #TODO leave only recipies part of the optmiized solution
            # pass all elements from next_level_queue to current_level_queue
            next_level_list_of_recipies, self.accumulated_mandatory_skills, self.accumulated_optional_skills, self.accumulated_noise_skills = self.select_best_recipes(next_level_list_of_lists_of_recipies, accumulated_mandatory_skills, accumulated_optional_skills,accumulated_noise_skills)
            

            #finalizing 'while' loop
            self.current_level_list_of_recipies = next_level_list_of_recipies
            bfs_layer += 1

        return None



# In[23]:


initial_persona = Persona('Orpheus Telos')
bfs = BFS(initial_persona, mandatory_skills, optional_skills)

bfs.find_personas_with_skills(max_layer = 4)


#  # abre persona
#  ## checa as skills que ela tem e adiciona as acumuladas daquela receita
#  ## para essa persona gere todas as receitas possiveis, mande para as receitas as skills acumuladas da receita daquela persona
#  ## para cada receita repete acima
# 
#  ## repita ate que todas as skills sejam encontradas

# In[21]:


bfs.accumulated_noise_skills


# In[41]:


import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Source

def build_graph(node, graph=None, parent=None):
    if graph is None:
        graph = nx.DiGraph()
    if parent:
        graph.add_edge(parent, node)
    for child in node.next_recipes:
        build_graph(child, graph, node)
    return graph

def visualize_tree(root, fig_size=(20, 20), dpi=300):
    graph = build_graph(root)
    plt.figure(figsize=fig_size)
    pos = nx.spring_layout(graph, k=0.5)  # Adjust the spacing between nodes with k

    # Set default color for nodes and then update the root node color
    node_colors = ['skyblue' if node != root else 'red' for node in graph.nodes()]

    # Draw the graph
    nx.draw(graph, pos, with_labels=False, node_size=5000, font_size=12, node_color=node_colors, edge_color='gray')
    #labels = {n: f"{n.attribute1}\n{n.attribute2}" for n in graph.nodes()}  # Customize as needed
    nx.draw_networkx_labels(graph, pos, None, font_size=8)

    # Save and show the graph
    plt.savefig("graph.png", format='PNG', dpi=dpi)
    plt.show()

# Example usage
# Build your tree by setting previous_recipe and next_recipes
visualize_tree(bfs.first_recipie, fig_size=(40, 40), dpi=300)


# In[28]:


import networkx as nx
import matplotlib.pyplot as plt

def build_graph(node, graph=None, parent=None, depth=0, levels=None):
    if graph is None:
        graph = nx.DiGraph()
    if levels is None:
        levels = {}
    
    # Assign the node to its level in the tree
    levels[node] = depth
    
    if parent:
        graph.add_edge(parent, node)
    for child in node.next_recipes:
        build_graph(child, graph, node, depth+1, levels)
    return graph, levels

def visualize_tree(root, fig_size=(20, 20), dpi=300):
    graph, levels = build_graph(root)
    plt.figure(figsize=fig_size)
    
    # Position nodes layer by layer
    pos = {node: (depth, -i) for i, (node, depth) in enumerate(sorted(levels.items(), key=lambda x: x[1]))}
    
    # Set colors layer by layer, root node will be red
    node_colors = ['skyblue' if node != root else 'red' for node in graph.nodes()]

    # Draw the graph
    nx.draw(graph, pos, with_labels=True, node_size=3000, font_size=12, node_color=node_colors, edge_color='gray')
    #labels = {n: f"{n.attribute1}\n{n.attribute2}" for n in graph.nodes()}  # Customize as needed
    nx.draw_networkx_labels(graph, pos, None, font_size=8)

    # Save and show the graph
    plt.savefig("/mnt/data/layered_tree_visualization.png", format='PNG', dpi=dpi)
    plt.show()

# Build your tree by setting previous_recipe and next_recipes
visualize_tree(bfs.first_recipie, fig_size=(120, 40), dpi=300)

