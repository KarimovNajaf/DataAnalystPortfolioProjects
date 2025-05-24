# DataAnalystPortfolioProjects
Following are my projects in SQL, Python, Tableau & Excel:

You can also take a look at my Linkedin : www.linkedin.com/in/najaf-karimov-5a094a350/

📊 Visualizing the Top 5 Best-Selling Products (Python, Pandas, Matplotlib)
![photo_2025-05-25_00-18-28](https://github.com/user-attachments/assets/f40d3e0a-d4de-4b7b-8d0f-89946598e43b)
📌 Explanation:

groupby('product_name')['quantity'].sum() – Groups the data by product name and calculates the total quantity sold for each.

sort_values(ascending=False).head(5) – Sorts the products by quantity in descending order and selects the top 5.

barh – Creates a horizontal bar chart for better readability, especially when product names are long.

plt.text() – Displays the exact sales count next to each bar.

tight_layout() – Optimizes spacing so labels and titles fit neatly.
