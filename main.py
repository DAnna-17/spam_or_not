from sklearn import preprocessing
import numpy as np
import  random


def derivative(x):
    return x * (1.0 - x)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


X = []
Y = []
# читаем данные
t = 0
data = open('spambase.data', "r")
data = data.read().split('\n')[1:-1]
random.shuffle(data)
for line in data:
    curr = line.split(',')
    new_curr = []
    for item in curr[:len(curr) - 1]:
        new_curr.append(float(item))
    X.append(new_curr)
    Y.append([float(curr[-1])])
    # print(new_curr, [float(curr[-1])])

# print(len(X), len(Y))
X = np.array(X)
X = preprocessing.scale(X)
Y = np.array(Y)
# для обучения
X_train = X[0:3600]
Y_train = Y[0:3600]
# для тестирования
X_test = X[3600:]
y_test = Y[3600:]
X = X_train
y = Y_train
# 3 уровня - вход, спрятанный, выход
dim1 = len(X_train[0])
dim2 = 4
# сначала используем рандомные значения
np.random.seed(1)
n = 24
weight0 = n * np.random.random((dim1, dim2)) - n/3
weight1 = n * np.random.random((dim2, 1)) - n/3

for j in range(1000):
    layer_0 = X_train
    layer_1 = sigmoid(np.dot(layer_0, weight0))
    layer_2 = sigmoid(np.dot(layer_1, weight1))
    # считаем ошибку
    layer_2_error = Y_train - layer_2

    layer_2_delta = layer_2_error * derivative(layer_2)
    layer_1_error = layer_2_delta.dot(weight1.T)
    layer_1_delta = layer_1_error * derivative(layer_1)
    # обновляем веса
    weight1 += layer_1.T.dot(layer_2_delta)
    weight0 += layer_0.T.dot(layer_1_delta)

# print(layer_2, layer_1, layer_0)
# проверка
layer_0 = X_test
layer_1 = sigmoid(np.dot(layer_0, weight0))
layer_2 = sigmoid(np.dot(layer_1, weight1))
correct = 0
# print(layer_2, layer_1, layer_0)
# если результат больше 0.5 - спам, если меньше - нет
for i in range(len(layer_2)):
    if layer_2[i][0] > 0.5:
        layer_2[i][0] = 1
    else:
        layer_2[i][0] = 0
    if layer_2[i][0] == y_test[i][0]:
        correct += 1
    print(layer_2[i][0], y_test[i][0], layer_2[i][0] == y_test[i][0])
# вывод
for i in weight0:
    print('[', end='')
    for k in i:
        print(k, end='')
        if k != i[-1]:
            print(', ', end='')
    print('],')
print(weight1)
print('всего = ', len(layer_2))
print('верно = ', correct)
print('аккуратность = ', correct * 100.0 / len(layer_2))


X = [[0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.24, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.07, 0.0,
      0.21, 0.0, 4.21, 11, 410],
     [0,0,1.23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.61,1.85,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.61,0.61,0,0,1.23,0.61,
      0,0,0,0,0.406,0,0,0,1.666,13,70],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9.52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4.76,0,0,0,0.625,0,0,
      0,0,1.375,4,11],
     [0,0,0.65,0,0,0,0,0,0,0,0,0,0.65,0,0,0,0,0,4.6,0,0.65,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.97,0.65,0,0,
      0,0,0,0.125,0,0,1.25,5,40],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.2886002886002886, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1443001443001443, 0.0, 0.1443001443001443, 0.0,
      1.341296928327645, 1, 393],
     [0.0, 0.0, 0.050075112669003496, 0.0, 0.5508262393590386, 0.0, 0.0, 0.0, 0.0, 0.15022533800701052,
      0.10015022533800699, 0.050075112669003496, 0.0, 0.0, 0.0, 0.050075112669003496, 0.0, 0.050075112669003496,
      0.30045067601402103, 0.0, 0.10015022533800699, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1517275913870806, 0.050075112669003496, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.20030045067601399, 0.0, 0.0, 0, 0, 100],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6711409395973155, 0.0, 0.0, 0.0, 0.0,
      0.33557046979865773, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.33557046979865773, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.013422818791946, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
      0.6711409395973155, 0.0, 0.0, 0, 0, 100],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0.353,0,0,
      1.555,4,14]

]


X = np.array(X)
X = preprocessing.scale(X)
layer_1 = sigmoid(np.dot(X, weight0))
print(layer_1)
layer_2 = sigmoid(np.dot(layer_1,weight1))

for i in range(len(layer_2)):
    if layer_2[i][0] > 0.5:
        layer_2[i][0] = 1
    else:
        layer_2[i][0] = 0
    print(layer_2[i][0])

# не спам

