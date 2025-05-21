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
data : list = ["Бег 100", "Кросс", "Отжимания", "Подтягивания", "Наклоны", "Прес", "Бег 400", "Челночный бег", "Прыжки в длинну"]
name_data = ["1 семестр","2 семестр","3 семестр","4 семестр","5 семестр","6 семестр"]

def print_data(i : int):
    data_vav = []
    for norm in name_data:
        data_vav.append(df_orders[norm][i])
    fig, ax = plt.subplots()
    if(i == 8):
        data_vav[0] = None
    ax.plot(name_data, data_vav, label = "Нормативы", marker='o', markersize=3)
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
    if(i >= 6):
        print(f"Не все данные в {data[i]} норамтиве (не сдавали). И с этим боритесь как хотите!!!")