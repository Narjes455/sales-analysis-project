import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns

print("📊 جاري توليد وتحليل بيانات المبيعات...")

# توليد بيانات وهمية
np.random.seed(42)
products = ["قهوة مختصة", "شاي", "عصير طازج", "كرواسان", "كعكة", "ساندويتش", "لاتيه", "موكا"]
regions = ["الرياض", "جدة", "الدمام", "مكة", "المدينة", "الخبر"]

data = {
    "المنتج": np.random.choice(products, 300),
    "المنطقة": np.random.choice(regions, 300),
    "الكمية": np.random.randint(1, 15, 300),
    "سعر الوحدة": np.round(np.random.uniform(5, 45, 300), 2),
    "تاريخ": [datetime.now() - timedelta(days=np.random.randint(0, 120)) for _ in range(300)]
}

df = pd.DataFrame(data)
df["الإجمالي"] = df["الكمية"] * df["سعر الوحدة"]
df["الشهر"] = df["تاريخ"].dt.strftime("%Y-%m")

# حفظ البيانات
df.to_excel("sales_data.xlsx", index=False)
print("✅ تم حفظ بيانات المبيعات في sales_data.xlsx")

# تحليل شامل
print("\n" + "="*50)
print("📈 تقرير تحليل المبيعات")
print("="*50)

print(f"\n💰 إجمالي المبيعات: {df['الإجمالي'].sum():,.2f} ريال")
print(f"📦 إجمالي الوحدات المباعة: {df['الكمية'].sum():,}")

best_product = df.groupby('المنتج')['الإجمالي'].sum().idxmax()
best_product_value = df.groupby('المنتج')['الإجمالي'].sum().max()
print(f"\n🏆 أكثر منتج تحقيقاً للمبيعات: {best_product} ({best_product_value:,.2f} ريال)")

best_region = df.groupby('المنطقة')['الإجمالي'].sum().idxmax()
best_region_value = df.groupby('المنطقة')['الإجمالي'].sum().max()
print(f"📍 أعلى منطقة مبيعات: {best_region} ({best_region_value:,.2f} ريال)")

# رسم بياني
plt.figure(figsize=(12, 6))
sales_by_product = df.groupby('المنتج')['الإجمالي'].sum().sort_values(ascending=False)
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('المبيعات حسب المنتج', fontsize=16)
plt.xlabel('المنتج', fontsize=12)
plt.ylabel('إجمالي المبيعات (ريال)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('sales_by_product.png', dpi=100)
print("✅ تم حفظ رسم المبيعات حسب المنتج")

plt.figure(figsize=(10, 6))
sales_by_region = df.groupby('المنطقة')['الإجمالي'].sum().sort_values(ascending=False)
sales_by_region.plot(kind='bar', color='coral')
plt.title('المبيعات حسب المنطقة', fontsize=16)
plt.xlabel('المنطقة', fontsize=12)
plt.ylabel('إجمالي المبيعات (ريال)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('sales_by_region.png', dpi=100)
print("✅ تم حفظ رسم المبيعات حسب المنطقة")

print("\n" + "="*50)
print("🎯 تم إنشاء الملفات التالية:")
print("1. sales_data.xlsx - بيانات المبيعات")
print("2. sales_by_product.png - رسم بياني للمنتجات")
print("3. sales_by_region.png - رسم بياني للمناطق")
print("="*50)