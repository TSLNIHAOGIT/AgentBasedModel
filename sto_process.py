import numpy as np
import matplotlib.pyplot as plt
mu = 0
sigma = 0.04
np.random.seed(0)

data=[]
Xt0=0

times=range(200000)
for t in times:
    et = np.random.normal(mu, sigma)
    Xt1 = 1 * Xt0 + et
    Xt0=Xt1
    data.append(Xt0)

plt.plot(range(len(data)),data)
# plt.hist(data,25,color="g",alpha=0.37)#直方图
plt.show()