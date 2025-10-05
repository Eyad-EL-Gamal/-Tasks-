# استدعاء المكتبات
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
#قراءة الملف
data = pd.read_csv("data.csv")
data.head()
#حذف اي قيم مفقودة
data = data.dropna()
#تحويل الاعمدة الي ارقام 
categorical_columns = data.select_dtypes(include=['object']).columns
#لو الاعمدة اقل من الصفر مينفزش حاجة علشان ميحصلش خطأ
if len(categorical_columns) > 0:
   #يحذف اول عمود علشان ميبقاش في تكرار (اتفهمت من السياق) 
    data = pd.get_dummies(data, columns=categorical_columns,
     drop_first=True)
#اختيار الاعمدة + ان لم يتواجد ايا منهم يتم حذفها تلقائي
columns_needed = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 
          'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement', 
          'yr_built', 'yr_renovated', 'price']
data = data[[col for col in columns_needed if col in data.columns]]
#الرسم visualize data
plt.scatter(data['view'], data['price'])
plt.xlabel('Area (sq meters)')
plt.ylabel('Price')
plt.title('House Price vs Area')
plt.show()
#التدريب و الاختبار 
X = data.drop('price', axis=1)
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#انشاء الموديل و استخدامة في التدريب
model = LinearRegression()
model.fit(X_train, y_train)
#الاختبار
y_pred = model.predict(X_test)
#حساب الخطأ
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
#طباعةالناتج
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-Square (R²): {r2:.2f}")
#مخطط الناتج
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
#النهائي
print(format(mse, r2, r2 * 100))