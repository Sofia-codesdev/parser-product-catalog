import requests  #библиотека для http-запросов

category = 'tv' #категория искомого товара
url = f'https://catalog.api.onliner.by/search/{category}' #url-адрес конкретной категории товаров

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}     #маскировка под браузер, чтобы онлайнер не заблокировал как робота

print(f"Отправляем запрос к {url}...")
response = requests.get(url, headers=headers) #через get-запрос по адресу url получаем данные в requests 

if response.status_code == 200: # если успешно
    print("Данные получены успешно!")
    
    data = response.json() # Превращаем ответ сервера (JSON) в словарь Python и сохраняем в data
    links_list = [] # создаем пустой массив, куда в дальнейшем будем записывать ссылки на найденные товары

    for product in data.get('products', []): #проходим по всем товарам из ответа сервера
        product_url = product.get('html_url') #присваиваем переменной product_url url-адреса товаров
        if product_url:                       #если такие существуют
            links_list.append(product_url)    #кладем их в links_list
            
    print(f"Найдено ссылок: {len(links_list)}")
    
    file_name = f'onliner_{category}_links.txt'  #называем файл в соотвествии с выбранной категорией товаров
    
    with open(file_name, 'w', encoding='utf-8') as file: #открываем файл file_name в режиме записи 'w'(создает файл или перезаписывает,если такой уже существует) с кодировкой utf-8
        for link in links_list:      #для всех ссылок в links_list 
            file.write(link + '\n')  #пишем каждую с новой строки
            
    print(f"Готово! Ссылки сохранены в файл: {file_name}")