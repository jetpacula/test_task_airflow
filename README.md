
# task 1

реализовать 3 модуля с нэймингом {source}_api_json_to_csv где через API предполагается получать данные, преобразовать с помощью pd.json_normalize в датафреймы и сохранять  в PostgreSQL в схему *raw_data* как 3 отдельные таблицы

| Source        | Metrics                                                              | Method | Tablename     |
|---------------|-----------------------------------------------------------------------|--------|---------------|
| GoogleAds     | 1. Impressions<br>2. Clicks<br>3. Cost<br>4. Conversions<br>5. Click-through rate (CTR) | API    | google_ads    |
| YandexDirect  | 1. Цена цели<br>2. Конверсия                                        | API    | yandex_direct |
| CRM           | 1. Сделки                                                            | API (?)| crm_deals     |


настроить в tableau cloud источник PostgreSQL и соединение к БД

обернуть модули в один (если данные доступны в одно и то же время) или несколько DAG’ов 

на дашборд попадет 3 таблицы со столбцами, указанными в таблице

# task 2
1. Скачайте json для доступа к google service_account и сохраните их в директорию airflow-docker в файле service_account_creds.json.
2. Замените имя проекта test-task-project-380016 на имя вашего проекта в Google Cloud в файле basic_creds.json.
3. Запустите команду docker-compose up -d.
4. Перейдите на страницу http://127.0.0.1:8080, войдите под учетной записью testtask, пароль - testtask и включите DAG.

# task 3

https://docs.google.com/spreadsheets/d/1m8NWzdj7luDeKW11kcFUu_biS7Pr3CaHN0OZfnaHDNc/edit?usp=sharing
