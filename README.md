
Following are my projects in SQL, Python, Tableau & Excel:

You can also take a look at my Linkedin : www.linkedin.com/in/najaf-karimov-5a094a350/

📊 Visualizing the Top 5 Best-Selling Products (Python, Pandas, Matplotlib)

![2222](https://github.com/user-attachments/assets/7f8a507c-fa33-4cc9-9549-c3470d3685d4)

📌 Explanation:

groupby('product_name')['quantity'].sum() – Groups the data by product name and calculates the total quantity sold for each.

sort_values(ascending=False).head(5) – Sorts the products by quantity in descending order and selects the top 5.

barh – Creates a horizontal bar chart for better readability, especially when product names are long.

plt.text() – Displays the exact sales count next to each bar.

tight_layout() – Optimizes spacing so labels and titles fit neatly.

----------------------------------------

Distribution of Prices by Category
This boxplot visualizes the distribution of product prices across different categories. The x-axis represents various product categories (e.g., Clothing, Electronics, Food), and the y-axis shows the corresponding prices.

![2](https://github.com/user-attachments/assets/fb1ee582-2498-459f-a776-502b72edc664)

Key insights:

Electronics have the highest price range and variability compared to other categories.
Most other categories, such as Clothing, Toys, and Cosmetics, have relatively lower and more consistent price ranges.
Outliers and the interquartile range are clearly visible, helping to identify pricing trends and anomalies within each category.

Language: Azerbaijani
Plot Labels:

Title: Kateqoriyalara görə Qiymət Paylanması (Price Distribution by Category)
Y-axis: Qiymət (Price)
X-axis: Məhsul Kateqoriyası (Product Category)
--------------------------------------------------------------

Sales Volume by Product Category and Discount Level

This heatmap illustrates the number of sales across different product categories and discount levels. The x-axis represents discount rates (from 0% to 35%), and the y-axis represents product categories. The darker the cell, the higher the number of sales.


![22](https://github.com/user-attachments/assets/b3a42577-6acf-4e84-a025-3464d2247fd2)

Key insights:

Electronics, Books, and Clothing are among the top-selling categories, especially at lower discount levels.
Cosmetics and Home Accessories have lower overall sales but respond better to moderate discounts.
The sales volume generally decreases as the discount rate increases beyond a certain point.

Language: Azerbaijani

Plot Labels:

Title: Məhsul Kateqoriyası və Endirim Səviyyəsi üzrə Satış Sayı — Sales Volume by Product Category and Discount Level

X-axis: Endirim Dərəcəsi — Discount Rate

Y-axis: Məhsul Kateqoriyası — Product Category

----------------------------------------------------------------------------

Overall Sales Share by Product Category
This pie chart illustrates the proportion of total sales represented by each product category. Each slice indicates the percentage share of that category in the overall sales.
![2218](https://github.com/user-attachments/assets/ab2226ca-5434-4dc1-ace2-6b004b0b0d60)


Key insights:

Electronics is the dominant category, making up 58.3% of total sales.
Other notable categories include Books (5.9%), Kitchen (5.8%), Food (5.7%), and Sports (5.5%).
The category labeled “Other” accounts for 18.8%, covering all remaining minor categories not listed individually.

Plot Labels:

Title: Məhsul Kateqoriyalarının Ümumi Satışda Payı — Overall Sales Share by Product Category

--------------------------

📊 HR Analytics Dashboard (Built with Power BI)
This HR Analytics Dashboard was developed using Microsoft Power BI to provide a clear and interactive overview of employee attrition across multiple dimensions. It helps HR teams and decision-makers understand patterns and trends related to employee turnover, salary, satisfaction, and demographics.

![HR Dashboard](https://github.com/user-attachments/assets/677055df-f13e-4ed8-9e3d-794674967721)

🧩 Key Features:
| Metric                  | Value    |
| ----------------------- | -------- |
| 👥 Total Employees      | 1,416    |
| 🔻 Total Attrition      | 229      |
| 📉 Attrition Rate       | 16.2%    |
| 👤 Average Age          | 37 years |
| 💶 Avg Salary           | €6.5K    |
| 🕒 Avg Years at Company | 7 years  |

📈 Visuals Included:
Attrition by Education
A donut chart showing attrition based on employee education fields (Life Sciences, Medical, Marketing, etc.).

Attrition by Age Group
Bar chart that highlights the highest attrition occurs in the 26–35 age range.

Attrition by Years at Company
A line graph showing the number of employees leaving based on tenure.

Attrition by Salary Slab
Horizontal bar chart showing that the majority of attrition happens in lower salary brackets (up to €5K).

Attrition by Job Satisfaction Score
A matrix displaying attrition count per job role and satisfaction score (1 to 4), giving insight into morale and satisfaction impact.

Attrition by Gender
Simple yet clear breakdown showing the gender distribution of attrition (122 males vs. 64 females).


💼 Job Role Filters:
Users can filter the dashboard by departments like:

Human Resources

Research & Development

Sales

This enhances interactivity and lets HR professionals drill down into specific domains for deeper insights.


🛠 Built With:
Microsoft Power BI Desktop

Custom visualizations and DAX measures

Interactive filters for slicing data by job role


📂 Use Cases:
Identify high-risk groups for turnover

Understand salary and satisfaction correlations with attrition

Support data-driven HR strategy and retention programs


🧠 Insight:
Most attrition occurs in low-salary brackets, among young professionals (26–35), and within certain roles like Sales Executive and Research Scientist — suggesting that targeted retention strategies in these areas could significantly reduce overall attrition.
