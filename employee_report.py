# employee_report.py
# Author email: 24f1002401@ds.study.iitm.ac.in

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import base64

# File path
csv_file = "employee_data.csv"

# Step 1: Load or generate dataset
if not os.path.exists(csv_file):
    print("employee_data.csv not found. Generating synthetic dataset...")

    np.random.seed(42)
    n = 100
    departments = ["HR", "Finance", "Sales", "Operations", "R&D", "IT"]
    regions = ["North America", "Europe", "Asia", "Middle East"]

    data = {
        "employee_id": [f"EMP{i:03d}" for i in range(1, n+1)],
        "department": np.random.choice(departments, n),
        "region": np.random.choice(regions, n),
        "performance_score": np.round(np.random.uniform(50, 100, n), 2),
        "years_experience": np.random.randint(1, 21, n),
        "satisfaction_rating": np.round(np.random.uniform(1, 5, n), 1),
    }

    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print("✅ employee_data.csv generated with 100 employees")
else:
    df = pd.read_csv(csv_file)
    print("✅ Loaded existing employee_data.csv")

# Step 2: Frequency count for HR department
hr_count = (df['department'] == 'HR').sum()
print(f"Frequency count for HR department: {hr_count}")

# Step 3: Create histogram for department distribution
plt.figure(figsize=(6, 6))
sns.countplot(x="department", data=df, palette="Set2")
plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save plot as PNG
plot_file = "department_hist.png"
plt.savefig(plot_file)
plt.close()

# Step 4: Encode image in base64 for embedding into HTML
with open(plot_file, "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode("utf-8")

# Step 5: Write HTML report
html_str = f"""
<html>
<head><title>Employee Performance Report</title></head>
<body>
<h2>Employee Performance Report</h2>
<p><b>Email:</b> 24f1002401@ds.study.iitm.ac.in</p>
<p><b>Frequency count for HR department:</b> {hr_count}</p>
<img src="data:image/png;base64,{encoded}" width="500"/>
</body>
</html>
"""

with open("employee_report.html", "w") as f:
    f.write(html_str)

print("✅ employee_report.html generated successfully")
