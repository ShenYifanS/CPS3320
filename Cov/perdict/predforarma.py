import pandas as pd
import numpy as np
import statsmodels
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.tsa.holtwinters
#normally display the Chinese and minus signs that appear when drawing
plt.rcParams['font.sans-serif'] = ['SimHei'] #Solve the problem of Chinese display
plt.rcParams['axes.unicode_minus']=False  #Solve the problem of negative coordinate display


data = pd.read_csv(r'C:\Users\Sivan\Desktop\Cov\perdict\data.csv', index_col=('date'),encoding='unicode_escape')


data['newdiagonsis'].plot(title = 'new diagonsis', grid = True)
plt.xlabel('时间')
plt.ylabel('')
plt.show()

data['newlocaldiagonsis'].plot(title = 'new local diagonsis', grid = True)
plt.xlabel('时间')
plt.ylabel('')
plt.show()

data['Newasymptomatic'].plot(title = 'New asymptomatic', grid = True)
plt.xlabel('时间')
plt.ylabel('')
plt.show()


data['totalNumberofconfirmedcases'].plot(title = 'total Number of confirmed cases', grid = True)
plt.xlabel('时间')
plt.ylabel('')
plt.show()

data['totalNumberofcured'].plot(title = 'total Number of cured ', grid = True)
plt.xlabel('时间')
plt.ylabel('')
plt.show()

data['totalNumberofdeath'].plot(title = 'total Number of death', grid = True)
plt.xlabel('时间')
plt.ylabel('')
plt.show()

ets1 = statsmodels.tsa.holtwinters.ExponentialSmoothing(data['newdiagonsis'], trend='add', seasonal='add')
r1 = ets1.fit()

ets2 = statsmodels.tsa.holtwinters.ExponentialSmoothing(data['newlocaldiagonsis'], trend='add', seasonal='add')
r2 = ets2.fit()

ets3 = statsmodels.tsa.holtwinters.ExponentialSmoothing(data['Newasymptomatic'], trend='add', seasonal='add')
r3 = ets3.fit()

ets4 = statsmodels.tsa.holtwinters.ExponentialSmoothing(data['totalNumberofconfirmedcases'], trend='add', seasonal='add')
r4 = ets4.fit()

ets5 = statsmodels.tsa.holtwinters.ExponentialSmoothing(data['totalNumberofcured'], trend='add', seasonal='add')
r5 = ets5.fit()

ets6 = statsmodels.tsa.holtwinters.ExponentialSmoothing(data['totalNumberofdeath'], trend='add', seasonal='add')
r6 = ets6.fit()


pd.DataFrame({
    'origin': data['newdiagonsis'].values,
    'fitted': r1.fittedvalues,
}).plot(title = 'new diagonsis', grid = True,legend=True)
plt.tick_params(color='w')
plt.xticks(color='w')
plt.yticks(color='w')
plt.show()




pd.DataFrame({
    'origin': data['newlocaldiagonsis'].values,
    'fitted': r2.fittedvalues,
}).plot(title = 'new local diagonsis', grid = True,legend=True)
plt.tick_params(color='w')
plt.xticks(color='w')
plt.yticks(color='w')
plt.show()


pd.DataFrame({
    'origin': data['Newasymptomatic'].values,
    'fitted': r3.fittedvalues,
}).plot(title = 'New asymptomatic', grid = True,legend=True)
plt.tick_params(color='w')
plt.xticks(color='w')
plt.yticks(color='w')
plt.show()

pd.DataFrame({
    'origin': data['totalNumberofconfirmedcases'].values,
    'fitted': r4.fittedvalues,
}).plot(title = 'total Number of confirmed cases', grid = True,legend=True)
plt.tick_params(color='w')
plt.xticks(color='w')
plt.yticks(color='w')
plt.show()

pd.DataFrame({
    'origin': data['totalNumberofcured'].values,
    'fitted': r5.fittedvalues,
}).plot(title = 'total Number of cured ', grid = True,legend=True)
plt.tick_params(color='w')
plt.xticks(color='w')
plt.yticks(color='w')
plt.show()

pd.DataFrame({
    'origin': data['totalNumberofdeath'].values,
    'fitted': r6.fittedvalues,
}).plot(title = 'total Number of death', grid = True,legend=True)
plt.tick_params(color='w')
plt.xticks(color='w')
plt.yticks(color='w')
plt.show()

print('new diagonsis\n',r1.forecast(10))
print('new local diagonsis\n',r2.forecast(10))
print('New asymptomatic\n',r3.forecast(10))
print('total Number of confirmed cases\n',r4.forecast(10))
print('total Number of cured\n',r5.forecast(10))
print('total Number of death\n',r6.forecast(10))
