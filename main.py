import pandas as pd
import matplotlib.pyplot as plt

# Под себя менять только следующую строку name
name = "Ханхаев Андрей"
# считывание происходит из exel файла 
# Куда сохраниться граффик
path_to_save = ""

#Сюда не лазить!!!!
#-------------------------------------------------------------------------------------------------------------------------
df_orders = pd.read_excel('Result.xlsx', index_col=0, sheet_name = name, header=0)
data = ["Бег 100", "Кросс", "Прыжки в длинну", "Отжимания", "Подтягивания", "Наклоны", "Челночный бег", "Прес"]

def print_data(i : int):
    print(i)
    data_vav = [df_orders['Осень'][i], df_orders['Весна'][i]]
    fig, ax = plt.subplots()
    ax.plot([1,2], data_vav, label = "Нормативы")
    ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
    ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
    plt.xlabel('Семестры') #Подпись для оси х
    plt.ylabel('Результат') #Подпись для оси y
    plt.title(data[i]) #Название
    plt.savefig(path_to_save + name + "-" + data[i] + '.png')
    #plt.show()
    plt.close(fig)


for i in range(0,len(data)):
    print_data(i)