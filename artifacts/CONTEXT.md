# Context of this directory

This is artifacts directory for artifacts of the project. 

Artifacts of this project is include of :
- Final of Machine learning model
- History of model version
- Explanation of why model get pick from architecture stand point and evaluation result
- Best data preprocessing for this model.

Each sub-directory use for single purpose only that define by the name of directory it self.

Example:
- training is contain code for training model
- preprocessing is contain code for preprocessing data `../data/raw/*.csv` and produce cleaned data that should be save in `../data/clean/` but different name with `[FILENAME]_cleaned.csv`
- evaluation is contain code for evaluation model and produce evaluation result of the model with certain metrics and save in `../data/metrics/`  
- model is contain best model that pass evaluation