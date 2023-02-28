#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Два економісти, ймовірність відхилення понад прогнозовану похибку - 0.1; для другого 0.2; перший поклав 40 документів, 
#другий 60. Витягли документ з суттєвою помилкую. Рахуємо вірогідність що цей док зроблений економістом №1:
P1 = 40/100
P2 = 60/100
print("Possiblity that get doc of first economist: ", P1, "Possiblity that get doc of second economist: ", P2)
# Використаємо теорему Байєса для двох випадків: 
print("Possibility_first_economist will be:   P(A1|B = (P(A1)*P(B|A1)/(P(A1)*P(B|A1)+(P(A2)*P(B|A2))")
Ps1 = 0.4*0.1/((0.4*0.1)+(0.6*0.2))
print("Still have small possiblity that first economist fill this doc: ", Ps1)


# In[32]:


#Для двох виробництв маємо дані, шукаємо ступінь ризику. Спочатку вирахуємо математичне сподівання і дисперсію, потім стаддартне
#середньоквадратичне відхилення, що вкаже на більшу ризикованість одного з підприємств:
# x 1000 1500 2000    # y 1000 1500 1750
# p 0,5   0,3  0,2    # p  0,4  0,4  0,2

Mx = 1000*0.5+1500*0.3+2000*0.2
My = 1000*0.4+1500*0.4+1750*0.2
print("Math_expect1 = ", Mx1, "Math_expect2 = ", Mx2)
Dx = ((1000**2)*0.5+(1500**2)*0.3+(2000**2)*0.2) - (1350**2)
Dy = ((1000**2)*0.4+(1500**2)*0.4+(1750**2)*0.2) - (1350**2)
print("Dispers_x is: ", Dx, "Dispers_y is: ", Dy)
Risk_x=Dx**0.5
Risk_y=Dy**0.5
print("Risk for first X way of production - ",  Risk_x, "Risk for second Y way of production - ", Risk_y)
print("Looks like X variant is with higher risk, but sometmet more risk match to more profit, so who knows...")


# In[ ]:




