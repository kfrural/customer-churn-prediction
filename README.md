# Customer Churn Prediction

This project aims to predict customer churn for a telecom company using machine learning techniques. By leveraging two methodologies, **CRISP-DM** and **KDD**, we ensure a structured and insightful approach to the data mining process. The project includes data preprocessing, feature engineering, modeling, and evaluation phases, and is supported by a deployable dashboard for presenting the results.

## Project Overview

- **Objective**: Predict whether a customer will churn (leave the company) based on historical customer data.
- **Dataset**: Telecom customer churn data containing demographic information, customer behavior, and churn status.
- **Methodologies**:
  - **CRISP-DM**: Cross Industry Standard Process for Data Mining.
  - **KDD**: Knowledge Discovery in Databases.

## Directory Structure

```plaintext
/customer-churn-prediction
│
├── /data
│   ├── telecom_churn_data.csv           # Dataset for customer churn
│
├── /notebooks
│   ├── 01_data_understanding.ipynb      # Data exploration and understanding
│   ├── 02_data_preprocessing.ipynb      # Data cleaning and preprocessing
│   ├── 03_feature_engineering.ipynb     # Feature selection and engineering
│   ├── 04_modeling.ipynb                # Model training and tuning
│   ├── 05_evaluation.ipynb              # Model evaluation and validation
│
├── /src
│   ├── data_preprocessing.py            # Data preprocessing script
│   ├── feature_engineering.py           # Feature engineering script
│   ├── modeling.py                      # Modeling script
│   ├── evaluation.py                    # Model evaluation script
│
├── /dashboard
│   ├── app.py                           # Dashboard for result visualization
│
├── /docs
│   ├── CRISP_DM_overview.md             # Overview of CRISP-DM methodology
│   ├── KDD_overview.md                  # Overview of KDD methodology
│   ├── Project_Plan.md                  # Project plan and methodology documentation
│
├── README.md                            # Project overview and instructions
├── requirements.txt                     # List of Python dependencies
└── LICENSE                              # License for the project
```

## Workflow

### 1. **Data Understanding**
The initial phase involves exploring the data to understand key attributes and relationships. The dataset includes features such as:

- **Customer Demographics**: Gender, SeniorCitizen, tenure.
- **Service Information**: MonthlyCharges, total service usage.
- **Churn Status**: Whether the customer left the company or not.

Exploration results are documented in `01_data_understanding.ipynb`.

### 2. **Data Preprocessing**
Cleaning and preparing the data for modeling. This includes:

- Handling missing values.
- Encoding categorical variables.
- Normalizing or scaling numeric data.
  
Details in `02_data_preprocessing.ipynb` and `data_preprocessing.py`.

### 3. **Feature Engineering**
New features are derived to improve model performance:

- Interaction features (e.g., tenure * monthly charges).
- Aggregations or groupings based on customer type.

More details in `03_feature_engineering.ipynb` and `feature_engineering.py`.

### 4. **Modeling**
Several machine learning models are tested, including:

- Logistic Regression
- Random Forest
- XGBoost

Model training, cross-validation, and hyperparameter tuning are performed to identify the best model.

Check `04_modeling.ipynb` and `modeling.py` for implementation.

### 5. **Evaluation**
The best-performing models are evaluated using:

- Accuracy, Precision, Recall, and F1-Score.
- Confusion Matrix.
- ROC and AUC metrics.

Results are recorded in `05_evaluation.ipynb` and `evaluation.py`.

### 6. **Dashboard**
A simple interactive dashboard is developed using `Plotly Dash` to visualize the model's performance, important features, and predictions.

Check the `dashboard/app.py` for the dashboard setup.

## Technologies Used

- **Python**: Core programming language.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning models and utilities.
- **XGBoost**: Advanced gradient boosting models.
- **Plotly Dash**: Dashboard development.
- **Jupyter Notebooks**: For interactive data exploration and model building.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/customer-churn-prediction.git
    cd customer-churn-prediction
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Download the dataset and place it in the `/data` folder (or use the example `telecom_churn_data.csv` provided).

4. Run the notebooks to explore the data and train the models:

    ```bash
    jupyter notebook
    ```

5. Run the dashboard for visualizing the results:

    ```bash
    python dashboard/app.py
    ```

## Results

- **Best Model**: XGBoost
- **Key Metrics**:
  - Accuracy: 85%
  - Precision: 82%
  - Recall: 78%
  - F1-Score: 80%
- **Feature Importance**: Tenure, Monthly Charges, Contract Type were found to be the most predictive features.

## Future Work

- Improve model interpretability using SHAP or LIME.
- Extend dashboard for real-time monitoring of churn predictions.
- Experiment with deep learning models for further improvements.

