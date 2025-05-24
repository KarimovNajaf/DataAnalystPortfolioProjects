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

----------------------------------------

Distribution of Prices by Category
This boxplot visualizes the distribution of product prices across different categories. The x-axis represents various product categories (e.g., Clothing, Electronics, Food), and the y-axis shows the corresponding prices.

![photo_2025-05-25_00-23-27](https://github.com/user-attachments/assets/ccdcfe48-5c62-4a40-96fe-5bb0237a6b06)
Key insights:

Electronics have the highest price range and variability compared to other categories.
Most other categories, such as Clothing, Toys, and Cosmetics, have relatively lower and more consistent price ranges.
Outliers and the interquartile range are clearly visible, helping to identify pricing trends and anomalies within each category.

Language: Azerbaijani
Plot Labels:

Title: Kateqoriyalara görə Qiymət Paylanması (Price Distribution by Category)
Y-axis: Qiymət (Price)
X-axis: Məhsul Kateqoriyası (Product Category)



