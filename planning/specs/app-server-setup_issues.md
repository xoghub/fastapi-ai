# App Server Setup (FastAPI)

## 1. Big View & Features
- **Goal**: Create a robust, scalable backend server using Python FastAPI to serve the Aspect-Based Sentiment Analysis (ABSA) machine learning model. This backend will process product reviews sent from the frontend and return the extracted product aspects and their associated sentiments.
- **Features**:
  - RESTful API architecture.
  - Health check endpoint to monitor API status and model availability.
  - Sentiment analysis endpoint to process individual product reviews.
  - Data validation using Pydantic to ensure reliable inputs.
  - Integration with the trained Support Vector Machine (SVM) ABSA pipeline model.

## 2. Technology Stack
- **Backend Framework**: Python FastAPI
- **Web Server**: Uvicorn
- **Data Validation & Serialization**: Pydantic
- **Machine Learning Integration**: joblib/pickle, scikit-learn, spacy
- **Containerization (Deployment)**: Docker

## 3. Project Structure
The backend code will reside in the `/app-server` directory, following a layered architecture approach.

```text
app-server/
├── main.py                             # FastAPI application instance and entry point
├── requirements.txt                    # Backend-specific dependencies
├── src/
│   ├── api/
│   │   ├── auth-router.py                    # Authentication endpoints
│   │   └── product-review-analysis-router.py # API endpoints and routing
│   ├── models/
│   │   ├── auth-schema.py                    # Pydantic models for authentication
│   │   └── product-review-analysis-schema.py # Pydantic models for request/response validation
│   ├── services/
│   │   ├── auth-service.py                   # Authentication logic
│   │   └── product-review-analysis-service.py # Business logic and ML model inference
│   └── utils/
│       └── logger.py                       # Logging utilities
```

## 4. Naming Conventions
- **Planning**: `planning/specs/feature_name_issues.md` (e.g., `app-server-setup_issues.md`)
- **App Server Python Files**: `feature-name-[component].py` (e.g., `product-review-analysis-service.py`, `product-review-analysis-router.py`)
- **Python Functions & Variables**: `snake_case` (e.g., `analyze_review`, `model_path`)
- **Python Classes (Pydantic/Services)**: `PascalCase` (e.g., `ReviewRequest`, `SentimentAnalysisService`)

## 5. Architecture of Project
1. **Client Interface**: The Angular frontend sends HTTP POST requests containing product reviews to the FastAPI Backend.
2. **Routing Layer**: The FastAPI router (`product-review-analysis-router.py`) receives the request.
3. **Validation Layer**: The payload is validated using Pydantic Schemas (`product-review-analysis-schema.py`). If invalid, a 422 Unprocessable Entity error is returned immediately.
4. **Service Layer**: The router calls the business logic service (`product-review-analysis-service.py`).
5. **Machine Learning Inference**: The service layer loads the pre-trained ML model from `/artifacts/model/` (or keeps it loaded in memory) and performs aspect-based sentiment extraction on the input text.
6. **Response Formulation**: The extracted aspects and sentiment predictions are mapped back into a Pydantic response schema and returned to the client as a JSON HTTP response.

## 6. API Endpoints

### 6.1 Health Check
- **Endpoint**: `GET /health`
- **Description**: Verifies that the API is running and accessible. Also useful for Docker health checks.
- **Headers**: None
- **Request Body**: None
- **Response (Good - 200 OK)**:
  ```json
  {
    "status": "healthy",
    "message": "FastAPI server is running."
  }
  ```

### 6.2 Analyze Product Review
- **Endpoint**: `POST /api/v1/analyze`
- **Description**: Receives a single product review text and returns the extracted aspects and sentiment polarities.
- **Headers**:
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Request Body**:
  ```json
  {
    "review_text": "The camera quality is amazing but the battery life is terrible."
  }
  ```

- **Response (Good - 200 OK)**:
  ```json
  {
    "review_text": "The camera quality is amazing but the battery life is terrible.",
    "analysis": [
      {
        "aspect": "camera quality",
        "sentiment": "Positive"
      },
      {
        "aspect": "battery life",
        "sentiment": "Negative"
      }
    ]
  }
  ```

- **Response (Error - 422 Unprocessable Entity)**:
  Returned when the request body is missing or malformed.
  ```json
  {
    "detail": [
      {
        "loc": ["body", "review_text"],
        "msg": "field required",
        "type": "value_error.missing"
      }
    ]
  }
  ```

- **Response (Error - 500 Internal Server Error)**:
  Returned when the server encounters an issue, such as failing to load the ML model or during inference.
  ```json
  {
    "detail": "Machine learning model failed to process the request. Model file not found."
  }
  ```

### 6.3 Authentication
- **Endpoint**: `POST /api/v1/auth/login`
- **Description**: Authenticates a user and returns a JWT token.
- **Headers**:
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Request Body**:
  ```json
  {
    "username": "user123",
    "password": "securepassword123"
  }
  ```
- **Response (Good - 200 OK)**:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5c...",
    "token_type": "bearer"
  }
  ```
- **Response (Error - 401 Unauthorized)**:
  ```json
  {
    "detail": "Incorrect username or password"
  }
  ```

- **Endpoint**: `POST /api/v1/auth/register`
- **Description**: Registers a new user.
- **Headers**:
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Request Body**:
  ```json
  {
    "username": "user123",
    "password": "securepassword123",
    "email": "user@example.com"
  }
  ```
- **Response (Good - 201 Created)**:
  ```json
  {
    "id": 1,
    "username": "user123",
    "email": "user@example.com"
  }
  ```
- **Response (Error - 400 Bad Request)**:
  ```json
  {
    "detail": "Username already registered"
  }
  ```

## 7. Database Schema

For the authentication feature, a `users` table is required to store credentials and user metadata safely. We will use MySQL as specified in the project CONTEXT.md.

### 7.1 `users` Table
- **id**: Primary Key, Integer, Auto-increment.
- **username**: String(255), Unique, Not Null. The chosen username for login.
- **email**: String(255), Unique, Not Null. The user's email address.
- **hashed_password**: String(255), Not Null. Bcrypt hashed version of the password.
- **is_active**: Boolean, Default `True`. Can be used to suspend or deactivate accounts.
- **created_at**: DateTime, Default `CURRENT_TIMESTAMP`. When the account was created.

*Note: Passwords must never be stored in plain text. Use `passlib` with `bcrypt` for hashing before inserting into the database.*
