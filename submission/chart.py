import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Synthetic product performance data
np.random.seed(42)
n_products = 10
product_data = {
    'product': [f'Product {i+1}' for i in range(n_products)],
    'sales': np.random.randint(500, 5000, n_products)
}
df = pd.DataFrame(product_data)

# Styling
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Create figure (512x512 = 8 inches * 64 dpi)
plt.figure(figsize=(8, 8))

# Barplot
sns.barplot(data=df, x="product", y="sales", palette="Set2")

# Titles & labels
plt.title("Product Performance Insights\nSales by Product",
          fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Product", fontsize=14, fontweight="semibold")
plt.ylabel("Sales (Units)", fontsize=14, fontweight="semibold")
plt.xticks(rotation=30, ha="right")

# Grid & layout
plt.grid(True, axis="y", alpha=0.3)
sns.despine()
plt.tight_layout()

# Save at 512x512
plt.savefig("chart.png", dpi=64)   # no bbox_inches="tight"
plt.close()

# Double-check dimensions
img = Image.open("chart.png")
if img.size != (512, 512):
    img = img.resize((512, 512), Image.Resampling.LANCZOS)
    img.save("chart.png")

print("✅ chart.png generated successfully with size:", Image.open("chart.png").size)
