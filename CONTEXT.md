# FAST-AI Project

## Who we are
We are software developer who want create portofolio project, with scope mixing machine learning with web developer.

## Project Goal

We want create planning issues.md for software project. The software project is fullstack web application using angular frontend and python FastAPI backend that can integrate with machine learning model that create from groudup from raw data for analyzing review of products market place using aspect-based sentiment analysis (ABSA).

## What we are doing
1. create issues.md for planning the project from the beginning until the end that detail and clear for easy understanding
2. research and find the best way to build model machine learning that use raw data for analyzing review of products market place using aspect-based sentiment analysis (ABSA)
3. review paper of sentiment analysis and aspect-based sentiment analysis that can be applied to our project from pdf or resource that given in folder "some-work/docs/"

## What good looks like
1. Always refer to CONTEXT.md for project requirements and guidelines
2. always use issue.md for planning the project from the beginning until the end
3. first issue.md must have stuctur project, naming convenstion, technology stack, feature of project, and architecture of project, big view of project
4. issue.md must have detail and explanation about project plan
5. issue.md for backend always have api endpoints, api request body and header, api responde with variation of body with good response and error response.
6. issue.md for frontend always using consistent style, color pattern and always use component.
7. issue.md for machine learning always have model architecture with reason and explanation, input data description, output data description, training data, evaluation metrics, training process, evaluation result, save model location

## What to avoid
1. Dont use issue.md as code output. issue.md is for planning only
2. Put all python code in single main.py file
3. Put all python code in single folder
4. Don't use library that is not in requirements.txt
5. Don't change the project structure
6. Not asking about any changes in project structure or library
7. Don't make any changes without my permission

## Tech Stack
- Frontend: Angular
- Backend: Python FastAPI
- Database: MySQL
- Deploy: Docker

## Workspaces
- /planning — Specs, architecture, decisions
- /app-server — Application code (FastAPI)
- /app-interface — Application code (Angular)
- /.data — Data files (CSV, JSON, models)
- /artifacts — Machine Learning models and training code

## Routing
| Task | Go to | Read | Skills |
|------|-------|------|--------|
| Spec a feature | /planning | CONTEXT.md | — |
| Write code | /app-server or /app-interface | CONTEXT.md | — |
| Create training code | /artifacts/training | CONTEXT.md | — |
| Create preprocessing code | /artifacts/preprocessing | CONTEXT.md | — |
| Create evaluation code | /artifacts/evaluation | CONTEXT.md | — |
| Best data preprocessing for this model | /artifacts/best_preprocessing | CONTEXT.md | — |

## Naming conventions
- Planning : feature_name_issues.md example : product_review_analysis_issues.md
- Model : model_architecture_version_YYYY_MM.pkl example : naive-bayes-classifier_2026_05.pkl
- ML Code Relate: training/preprocessing/evaluation/code-name.py example: training-naive-bayes-classifier_2026_05.py
- App Server : feature-name-[component].py example: product-review-analysis-service.py
- App Interface : feature-name-[component].component.ts example: product-review-analysis-button.component.ts

## Workflow
1. Review progress by read issues.md on planing `./planning/` folder
1. Read and Review of paper on paper `.data/references/` folder
2. Create issues.md for planning the project from start
3. Create model machine learning that use raw data for analyzing review of products market place using aspect-based sentiment analysis (ABSA)
4. Create API endpoints, API request body and header, API response with variation of body with good response and error response
5. Create frontend using Angular that can integrate with API endpoints
6. Create evaluation metrics, training process, evaluation result
6. Create best data preprocessing for this model