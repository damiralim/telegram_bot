from telebot.handler_backends import State, StatesGroup

''' Определение состояний бота '''

class UserDataState(StatesGroup):
    city_name: State = State()          # ввод названия города -> уточнение локации -> переход к запросу кол-ва отелей
    get_num_hotels: State = State()     # ввод количества отелей -> уточнение необходимости загрузки фото
    get_photo: State = State()          # 1.подтверждение загрузки фото -> переход к запросу кол-ва фото
                                        # 2.отказ от загрузки -> переход к выбору даты заезда/выезда
    get_num_photo: State = State()      # ввод количества фото -> переход к выбору даты заезда/выезда:
                                        # 1. bestdeal -> переход к запросу мин. цены бронирования
                                        # 2. lowprice, highprice -> переход к подтверждению данных
    min_price: State = State()          # ввод мин. цены бронирования -> переход к запросу макс. цены бронирования
    max_price: State = State()          # ввод макс. цены бронирования -> переход к запросу расстояния
                                        # от отеля до центра города
    distance: State = State()           # ввод расстояния от отеля до центра города -> переход к подтверждению данных
    data_check: State = State()         # 1.подтверждение введенных данных -> переход к выводу информации/
                                        # 2.возврат к началу
    result: State = State()             # вывод информации по отелям



