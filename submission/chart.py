import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# Generate synthetic data for product performance insights
n_products = 10
product_data = {
    'product': [f'Product {i+1}' for i in range(n_products)],
    'sales': np.random.randint(500, 5000, n_products),
    'satisfaction': np.random.uniform(3.0, 5.0, n_products)  # Customer rating out of 5
}

# Create DataFrame
df = pd.DataFrame(product_data)

# Set Seaborn style and context
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Set figure size for 512x512 output
plt.figure(figsize=(8, 8))

# Create a Seaborn barplot
sns.barplot(
    data=df,
    x='product',
    y='sales',
    palette='Set2'
)

# Customize the plot professionally
plt.title('Product Performance Insights\nSales by Product', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Product', fontsize=14, fontweight='semibold')
plt.ylabel('Sales (Units)', fontsize=14, fontweight='semibold')

# Rotate x-axis labels for readability
plt.xticks(rotation=30, ha='right')

# Add subtle grid and styling
plt.grid(True, axis='y', alpha=0.3)
sns.despine()

# Ensure tight layout
plt.tight_layout()

# Save chart as 512x512 (dpi=64 × 8 in = 512 px)
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

# Display summary statistics
print("Product Performance Insights")
print("=" * 50)
print(f"Total Products: {len(df)}")
print(f"Average Sales: {df['sales'].mean():.2f} units")
print(f"Average Satisfaction: {df['satisfaction'].mean():.2f}/5")
print("\nChart generated successfully with Seaborn barplot!")

plt.show()
