# **Loan Default** 🚀  
This is ML approach of predicting  loan default for credit provider company in Ghana.

## **Approach**  

### 1 Business Problem Understanding
Loan default prediction using machine learning addresses the critical business problem of identifying borrowers at risk of failing to repay their loans, which can lead to significant financial losses for lending institutions. By leveraging historical data on borrower characteristics, repayment history, and loan terms, a predictive model can help lenders assess credit risk more accurately and make informed lending decisions. This approach enables businesses to minimize defaults, optimize loan approval processes, and improve overall portfolio profitability while maintaining customer satisfaction.

 ### 2 Data Preprocessing  
 In the preprocessing step, I use domain knowledge to create new features for loan default prediction by engineering columns such as the debt-to-income ratio, risk categories, and income levels based on monthly income bins. Numerical features like loan amount and credit score are imputed with median values and scaled using MinMaxScaler, while categorical features, including newly binned columns, are imputed with the most frequent value and one-hot encoded. This pipeline transforms the data into a structured format, enhancing the model's ability to identify patterns and predict defaults effectively.

### 3  Model Selection
For model selection, I focus on non-linear algorithms like decision trees, training multiple models such as Random Forest, Gradient Boosting, and XGBoost to capture complex patterns in the loan default data. After evaluating their performance using metrics recall, and F1-score, I select the best-performing model for further fine-tuning. This approach ensures the chosen model is optimized for predictive power and robustness, tailored to the non-linear relationships inherent in the dataset.

### 4 Model Explainability
For model explainability, I employ SHAP (SHapley Additive exPlanations) to interpret the impact of each feature on individual loan default predictions, providing clear insights into the model's decision-making process. Additionally, I use feature importance scores derived from the model to identify the most influential variables, such interest rate, driving the predictions. This dual approach enhances transparency, allowing stakeholders to understand and trust the model's outputs while pinpointing key factors affecting loan default risk.

### 5 Model Deployment
For model deployment, I initially utilized Flask to create a web application for real-time loan default predictions and integrated Evidently for data drift monitoring, but I had to drop Evidently due to version compatibility issues. With a tight 6-hour deadline, I streamlined the deployment by focusing solely on Flask, ensuring the preprocessing pipeline and trained model are fully operational for predictions via a user-friendly interface. This approach prioritizes delivering a functional solution quickly, allowing users to input loan data and receive default risk assessments without the added complexity of drift monitoring.

## **Usage**  
1. Clone the repository:  
   ```sh
   git clone https://github.com/lamakye7/Loan_Default.git
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   python appy.py
   ```
 
