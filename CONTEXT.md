# FAST-AI Project

## Who we are
We are software developer who want create portofolio project, with scope mixing machine learning with web developer.

## Project Goal

We want create planning feature-name_issues.md for software project. The software project is fullstack web application using angular frontend and python FastAPI backend that can integrate with machine learning model that create from groudup from raw data for analyzing review of products market place using aspect-based sentiment analysis (ABSA).

## What we are doing
1. create feature-name_issues.md for planning the project from the beginning until the end that detail and clear for easy understanding
2. research and find the best way to build model machine learning that use raw data for analyzing review of products market place using aspect-based sentiment analysis (ABSA)
3. review paper of sentiment analysis and aspect-based sentiment analysis that can be applied to our project from pdf or resource that given in folder "./data/references/"

## What good looks like
1. Always refer to CONTEXT.md for project requirements and guidelines
2. always use issue.md for planning the project from the beginning until the end
3. first issue.md must have stuctur project, naming convenstion, technology stack, feature of project, and architecture of project, big view of project
4. issue.md must have detail and explanation about project plan
5. issue.md for backend always have api endpoints, api request body and header, api responde with variation of body with good response and error response.
6. issue.md for frontend always using consistent style, color pattern and always use component.
7. issue.md for machine learning always have model architecture with reason and explanation, input data description, output data description, training data, evaluation metrics, training process, evaluation result, save model location

## What to avoid
1. Dont use feature-name_issues.md as code output. feature-name_issues.md is for planning only
2. Put all python code in single main.py file
3. Put all python code in single folder
4. Not asking about any changes on libraries dependency inside requirements.txt
5. Not asking about any changes in project structure
6. Don't make any changes without my permission

## Tech Stack
- Frontend: Angular
- Backend: Python FastAPI
- Database: MySQL
- Deploy: Docker

## Workspaces
- /planning/specs — Feature Specs, Planning, and Decisions
- /app-server — Application code (FastAPI)
- /app-interface — Application code (Angular)
- /data — Data files (CSV, JSON, models)
- /artifacts — Machine Learning models and training code

## Routing
| Task | Go to | Read | Skills |
|------|-------|------|--------|
| Create planning | /planning/specs | CONTEXT.md | — |
| Create planning feature | /planning/specs | CONTEXT.md | — |
| Create planning project | /planning/specs | CONTEXT.md | — |
| Execute planning project | *ask user or using prompt from user as reference to execute planning project* | planning/specs/feature-name_issues.md | — |
| Write code | /app-server or /app-interface | planning/specs/feature-name_issues.md | ./app-server/AGENTS.md |
| Create training code | /artifacts/training | planning/specs/feature-name_issues.md | — |
| Create preprocessing code | /artifacts/preprocessing | planning/specs/feature-name_issues.md | — |
| Create evaluation code | /artifacts/evaluation | planning/specs/feature-name_issues.md | — |
| Scrape data from website | /data/scrape | planning/specs/feature-name_issues.md | — |
| Store raw data | /data/raw | CONTEXT.md | — |
| Read reference paper | /data/references | CONTEXT.md | — |
| Store clean data | /data/clean | CONTEXT.md | — |
| Store Machine Learning Model | /artifacts/model | CONTEXT.md | — |

## Naming conventions
- Planning : feature_name_issues.md example : product_review_analysis_issues.md
- Model : model_architecture_version_YYYY_MM.pkl example : naive-bayes-classifier_2026_05.pkl
- ML Code Relate: training/preprocessing/evaluation/code-name.py example: training-naive-bayes-classifier_2026_05.py
- App Server : feature-name-[component].py example: product-review-analysis-service.py
- App Interface : feature-name-[component].component.ts example: product-review-analysis-button.component.ts

## Workflow
1. Review progress by read feature-name_issues.md on planing `./planning/specs/` folder
2. Read and Review of paper on paper `./data/references` folder
3. Create feature-name_issues.md based on feature that requested by user or from prompt (feature or prompt is from me)
4. Scraping data from website if data not exists in `./data/raw/` directory
5. Create best data preprocessing based on data that available in `./data/raw/` directory
6. Create training code that produce best model for analyzing review of products market place using aspect-based sentiment analysis (ABSA)
7. Save best model for analyzing review of products market place using aspect-based sentiment analysis (ABSA)
8. Create evaluation metrics, and evaluation result, if result is bad change parameters in training code or how to preprocess data to get better result 
9. Create API endpoints, API request body and header, API response with variation of body with good response and error response
10. Create frontend using Angular that can integrate with API endpoints
11. Create documentation of the project