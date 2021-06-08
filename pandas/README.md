![](https://img.shields.io/badge/Python-3.9-blue)
![](https://img.shields.io/badge/pandas-1.1.5-blue)
![](https://img.shields.io/badge/NumPy-1.19.5-blue)

_________

Из этических соображений, полное условие задание здесь публиковаться не будет. Дана ссылка на документ Google Sheets, который нужно забрать API v4. Далее, в условии сдачи отчёта, указаны три канала остальное - поля метрик, которые нужно выбрать или вычислить из 4-х исходных таблиц, используя код Python. Итоговый отчёт пересогласовал на Tableau и вот что у меня получилось в итоге:

![](https://github.com/rpuropuu/educational/blob/master/pandas/images/01.jpg)

[Ссылка на интерактивный Dashboard](https://public.tableau.com/app/profile/derun.grigorii/viz/LeadDashboard_16231459932060/Dashboard1)

_(В связи с недавним обновлением Tableau, сайт может открываться не сразу.)_

Исходные названия столбцов близки к оригинальным, поэтому требуются некоторые пояснения:

  * **created_at_y** - фильтр, с возможностью регулировки с точностью до дня:

![](https://github.com/rpuropuu/educational/blob/master/pandas/images/02.jpg)

  * **dropped** - фильтр, с возможностью включения/ выключения из выборки дропнутых пользователей (True - дропнутые пользователи):

![](https://github.com/rpuropuu/educational/blob/master/pandas/images/03.jpg)

  * **old** - фильтр, с возможностью включения/ выключения из выборки старых и новых пользователей (False - новый пользователь):

![](https://github.com/rpuropuu/educational/blob/master/pandas/images/04.jpg)

  * **is_fast_buy** - отфильтровывает пользователей, у которых разница между заказом и оплатой менее недели (True - оплачено в течение недели):

![](https://github.com/rpuropuu/educational/blob/master/pandas/images/05.jpg)

  * **old** - для выведения покупок новых покупателей использован тот же фильтр old, но на другом листе, суммы выведены вместе и подписаны (False - новые покупатели):

![](https://github.com/rpuropuu/educational/blob/master/pandas/images/06.jpg)

_________

Все операции над данными делались в Google Colab, Jupyter Notebook. Итоговый файл со всеми комментариями сохранён здесь:

[Файл ipynb](https://github.com/rpuropuu/educational/blob/master/pandas/google_sheets_lead.ipynb)
_(тоже может не открыться с первого раза)_

А вот первый вариант, на который я потратил несколько дней, стараясь всё сделать одними средствами Tableau:

[Ссылка на первый вариант](https://public.tableau.com/app/profile/derun.grigorii/viz/LeadDate/Orders)
