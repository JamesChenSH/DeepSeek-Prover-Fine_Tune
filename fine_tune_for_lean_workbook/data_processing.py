import pandas as pd
import transformers


def preprocess_data(ds_path):
    data = pd.read_parquet(ds_path)
    valid_data = data[data['state_after'] == 'no goals']

    solved_problems = valid_data[['id', 'formal_statement', 'natural_language_statement', 'state_before']]

    solved_problems['header'] = 'import Mathlib\n\n'
    solved_problems = solved_problems.rename(columns={'id': 'name', 'state_before' : 'goal', 'natural_language_statement': 'informal_prefix'})
    print(solved_problems)

    return solved_problems



if __name__ == '__main__':
    
    solved_problems = preprocess_data('Lean_Workbook.parquet')
    print(solved_problems.size)
    # Save Data
    solved_problems.to_json('solved_problems.jsonl', orient='records', lines=True, force_ascii=False)