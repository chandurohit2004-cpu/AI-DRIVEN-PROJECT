# Grouping data by department and calculating averages using Spark SQL functions
dept_summary = df.groupBy("Department").agg(
    F.avg("Total_Marks").alias("Avg_Total_Marks"),
    F.avg("Attendance (%)").alias("Avg_Attendance"),
    F.avg("Backlogs").alias("Avg_Backlogs"),
    F.count("Student_ID").alias("Student_Count")
)

# Writing the final processed analytics to the "Gold Layer" Data Lake
dept_summary.write.mode("overwrite").parquet("student_analytics_gold.parquet")
# Why it's important: This shows you know how to process Big Data.
# Instead of using basic Python loops, you use Spark to aggregate the data. 
