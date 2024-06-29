from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import os

notebook_path = '/home/estudo/Documents/case_equalbi/Case_equalBi.ipynb'

executor = ExecutePreprocessor(timeout=-1)  

with open(notebook_path) as f:
    nb = nbformat.read(f, as_version=4)

try:
    executor.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
except Exception as e:
    print(f'Erro ao executar o notebook: {e}')
    raise

with open(notebook_path, mode='wt') as f:
    nbformat.write(nb, f)

print('Notebook executado com sucesso!')
