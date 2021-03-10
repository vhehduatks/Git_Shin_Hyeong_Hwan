import numpy as np

#생성된 플롯을 그리기 위해 필요함
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#KNN 알고리즘으로 기계학습을 시키기 위해 분류기 임포트
from sklearn.neighbors import KNeighborsClassifier


iris_dataset=load_iris()
#데이터셋 자료형의 key
print("dataset의 키",iris_dataset.keys())

#iris 데이터셋의 description
print(iris_dataset['DESCR'])

#iris 데이터셋의 타입 : <class 'sklearn.utils.Bunch'>
print(type(iris_dataset))

#iris 데이터셋의 data 타입 : <class 'numpy.ndarray'>
print(type(iris_dataset.data))

#iris 데이터셋의 형식
print(iris_dataset.data.shape)

#타겟의 이름
print(iris_dataset['target_names'])

#특징의 이름
print(iris_dataset['feature_names'])

#데이터셋의 식별 데이터
print(iris_dataset['target'])

#데이터셋의 특징 데이터
print(iris_dataset['data'][:5])

#데이터셋 분할(훈련,테스트)
x_train,x_test,y_train,y_test=train_test_split(iris_dataset.data,iris_dataset.target,random_state=0)
x_train,x_test,y_train,y_test=train_test_split(iris_dataset.data,iris_dataset.target,random_state=0)


print('x_tarin의 크기',x_train.shape)
print('y_tarin의 크기',y_train.shape)

print('x_test의 크기',x_test.shape)
print('y_test의 크기',y_test.shape)


#넘파이로 데이터의 산전도행렬 표현

#iris데이터프레임(x_train을 이용한) 만들기
# iris_df=pd.DataFrame(x_train,columns=iris_dataset.feature_names)

# pd.plotting.scatter_matrix(iris_df,c=y_train,figsize=(15,15),marker='o',hist_kwds={'bins':20},s=60,alpha=0.8,cmap=mglearn.cm3)
# plt.show()

#가장 가까운 1개의 이웃의 영향을 받아 분류하도록 함
knn=KNeighborsClassifier(n_neighbors=1)

#x데이터와 y라벨로 fit 시켜준다=학습
knn.fit(x_train,y_train)

#새로운 데이터를 예측하기
unknown_data=[[5,2.9,1,0.2]]
guesses=knn.predict(unknown_data)
print('predict:',guesses)
print('predict name:',iris_dataset['target_names'][guesses])
# print(type(iris_dataset['target_names']),iris_dataset['target_names'].shape )

#테스트 데이터의 정확도 평가하기
print('test_x accuracy :',knn.score(x_test,y_test))

#k값의 변동에 따른 모델의 정확도 시각화
k_range=range(1,101)
accuracy=list()

for k in k_range:
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    accuracy.append(knn.score(x_test,y_test))

plt.plot(k_range,accuracy)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.show()

#1