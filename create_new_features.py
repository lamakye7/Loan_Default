def new_features(df):
    df = df.copy()
    df['dti_ratio'] = (df['loan_amount'] / (df['monthly_income']*12))* 100
    bins = [0, 30, 50, 60, float('inf')]
    labels = ['Low Risk', 'Moderate Risk', 'High Risk', 'Very High Risk']
    df['risk_category'] = pd.cut(df['dti_ratio'], bins=bins, labels=labels, right=True)
    
    bins = [300, 579, 669, 739, 799, 850]
    labels = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
    df['credit_score_category'] = pd.cut(df['credit_score'], bins=bins, labels=labels, right=True)
    
    df['term_category'] = pd.cut(df['term'], bins=[0, 12, 36, df['term'].max()], 
                                labels=['Short', 'Medium', 'Long'], include_lowest=True)
    
    income_bins = [0, 2500, 7500, 20000, float('inf')]
    income_labels = ['Low Income Group', 'Lower-Middle Income', 'Upper-Middle Income', 'High-Income Group']
    df['income_category'] = pd.cut(df['monthly_income'], bins=income_bins, labels=income_labels, right=True)
    
    df['applicant_type'] = df['num_previous_loans'].apply(lambda x: 'First-Timer' if x == 0 else 'Existing')
    df["default_ratio"] = np.where(df["num_previous_loans"] != 0, df["default_history"] / df["num_previous_loans"], 0)
    
    
    return df