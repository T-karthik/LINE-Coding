# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

num_bits=int(input("Enter the number of bits:"))
y=[i/2 for i in range(num_bits*2)]
y=[]
manchester=[]
diff_manchester=[]
bits=[]
for i in range(num_bits):
    y.append(i)
    y.append(i+0.5)
    y.append(i+0.5)
    y.append(i+0.5)
    y.append(i+1)
print("Enter the bits:")
for i in range(num_bits):
    num=int(input())
    bits.append(num)
    if num==1:
        manchester.append(1)
        manchester.append(1)
        manchester.append(0)
        manchester.append(-1)
        manchester.append(-1)
        if len(diff_manchester)==0:
            diff_manchester.append(1)
            diff_manchester.append(1)
            diff_manchester.append(0)
            diff_manchester.append(-1)
            diff_manchester.append(-1)
        else:
            x=[diff_manchester[-4],diff_manchester[-1]]
            diff_manchester.append(x[1])
            diff_manchester.append(x[1])
            diff_manchester.append(0)
            diff_manchester.append(x[0])
            diff_manchester.append(x[0])
    elif num==0:
        manchester.append(-1)
        manchester.append(-1)
        manchester.append(0)
        manchester.append(1)
        manchester.append(1)
        if len(diff_manchester)==0:
            diff_manchester.append(-1)
            diff_manchester.append(-1)
            diff_manchester.append(0)
            diff_manchester.append(1)
            diff_manchester.append(1)
        else:
            x=[diff_manchester[-4],diff_manchester[-1]]
            diff_manchester.append(x[0])
            diff_manchester.append(x[0])
            diff_manchester.append(0)
            diff_manchester.append(x[1])
            diff_manchester.append(x[1])
plt.subplot(1, 2, 1)
plt.plot(y, diff_manchester)
plt.title("Manchester")
plt.subplot(1,2,2)
plt.plot(y,manchester)
plt.title("Differential Manchester")

plt.show()

