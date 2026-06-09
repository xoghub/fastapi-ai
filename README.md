# FAST-AI Aspect-Based Sentiment Analysis (ABSA)

A fullstack web application that uses a machine learning model to analyze marketplace product reviews. It extracts specific product aspects (e.g., *suara*, *harga*, *packing*) and determines their sentiment polarity (Positive, Neutral, Negative).

The application consists of:
1. **Frontend (`app-interface`)**: An Angular stand-alone application utilizing Signals for state management and customized styling.
2. **Backend (`app-server`)**: A Python FastAPI RESTful API that handles authentication, database connections, and integrates with the trained ML pipeline.
3. **Machine Learning Pipeline**: A lightweight aspect-extraction and sentiment-classification engine using spaCy and Support Vector Machines (SVM).

---

## Project Structure

* `/planning/specs` — Feature specifications, planning documents, and database schemas.
* `/app-server` — FastAPI backend application code.
* `/app-interface` — Angular frontend application code.
* `/data` — Raw and cleaned review datasets.
* `/artifacts` — Saved machine learning models and pipeline files.

---

## First-Time Installation & Setup

### Prerequisites
Make sure you have the following installed on your machine:
* Python 3.10 or higher
* Node.js 18 or higher
* Git

---

### 1. Backend (`app-server`) Setup

1. **Activate the Virtual Environment**:
   Open a terminal in the project root directory and run:
   * **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * **Windows (CMD)**:
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   * **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

2. **Install Python Dependencies**:
   With the virtual environment active, run this command from the project root:
   ```bash
   pip install -r requirements.txt
   ```
   *This will install all required Python libraries, including FastAPI, Uvicorn, SQLAlchemy, scikit-learn, and the spaCy English model.*

3. **Database Initialization**:
   No manual database creation is required. The server is configured to use a local SQLite database (`test.db`) by default. On startup, the server will automatically create this database file and initialize all necessary tables.

---

### 2. Frontend (`app-interface`) Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd app-interface
   ```

2. **Install Node Modules**:
   ```bash
   npm install
   ```

---

## Running the Applications

To run the applications locally, you must start both the backend and frontend development servers. This requires opening **two separate terminal windows**.

### Terminal 1: Run the Backend (`app-server`)
1. Open a terminal and ensure your virtual environment is active.
2. Navigate to the `app-server` directory:
   ```bash
   cd app-server
   ```
3. Start the FastAPI server using Uvicorn:
   ```bash
   python main.py
   ```
   *(Alternatively, you can run: `uvicorn main:app --host 127.0.0.1 --port 8000 --reload`)*
* The backend API will be available at **`http://localhost:8000`**.
* Interactive API documentation can be accessed at `http://localhost:8000/docs`.

### Terminal 2: Run the Frontend (`app-interface`)
1. Open a second terminal window.
2. Navigate to the `app-interface` directory:
   ```bash
   cd app-interface
   ```
3. Start the Angular development server:
   ```bash
   npm start
   ```
* The frontend application will be hosted at **`http://localhost:4200`**.
* Open your browser and go to `http://localhost:4200` to interact with the dashboard.

### How They Connect (API Proxy)
During development, the Angular dev server is configured to proxy all `/api` requests to `http://localhost:8000` using the `proxy.conf.json` file. This prevents Cross-Origin Resource Sharing (CORS) issues and allows seamless local integration.
