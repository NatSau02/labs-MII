import csv
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly
import numpy as np


# data generation
class Employee:
    def __init__(self, number, name, gender, birth_year, start_work, department, post, salary, number_projects):
        self.number = number
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.start_work = start_work
        self.department = department
        self.post = post
        self.salary = salary
        self.number_projects = number_projects

    def get_str(self):
        return [self.number, self.name, self.gender, self.birth_year,
                self.start_work, self.department, self.post, self.salary, self.number_projects]


full_name = ('Сиборов У. А.', 'Мишин В. Ф.', 'Николаев Д. В.', 'Похрутин С. К.', 'Иванов Б. Д.',
             'Ермилов В. Ч.', 'Никишкин Ш. Л.', 'Емельянов Д. К.', 'Свиязов К. В.', 'Кандалинцев А. Ц.',
             'Макаров В. Р.', 'Малов У. Ш.', 'Буров Р. Д.', 'Гордеенко С. Т.', 'Митин С. Л.',
             'Ганин В. С.', 'Горинович Ц. Т.', 'Синотов У. И.', 'Кузмячук В. Н..', 'Демянчук В. Л.',
             'Гранин З. Л.', 'Бельский З. Д.', 'Плеханов З. В.', 'Желябов Х. В.', 'Богров З. Н.',
             'Семенова Е. А.', 'Коннова Г. С.', 'Койнова В. З.', 'Завьялова у. З.', 'Шевцова Г. Л.',
             'Петрова Г. В.', 'Селезнева Ш. Л.', 'Рубина К. Т.', 'Князева О. Л.', 'Стрелецкая Ж. Г.',
             'Плетнева Л. В.', 'Сибирцева Л. В.', 'Кумова Д. Г.', 'Шитова Л. А.', 'Максимова Г. З.',
             'Тульцева К. Н.', 'Зиновьева Г. В.', 'Каменева Л. В.', 'Тахтилова В. К.', 'Железнова Ш. Л.')

department = ('отделение по работе с общественностью', 'секретариат', 'техническое отделение',
              'отделение построения', 'служба упревления персоналом',
              'отдел организации труда', 'бухгалтерия', 'служба управления персоналом',
              'финансовое подразделение', 'отдел внешнеэкономических связей',
              'склады готовой продукции и материалов', 'планово-экономический отдел',
              'служба стандартизации', 'юридическая служба', 'отдел кадров',
              'служба безопасности', 'вычислительный центр')

rank = ("руководитель отдела информационной безопасности", "начинающий специалист",
        "руководитель отдела разработки ПО", "senior разработчик", "middle разработчик",
        "руководитель отдела контроля качества и процесов", "специалист", "работник",
        "руководитель отдела развития ИТ", "специалист",
        "руководитель отдела поддержки ИТ", 'отдел кадров',
        'служба безопасности', 'вычислительный центр')

gender = ('муж', 'жен')

count_str = random.randint(1000, 1200)

workers = list()

for i in range(count_str):
    number = random.randint(1, 1500)
    name = random.choice(full_name)
    gen = random.choice(gender)
    birth_year = random.randint(1970, 2000)
    start_work = random.randint(2005, 2022)
    dep = random.choice(department)
    pos = random.choice(rank)
    salar = random.randint(15000, 70000)
    number_projects = random.randint(1, 15)
    person = Employee(number, name, gen, birth_year, start_work, dep, pos, salar, number_projects)
    workers.append(person)

with open("data.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(["number", "name", "gender", "birth_year", "start_work", "department", "rank", "salary",
                          "number_projects"])
    for per in workers:
        file_writer.writerow(per.get_str())


def get_info(max_res, min_res, average, disp, std, median):
    print('Max:', max_res, '\nMin:', min_res, '\nAverage:', average,
          '\nDisp:', disp, '\nStd:', std, '\nMedian:', median)


# working with a file

with open('data.csv') as scvfile:
    tab_num = []
    year_birth = []
    salary = []

    reader = csv.reader(scvfile)
    for row in reader:
        tab_num.append(row[0])
        year_birth.append(row[3])
        salary.append(row[7])

    tab_num.pop(0)
    tab_num_int = list(map(int, tab_num))

    print('Numpy:\n')

    print('Information on the service number:\n')

    get_info(np.max(tab_num_int), np.min(tab_num_int),
             np.mean(tab_num_int), np.var(tab_num_int), np.std(tab_num_int), np.median(tab_num_int))

    print('\nInformation about the year of birth:\n')

    year_birth.pop(0)
    year_birth_int = list(map(int, year_birth))

    get_info(np.max(year_birth_int), np.min(year_birth_int),
             np.mean(year_birth_int), np.var(year_birth_int), np.std(year_birth_int), np.median(year_birth_int))

    print('\nSalary information:\n')

    salary.pop(0)
    salary_int = list(map(int, salary))

    get_info(np.max(salary_int), np.min(salary_int),
             np.mean(salary_int), np.var(salary_int), np.std(salary_int), np.median(salary_int))

# pandas

data = pd.read_csv('data.csv', delimiter=',', encoding="utf-8")
print('**************************')
print('Pandas:\n')

print('Information on the service number:\n')

data_num = data['number']

get_info(data_num.max(), data_num.min(),
         data_num.mean(), data_num.var(), data_num.std(), data_num.median())

print('\nInformation about the year of birth:\n')

data_birth = data['birth_year']

get_info(data_birth.max(), data_birth.min(),
         data_birth.mean(), data_birth.var(), data_birth.std(), data_birth.median())

print('\nSalary information:\n')

data_sal = data['salary']

get_info(data_sal.max(), data_sal.min(),
         data_sal.mean(), data_sal.var(), data_sal.std(), data_sal.median())

# plotting
plt.figure(figsize=(14, 10), dpi=80)
plt.hlines(y=data['number_projects'], xmin=0, xmax=data['salary'], alpha=0.4, linewidth=5)
plt.gca().set(ylabel='number of projects', xlabel='salary')
plt.title('dependence of the number of projects on salary')
plt.show()

graf1 = data['department'].hist()
plt.xlabel('department')
plt.ylabel('number of employees')
plt.xticks(rotation=90)
plt.title('distribution of employees by departments')
plt.show()

plt.figure(figsize=(16, 10), dpi=80)
plt.plot_date(data["start_work"], data["salary"])
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.ylabel('salary')
plt.xlabel('dates')
plt.title("salary change for the period")
plt.show()
