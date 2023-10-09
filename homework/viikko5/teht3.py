import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

#------------------------------------------------------------------------------------
# lataa aineisto pandas dataframeen
df = pd.read_csv('salary.csv')
print(df)

#-------------------------------------------------------------------------------------
# tutustu dataan ja visualisoi pistepilvellä data, ja selvitä korrelaatio 
# (työkokemus, palkka) ja p-arvo sekä visualisoi vielä heatmap korrelaatioista (työkokemus, palkka)
plt.scatter(df['YearsExperience'], df['Salary'])
plt.show()

#------------------------------------------------------------------------------------
# jaa aineisto opetusdataan ja testidataan 70/30 suhteessa

# Otetaan dataframesta data
X = df.iloc[:, [0]] #YearsExperience
y = df.iloc[:, [1]] #Salary

# Jaetaan se
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#------------------------------------------------------------------------------------
# opeta lineaarinen regressio -malli
model = LinearRegression()
model.fit(X_train, y_train)

#------------------------------------------------------------------------------------
# tulosta suoran yhtälö
coef = model.coef_
inter = model.intercept_

print(f'Suoran ythälö: y = {coef} x + {inter}')

#------------------------------------------------------------------------------------
# tee ennuste testidatalla
y_pred = model.predict(X_test)

#------------------------------------------------------------------------------------
# visualisoi testiaineiston tulokset pistepilven ja suoran sovituksen avulla
plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, y_pred, color='blue')
plt.show()

#------------------------------------------------------------------------------------
# luo seabornin regplot-visualisointi ja vertaa tulosta edelliseen visualisointiin
sns.regplot(x=X_test, y=y_test)
plt.show()

#------------------------------------------------------------------------------------
# arvioi mallia käyttäen metriikoita: R2, MAE ja RMSE. 
# Mitä mallista voidaan sanoa näiden metriikoiden perusteella?
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

print(f'r2: {r2}')
print(f'mae: {mae}')
print(f'rmse: {rmse}')

#------------------------------------------------------------------------------------
# Ennusta vielä kuvitteellisen työntekijän palkka 7v kokemuksella
print(f'Uuden työntekijän palkka 7V kokemusella on: {model.predict([[7]])}')