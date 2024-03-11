#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:
import json
import sys

list_of_persona_inherit_types = ['ALL', 'SLASH', 'STRIKE', 'PIERCE', 'FIRE', 'ICE', 'ELECTRICITY', 'WIND', 'LIGHT', 'DARK', 'LIGHT & DARK', 'RECOVERY', 'BAD STATUS']

# Check if command line argument is provided and is a valid index
if len(sys.argv) > 1 and sys.argv[1].isdigit() and int(sys.argv[1]) < len(list_of_persona_inherit_types):
    global_persona_inherit_type = list_of_persona_inherit_types[int(sys.argv[1])]
    print(global_persona_inherit_type)
else:
    print("Please provide a valid index as a command line argument.")

# Open the file
f = open('logs_optimal_solutions/logs-{}-output.txt'.format(global_persona_inherit_type), 'w')

# Redirect stdout to the file
sys.stdout = f


personae_path = '/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/personae.json'
#personae_path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\fusion_navigator\\personae.json'
with open(personae_path, 'r') as fp:
    personae = json.load(fp)


# open json file and read contenta as a list of dictionaries
#combos2path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\fusion_navigator\\combos2.json'
combos2path = '/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/combos2.json'
with open(combos2path, 'r') as fp:
    arcana2Combos = json.load(fp)


combos3path = '/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/combos3.json'
#combos3path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\fusion_navigator\\combos3.json'
with open(combos3path, 'r') as fp:
    arcana3Combos = json.load(fp)


#specialCombos_path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\fusion_navigator\\specialCombos.json'
specialCombos_path = '/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/specialCombos.json'
with open(specialCombos_path, 'r') as fp:
    specialCombos = json.load(fp)


# In[3]:


class PersonaCompendiumExtracted:
    def __init__(self, name, level, skills):
        self.name = name
        self.level = level
        self.skills = skills

import json


#persona_compendium_save_file_path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\fusion_navigator\\persona_compendium_save_file.json'
persona_compendium_save_file_path = '/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/persona_compendium_save_file.json'
# Load the JSON file
with open(persona_compendium_save_file_path, 'r', encoding='utf-8') as f:
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

# In[5]:


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

#calc_ctrl = CalcCtrl('chi you', is_intermediate_fusion=False)
#calc_ctrl = CalcCtrl('orpheus telos', is_intermediate_fusion=True)
#print(calc_ctrl.all_recipes)


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
        print(f"Total Cost: {cost}\\n", file=file)


# In[17]:


# open dataframe located in "/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv"
import pandas as pd


#skills_csv_path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\skills_list\\skills.csv'
skills_csv_path = "/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv"
df = pd.read_csv(skills_csv_path)

#print(df)

skill_type_dict = df.set_index('skill')['type'].to_dict()

skill_rank_dict = df.set_index('skill')['rank'].to_dict()


# given a skill name return the skill type
def get_skill_type(skill_name):
    return skill_type_dict[skill_name]

def get_skill_rank(skill_name):
    return skill_rank_dict[skill_name]

#print(get_skill_type('Agidyne'))

persona_name = 'chi you'

#inheritance_csv_path ='C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\inheritance_calculator\\inheritance.csv'
inheritance_csv_path = '/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/inheritance.csv'
inheritance_df = pd.read_csv(inheritance_csv_path)

#personas_inheritance_csv_path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\inheritance_calculator\\personas_inheritance.csv'
personas_inheritance_csv_path = '/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/personas_inheritance.csv'
persona_inheritance_df = pd.read_csv(personas_inheritance_csv_path)

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


#print(get_inheritance_probability('Almighty', persona_inherit_type))


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


#chi_you_base = CalcCtrl(persona_name, is_intermediate_fusion=False).all_recipes



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

#best_ratio, best_recipe, best_set, best_desired_skills_prob_dict, biggest_ammount_of_inherited_skills, best_ratio_max, best_recipe_max, best_set_max, best_skills_max, best_desired_skills_prob_dict_max, running_ratio, running_recipe, running_set = get_best_recipe(desired_skills=desired_skills, recipes_list=chi_you_base)


# In[2]:


import pandas as pd

#personas_inheritance_csv_path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\inheritance_calculator\\personas_inheritance.csv'
personas_inheritance_csv_path = '/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/personas_inheritance.csv'
persona_inheritance_df = pd.read_csv(personas_inheritance_csv_path)

# Convert the dataframe to a dictionary
persona_inheritance_dict = persona_inheritance_df.set_index('Persona')['Type'].to_dict()

def get_persona_inheritance_type(persona_name):
    # Use the dictionary for fast lookups
    return persona_inheritance_dict.get(persona_name)

# Example usage
#persona_inheritance_type = get_persona_inheritance_type("chi you")


# In[3]:


# open json file into a dictionary

#skills_csv_path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\skills_list\\skills.csv'
skills_csv_path = "/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv"
df = pd.read_csv(skills_csv_path)

#print(df)

skill_type_dict = df.set_index('skill')['type'].to_dict()

skill_rank_dict = df.set_index('skill')['rank'].to_dict()

# get all unique skill types and all unique ranks
unique_skill_types = set(skill_type_dict.values())
unique_skill_ranks = set(skill_rank_dict.values())

missing = 0
pair_exist = []
pair_dont_exist = []
for st in unique_skill_types:
    for sr in unique_skill_ranks:
        if sr == 99:
            continue
        # veriy if there is not an entry in the df with that skill type and rank
        if len(df.loc[(df['type'] == st) & (df['rank'] == sr)]) == 0:
            #print(f"Missing skill: {st} - {sr}")
            missing+=1
            pair_dont_exist.append((st,sr))
        else:
            pair_exist.append((st,sr))

print('missing pairs: ', pair_dont_exist)
print('missing pairs ammount: ', missing)

def load_empty_total_dict():
    #combinations_json_path= 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\inheritance_calculator\\combinations.json'
    combinations_json_path = '/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/combinations.json'
    with open(combinations_json_path, 'r') as fp:
        total_combinations_dict = json.load(fp)

    inheritance_df = pd.read_csv('/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/inheritance.csv')

    # Convert the DataFrame to a dictionary where each key is an inheritance type
    # and its value is another dictionary of skill types and their probabilities.
    inheritance_dict = inheritance_df.set_index('Inheritance Type').T.to_dict('dict')

    total_combinations_dict_new = {}

    # for each key in the dictionary convert the tuple string in a tuple
    for key in total_combinations_dict:
        eval_key = eval(key)
        inherit_type , skill_rank, skill_type = eval_key

        if inherit_type != global_persona_inherit_type:
            continue

        pair = (skill_type,skill_rank)

        # if the value is equal to zero in inheritance_dict
        current_ratio = inheritance_dict[inherit_type][skill_type]

        if current_ratio == 0:
            total_combinations_dict_new[eval_key] = 1

        elif pair in pair_dont_exist:
            total_combinations_dict_new[eval_key] = 1
        else:
            total_combinations_dict_new[eval_key] = 0


    total_dict = total_combinations_dict_new

    return total_dict


# In[4]:


import ast

import pandas as pd
# Load the CSV file into a DataFrame
#inheritable_skills_csv_path = 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\skills_list\\inheritable_skills_with_levels.csv'
inheritable_skills_csv_path = '/home/eduardo/Documents/Persona3/AutoTelos/skills_list/inheritable_skills_with_levels.csv'
df = pd.read_csv(inheritable_skills_csv_path)

#print all lines of the dataframe
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    None
    #print(df)

class UnlockableSkill:
    def __init__(self, name, level=None):
        self.name = name
        self.level = level

    def __repr__(self):
        if self.level:
            return f"('{self.name}', lv{self.level})"
        else:
            return f"('{self.name}')"


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

def ammount_of_base_skills(persona_name):
    persona_skills = skill_dict[persona_name]
    base_skills = [skill for skill in persona_skills if skill.level is None]
    return len(base_skills)

def get_base_skills(persona_name):
    persona_skills = skill_dict[persona_name]
    base_skills = [skill.name for skill in persona_skills if skill.level is None]
    return base_skills

#print(ammount_of_base_skills('chi you'))


# In[5]:


from itertools import product
from tqdm import tqdm
from bitarray import bitarray


class Persona:
    def __init__(self, data):
        self.name = data.get('name', 'Unknown')
        self.level = data.get('level', 0)
        self.arcana = data.get('arcana', 'Unknown')
        self.special = data.get('special', False)
        self.base_level = data.get('base_level', 0)
        self.base_level_plus_5 = data.get('base_level+5', self.base_level + 5)
        self.skills = data.get('skills', [])
        self.all_recipes = CalcCtrl(self.name, is_intermediate_fusion=False).all_recipes
        self.ammount_of_base_skills = ammount_of_base_skills(self.name)

    def __str__(self):
        return (f"Name: {self.name}\\n"
                f"Level: {self.level}\\n"
                f"Arcana: {self.arcana}\\n"
                f"Special: {self.special}\\n"
                f"Base Level: {self.base_level}\\n"
                f"Base Level + 5: {self.base_level_plus_5}\\n"
                f"Skills: {', '.join(self.skills)}\\n"
                f"Ammount of Base Skills: {self.ammount_of_base_skills}\\n")

    def __lt__(self, other):
        return self.name < other.name

all_personas = {}

# beging search

def are_all_values_true(dictionary):
    return all(dictionary.values())

minimal_ammout_of_recipes = 0


total_dict = load_empty_total_dict()
# Sort and enumerate keys of the initial coverage_dict
sorted_keys = sorted(total_dict.keys())
key_index_map = {key: index for index, key in enumerate(sorted_keys)}


class Recipe():
    def __init__(self, personas,amount_of_inherited_skills, skills_set, resulting_persona_name, coverage_dict):
        self.personas = personas
        self.skills_set = skills_set
        self.resulting_persona_name = resulting_persona_name
        self.amount_of_base_skills = ammount_of_base_skills(resulting_persona_name)  # Assuming this is defined elsewhere
        self.amount_of_inherited_skills = amount_of_inherited_skills  # Assuming this is defined elsewhere

        # Create a bitarray for the values
        self.coverage_bits = bitarray(len(sorted_keys))
        for key, value in coverage_dict.items():
            self.coverage_bits[key_index_map[key]] = value

        # empty the variable to free memory
        coverage_dict = None
    
    def __lt__(self, other):
        return self.personas < other.personas

    @property
    def coverage_dict(self):
        # Reconstruct the dictionary from the bitarray
        return {key: self.coverage_bits[index] for key, index in key_index_map.items()}

    def __str__(self):
        # count ammount of true values in the dictionary
        count = sum(self.coverage_dict.values())

        persona_names = [persona.name for persona in self.personas]

        return (f"Personas: {persona_names}\\n"
                f"Skills: {self.skills_set}\\n"
                f"Resulting Persona: {self.resulting_persona_name}\\n"
                f"Coverage: {self.coverage_dict}\\n"
                f"Coverage Ammount: {count}\\n"
                f"Base Skills Ammount: {self.ammount_of_base_skills}\\n"
                f"Inherited Skills Ammount: {self.ammount_of_inherited_skills}\\n"
                "------------------------\\n")
    
    def __repr__(self):

        count = sum(self.coverage_dict.values())

        persona_names = [persona.name for persona in self.personas]

        return (f"Personas: {persona_names}\\n"
                f"Skills: {self.skills_set}\\n"
                f"Resulting Persona: {self.resulting_persona_name}\\n"
                f"Coverage: {self.coverage_dict}\\n"
                f"Coverage Ammount: {count}\\n"
                f"Base Skills Ammount: {self.ammount_of_base_skills}\\n"
                f"Inherited Skills Ammount: {self.ammount_of_inherited_skills}\\n"
                "------------------------\\n")


all_fucking_recipes = []

print("Creating giant list")

# giant list of recipes
for persona in tqdm(personae):
    persona_name = persona['name']

    persona_inherit_type = get_persona_inheritance_type(persona_name)

    if persona_inherit_type != global_persona_inherit_type:
        continue

    if persona_name not in all_personas:
        # Convert JSON string to dictionary
        # Create Persona object
        current_p = Persona(persona)
        all_personas[persona_name] = current_p
    else:
        current_p = all_personas[persona_name]
    
    all_recipes = current_p.all_recipes

    base_skills = get_base_skills(persona_name)

    for recipe in all_recipes:
        # make all values in the dictionary be the last iteration
        personas = []
        recipe_skills = []

        coverage_dict = total_dict.copy()

        all_skills_in_parent_personas = []

        for parent in recipe['sources']:
            name = parent.get('name', 'Unknown')
            if name not in all_personas:
                # Convert JSON string to dictionary
                # Create Persona object
                current_p = Persona(parent)
                all_personas[name] = current_p
            else:
                current_p = all_personas[name]
            personas.append(current_p)
            
            for s in current_p.skills:
                all_skills_in_parent_personas.append(s)
                if s in base_skills:
                    continue
                recipe_skills.append(s)
                skill_type = get_skill_type(s)
                skill_rank = get_skill_rank(s)
                if skill_rank == -1 or skill_rank == 99:
                    continue
                triple_rank_skilltype_inherittype = (persona_inherit_type, skill_rank, skill_type)
                coverage_dict[triple_rank_skilltype_inherittype] = True
                
        recipe_skills_set_list = list(set(recipe_skills))

        amount_of_inherited_skills = get_ammount_of_inherited_skills(all_skills_in_parent_personas)

        currect_recipe = Recipe(personas,amount_of_inherited_skills, recipe_skills_set_list,resulting_persona_name=persona_name,coverage_dict=coverage_dict)
        coverage_dict = None
        all_fucking_recipes.append(currect_recipe)
        


print(len(all_fucking_recipes))


# In[6]:


import itertools


def coverage_of_list_of_recipes(list_of_recipes):
    total_dict = load_empty_total_dict()
    #print(total_dict)

    for recipe in list_of_recipes:
        
        recipe_skills_set_list = recipe.skills_set

        persona_inherit_type = get_persona_inheritance_type(recipe.resulting_persona_name)
        
        #find all probability ratios for each skill in the recipe
        for s in recipe_skills_set_list:
            skill_type = get_skill_type(s)
            skill_rank = get_skill_rank(s)
            triple_rank_skilltype_inherittype = (persona_inherit_type, skill_rank, skill_type)
            total_dict[triple_rank_skilltype_inherittype] = True
    
            
    # count the ammount of True values in the dictionary
    count = sum(total_dict.values())
    return count

recipe = all_fucking_recipes[:1]
#print(recipe[0].coverage_dict)
#coverage_of_list_of_recipes(recipe)


# In[8]:

print("filter recipes")


def remove_duplicate_recipes(recipe_list):
    unique_recipes = {}

    for recipe in recipe_list:
        # Convert the bitarray to a string or tuple for hashability
        coverage = tuple(recipe.coverage_bits)

        if coverage in unique_recipes:
            if len(recipe.personas) < len(unique_recipes[coverage].personas):
                unique_recipes[coverage] = recipe
        else:
            unique_recipes[coverage] = recipe

    return list(unique_recipes.values())




def remove_recipes_with_zero_coverage(recipe_list):
    return [recipe for recipe in recipe_list if sum(recipe.coverage_dict.values()) > 0]

all_fucking_recipes = remove_duplicate_recipes(all_fucking_recipes)
all_fucking_recipes = remove_recipes_with_zero_coverage(all_fucking_recipes)
filtered_recipes = all_fucking_recipes
filtered_recipes.sort()
print(len(filtered_recipes))


# integer programming

# In[ ]:
print("defining constraints dictionary")

dict_constraints = {}

for i in range(len(filtered_recipes)):
    recipe = filtered_recipes[i]
    coverage_dict = recipe.coverage_dict
    if i == len(filtered_recipes)-1:
        None
        # print(len(coverage_dict.keys()))
    for key, value, in coverage_dict.items():
        if value == True:
            # add empty list if key does not exist
            if key not in dict_constraints:
                dict_constraints[key] = []
            dict_constraints[key].append(i)
            
dict_constraints_keys = list(dict_constraints.keys())
dict_constraints_keys.sort()

#if not all keys are found discover which ones and assume they are true for everyone

total_dict = load_empty_total_dict()

total_dict_keys = total_dict.keys()

print("Keys not found:")
not_found_count = 0
list_not_found = []

for total_key in total_dict_keys:
    if total_key not in dict_constraints_keys:
        print(total_key)
        list_not_found.append(total_key)
        dict_constraints[total_key] = "Full"

dict_constraints_keys = list(dict_constraints.keys())
dict_constraints_keys.sort()

print("amount not found: ", not_found_count)

# Save list_not_found to a file
with open('logs_optimal_solutions/logs-{}-keys_not_found.txt'.format(global_persona_inherit_type), 'w') as f:
    for item in list_not_found:
        f.write("%s\n" % str(item))

import numpy as np

# Assuming 'filtered_recipes' is a list and 'dict_constraints' is a dictionary
num_keys = len(dict_constraints_keys)
num_recipes = len(filtered_recipes)

from scipy.sparse import lil_matrix

# Initialize a LIL (List of Lists) sparse matrix
sparse_a = lil_matrix((num_keys, num_recipes), dtype=int)

print("creating matrix")

# Iterate over the keys and update the sparse matrix
for index, key in enumerate(dict_constraints_keys):
    coverage_index_list = dict_constraints[key]

    if coverage_index_list == "Full":
        # Update all entries in the column
        sparse_a[index, :] = 1
    else:
        # Update only the non-zero entries
        sparse_a[index, coverage_index_list] = 1

# Optionally, convert to a more efficient format like CSR (Compressed Sparse Row)
sparse_a = sparse_a.tocsr()



# In[ ]:


import numpy as np

from scipy.sparse import save_npz

# Save the sparse matrix to a file
sparse_matrix_path = "logs_optimal_solutions/logs-{}-sparse_matrix.npz".format(global_persona_inherit_type)
save_npz(sparse_matrix_path, sparse_a)
print("saved matrix")

# In[ ]:
from scipy.sparse import load_npz
print("using to solve problem")
# Load the sparse matrix from the file
sparse_a = load_npz(sparse_matrix_path)

# Convert to CSR format for efficient row slicing
sparse_a_csr = sparse_a.tocsr()

# Number of recipes (n) and tags (m)
m, n = sparse_a_csr.shape

import pulp
from tqdm import tqdm

# Create the problem variable
prob = pulp.LpProblem("Recipe_Selection", pulp.LpMinimize)

# Decision variables
x = [pulp.LpVariable(f'x{j}', cat='Binary') for j in range(n)]

# Objective function
prob += pulp.lpSum(x)

# Constraints
for i in tqdm(range(m)):  # for each tag
    row = sparse_a_csr.getrow(i).toarray().ravel()
    prob += pulp.lpSum(row[j] * x[j] for j in range(n)) >= 1, f"TagCoverage{i}"
print("solve...")
# Solve the problem
prob.solve()

# Print the results
print("Status:", pulp.LpStatus[prob.status])
print("Minimum number of recipes:", pulp.value(prob.objective))
selected_recipes = [j for j in range(n) if x[j].varValue == 1]
print("Selected recipes (indexed at j):", selected_recipes)

sys.stdout = sys.__stdout__
f.close()
