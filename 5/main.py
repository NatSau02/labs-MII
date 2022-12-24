import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

dictABC = {'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 29,
     }

def convert_to_number(source_list):
    result =[]
    i=0
    while i<len(source_list):
        result.append(dictABC[source_list[i]])
        i+=1
    return result


def naive_bayes(X_train_n, X_test_n, y_train_n, y_test_n):
    naive_bayes_model = GaussianNB()
    naive_bayes_model.fit(X_train_n, y_train_n)
    y_pred_n = naive_bayes_model.predict(X_test_n)

    print('Показатели классификации:')
    print(classification_report(y_test_n, y_pred_n, zero_division=0))

    print('Счет X-train с Y-train: ', naive_bayes_model.score(X_train_n, y_train_n))
    print('Счет the X-test  c Y-test: ', naive_bayes_model.score(X_test_n, y_test_n))
    print('Точность наивного байесовского классификатора: ', accuracy_score(y_test_n, y_pred_n))

    point = 250

    fig, ax = plt.subplots(2, 1, figsize=(12, 12))
    ax[0].scatter(X_test[:point, 0] + X_test[:point, 1] + X_test[:point, 2] + X_test[:point, 3] +
                  X_test[:point, 4], X_test[:point, 5] + X_test[:point, 6] + X_test[:point, 7] + X_test[:point, 8] +
                  X_test[:point, 9]+X_test[:point, 10]+X_test[:point, 11]+X_test[:point, 12]+
                  X_test[:point, 13]+X_test[:point, 14]+X_test[:point, 15], c=convert_to_number(y_pred_n[:point]))
    ax[0].set_title('Наивный байесовский классификатор \n'+
                    'ПРОГНОЗ: Зависимость буквы от статических моментов и количества ребер')

    ax[1].scatter(X_test[:point, 0] + X_test[:point, 1] + X_test[:point, 2] + X_test[:point, 3] +
                  X_test[:point, 4], X_test[:point, 5] + X_test[:point, 6] + X_test[:point, 7] + X_test[:point, 8] +
                  X_test[:point, 9]+X_test[:point, 10]+X_test[:point, 11]+X_test[:point, 12]+
                  X_test[:point, 13]+X_test[:point, 14]+X_test[:point, 15], c=convert_to_number(y_test[:point]))
    ax[1].set_title('РЕЗУЛЬТАТ: Зависимость буквы от статических моментов и количества ребер')
    plt.show()

def knn(X_train_knn, X_test_knn, y_train_knn, y_test_knn):
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train_knn, y_train_knn)
    y_pred_knn = knn_model.predict(X_test_knn)
    print('Показатели классификации:')
    print(classification_report(y_test_knn, y_pred_knn, zero_division=0))

    print('Счет X-train с Y-train: ', knn_model.score(X_train_knn, y_train_knn))
    print('Счет X-test  с Y-test: ', knn_model.score(X_test_knn, y_test_knn))
    print('Точность метода ближайших соседей', accuracy_score(y_test_knn, y_pred_knn))

    point=250

    fig, ax = plt.subplots(2, 1, figsize=(12, 12))
    ax[0].scatter(X_test[:point, 0] + X_test[:point, 1] + X_test[:point, 2] + X_test[:point, 3] +
                  X_test[:point, 4], X_test[:point, 5] + X_test[:point, 6] + X_test[:point, 7] + X_test[:point, 8] +
                  X_test[:point, 9]+X_test[:point, 10]+X_test[:point, 11]+X_test[:point, 12]+
                  X_test[:point, 13]+X_test[:point, 14]+X_test[:point, 15], c=convert_to_number(y_pred_knn[:point]))
    ax[0].set_title('Метод ближайших соседей\n'+
                    'ПРОГНОЗ: Зависимость буквы от статических моментов и количества ребер')

    ax[1].scatter(X_test[:point, 0] + X_test[:point, 1] + X_test[:point, 2] + X_test[:point, 3] +
                  X_test[:point, 4], X_test[:point, 5] + X_test[:point, 6] + X_test[:point, 7] + X_test[:point, 8] +
                  X_test[:point, 9]+X_test[:point, 10]+X_test[:point, 11]+X_test[:point, 12]+
                  X_test[:point, 13]+X_test[:point, 14]+X_test[:point, 15], c=convert_to_number(y_test[:point]))
    ax[1].set_title('РЕЗУЛЬТАТ: Зависимость буквы от статических моментов и количества ребер')
    plt.show()

def svm(X_train_svm, X_test_svm, y_train_svm, y_test_svm):
    svm_model = SVC(kernel='poly', degree=10)
    svm_model.fit(X_train_svm, y_train_svm)
    y_pred_svm = svm_model.predict(X_test_svm)

    print('Показатели классификации:')
    print(classification_report(y_test_svm, y_pred_svm, zero_division=0))

    print('Счет X-train Y-train: ', svm_model.score(X_train_svm, y_train_svm))
    print('Счет X-test с Y-test: ', svm_model.score(X_test_svm, y_test_svm))
    print('Точность метода опорных векторов:', accuracy_score(y_test_svm, y_pred_svm))

    point = 250

    fig, ax = plt.subplots(2, 1, figsize=(12, 12))
    ax[0].scatter(X_test[:point, 0] + X_test[:point, 1] + X_test[:point, 2] + X_test[:point, 3] +
                  X_test[:point, 4], X_test[:point, 5] + X_test[:point, 6] + X_test[:point, 7] + X_test[:point, 8] +
                  X_test[:point, 9]+X_test[:point, 10]+X_test[:point, 11]+X_test[:point, 12]+
                  X_test[:point, 13]+X_test[:point, 14]+X_test[:point, 15], c=convert_to_number(y_pred_svm[:point]))
    ax[0].set_title('Метод опорных векторов \n'+
                    'ПРОГНОЗ: Зависимость буквы от статических моментов и количества ребер')

    ax[1].scatter(X_test[:point, 0] + X_test[:point, 1] + X_test[:point, 2] + X_test[:point, 3] +
                  X_test[:point, 4], X_test[:point, 5] + X_test[:point, 6] + X_test[:point, 7] + X_test[:point, 8] +
                  X_test[:point, 9]+X_test[:point, 10]+X_test[:point, 11]+X_test[:point, 12]+
                  X_test[:point, 13]+X_test[:point, 14]+X_test[:point, 15], c=convert_to_number(y_test[:point]))
    ax[1].set_title('РЕЗУЛЬТАТ: Зависимость буквы от статических моментов и количества ребер')
    plt.show()

dataset = pd.read_csv('letter-recognition.csv')

print('\nПервые пять строк')
print(dataset.head())


print('\nРазмерность базы данных: ', dataset.shape)

print('\nОписательная статистика')
print(dataset.describe().round(2))

print('\nПросмотр классов: ', dataset['lettr'].unique())

X = dataset.drop(columns='lettr').values
y = dataset['lettr'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print('\nРазмеры исходных массивов')
print('X train : ', X_train.shape)
print('X test  : ', X_test.shape)
print('Y train : ', y_train.shape)
print('Y test  : ', y_test.shape)

print('Наивный байесовский классификатор')
naive_bayes(X_train, X_test, y_train, y_test)

print('Метод опорных векторов')
svm(X_train, X_test, y_train, y_test)

print('Метод ближайших соседей')
knn(X_train, X_test, y_train, y_test)