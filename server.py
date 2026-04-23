@app.route('/api/analytics')
@login_required
def get_analytics():
    # Reading from the optimized Parquet Data Lake
    df = pd.read_parquet('student_analytics_gold.parquet')
    
    # Converting the structured data into JSON for the web dashboard charts
    dept_stats = df.set_index('Department').to_dict('index')
    
    return jsonify({
        "department_stats": dept_stats,
        "status": "Success"
    })
   # Why it's important: This shows you can bridge the gap between Big Data/ML and a user-facing application by creating RESTful APIs.
