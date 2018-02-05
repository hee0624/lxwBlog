---
title: Learning Notes on Machine Learning
date: 2018-01-18 11:36:08
tags: [Machine Learning]
categories: [Machine Learning]
---

### 一、激活函数
1. 不用激活函数可不可以?  
 答案是不可以。**激活函数的主要作用是提供网络的非线性建模能力**。如果没有激活函数，那么该网络仅能够表达线性映射，此时**即便有再多的隐藏层，其整个网络跟单层神经网络也是等价的**。因此也可以认为，只有加入了激活函数之后，深度神经网络才具备了分层的非线性映射学习能力。
2. 激活函数应该具有什么样的性质?  
 * 可微性: 当优化方法是基于梯度的时候，这个性质是必须的
 * 单调性: 当激活函数是单调的时候，单层网络能够保证是凸函数
 * 输出值的范围: 当激活函数输出值是"有限"的时候，基于梯度的优化方法会更加稳定，因为特征的表示受有限权值的影响更显著;当激活函数的输出是"无限"的时候，模型的训练会更加高效，不过在这种情况下，一般需要更小的learning rate
3. 常见的激活函数多是分段线性和具有指数形状的非线性函数, 例如: sigmoid、tanh、ReLU(Leaky-ReLU、P-ReLU)、ELU、Maxout。各种激活函数的函数曲线以及优缺点请参见[这里][深度学习笔记(三)：激活函数和损失函数]。

### 二、损失函数 & 风险函数
参考 李航《统计学习方法》
1. **损失函数**是度量模型一次预测的好坏; **风险函数**是度量平均意义下模型预测的好坏
2. 模型的输出f(X)与真实。。。
3. 

<!-- References -->
[深度学习笔记(三)：激活函数和损失函数]: http://blog.csdn.net/u014595019/article/details/52562159

### 三、梯度下降法(Gradient Descent)
梯度下降法求代价函数(cost function)的最小值, 梯度下降法要求所有的参数必须同时更新(simultaneous update)
![gradient_descent.png](./gradient_descent.png)
![gradient_descent_property.png](./gradient_descent_property.png)

