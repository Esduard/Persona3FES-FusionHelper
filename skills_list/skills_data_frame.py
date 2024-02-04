import pandas as pd

class SkillDataFrame():


    def __init__(self):
        # 'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\Persona3FES-FusionHelper\\skills_list\\skills.csv'
        skills_csv_path = "/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv"
        df = pd.read_csv(skills_csv_path)

        print(df)
        self.skill_type_dict = df.set_index('skill')['type'].to_dict()

        self.skill_rank_dict = df.set_index('skill')['rank'].to_dict()

    
    def get_skill_type_dict(self):
        return self.skill_type_dict

    def get_skill_rank_dict(self):
        return self.skill_rank_dict
