# Context of this directory

This is artifacts directory for artifacts of the project. 

Artifacts of this project is include of :
- Final of Machine learning model
- History of model version
- Explanation of why model get pick from architecture stand point and evaluation result
- Best data preprocessing for this model.
- Training code for train model
- Preprocessing code for preprocess data
- Evaluation code for evaluation model

Each sub-directory use for single purpose only that define by the name of directory it self.

## Naming Conventions
Example:
- training is contain code for training model
- preprocessing is contain code for preprocessing data `../data/raw/*.csv` and produce cleaned data that should be save in `../data/clean/` but different name with `[FILENAME]_cleaned.csv`
- evaluation is contain code for evaluation model and produce evaluation result of the model with certain metrics  
- model is contain best model that pass evaluation

## Routing
| Task | Go to | Read |
|------|-------|------|
| Create training code for [model] with [data_clean] from [data_raw] | ./training | CONTEXT.md |
| Create preprocessing code for [data_raw] and produce [data_clean] | ./preprocessing | CONTEXT.md |
| Create evaluation code for [model] with [data_clean] and produce evaluation result | ./evaluation | CONTEXT.md |
| Save best model for [model] that pass evaluation with [data_clean] and save in ./model/ with [model_name_YYYY-MM-DD.pkl] naming convention | ./model | CONTEXT.md |
| Save result of evaluation artifacts like confusion matrix, roc curve, etc. save in ./artifacts/evaluation/assets/ with [assets_YYYY-MM-DD.png] naming convention | ./artifacts/evaluation/assets/ | CONTEXT.md |