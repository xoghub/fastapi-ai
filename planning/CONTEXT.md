# Context of this directory

This is planning directory for planning of the project and place to store issues.md that plan of the project.

Planning of this project is include of :
- Structure of project
- Database schema
- API endpoints
- Machine learning model
- Evaluation metrics
- Training process
- Evaluation result

[Specs](./specs) is the step to create planning using issue.md

## Naming Conventions
Always using `feature-name_issues.md` for planning. Example : `product-review-analysis_issues.md`

## Routing
| Task | Go to | Read |
|------|-------|------|
| Create Planning for create new features | ./specs | CONTEXT.md |

## Example of Issues.md Content

- Api FastApi Planning 
    - Method `POST`
    - Endpoints `/api/login`
    - Request Body
        ```json
        {
            "id" : 1,
            "name" : "john",
            "email" : "[EMAIL_ADDRESS]",
            "password" : "password"
        }
        ```
    - Request Header 
        ```json
        {
            "Content-Type": "application/json",
            "Authorization": "Bearer <token>"
        }
        ```
    - Response Body 
        ```json
        {
            "message": "Sucessfuly Login"
        }
        ```
    - Error Response Body
        ```json
        {
            "message": "Failed to Login"
        }
        ```


- Machine Learning Planning
    - Method or Architecture `Naive Bayes`
    - Reason `Easy to implement and understand, and have good performance for sentiment analyst with estimate 89% f1 accuracy based on [this_refererence_paper](./../data/references/)`
    - Data Preprocessing 
        - step 1 : lowercase and remove punctuation
        - step 2 : remove stop words
        - step 3 : tokenize
        - step 4 : lemmatization
    - Training Process
        - step 1 : split data into training data and testing data with 70:30 ration based on [this_reference_paper](./../data/references/_.pdf) it recommend this ratio for avoid overfitting.
        - step 2 : train model using training data with [this_number_eppoch] with batch size, iteration, epoch, and learning rate according [this_reference_paper](./../data/references/_.pdf) it recommend this number for training process
        - step 3 : if train result is bad, adjust parameters or how to preprocess data again and repeat step 1 and 2 until result is good
    - Evaluation Process
        - step 1 : we choose [this_metrics] because [this_reference_paper](./../data/references/_.pdf) it recommend this metrics for sentiment analyst
        - step 2 : if evaluation result is bad, back to step training process and repeat until result is good
        - step 3 : if evaluation result is good, we will save model to [this_path](../artifacts/model) with [model_name_YYYY_MM.pkl] naming convention, and proof of evaluation process result must saved in [this_path](../artifacts/evaluation)


