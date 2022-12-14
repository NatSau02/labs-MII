### Техническое задание:

Создать rest-api сервис управления группой людей на языке Golang

Предметная область: cистема управления группами людей.
Требования:
0. Уметь создавать/обновлять/удалять группы (Название). У групп могут быть дочерние группы;
- запросы:

   - POST   api/create/group

   - PATCH  api/update/group
  
   - DELETE api/delete/group

1. Уметь создавать/обновлять/удалять человека (Имя,Фамилия,Год рождения). При создании человека нужно добавить в группу. При обновлении можно менять группу;
- запросы:
   
  - POST   api/create/human

  - PATCH  api/update/human

  - DELETE api/delete/human

2. Уметь отображать список групп и количество участников в этой группе, как чисто в данной группе, так и общее количество вместе с дочерними группами;
- запросы:
   
  - GET   api/group
  - GET   api/group/all
3. Уметь отображать список людей в определённой группе только привязанных к данной и список людей со всеми дочерними группами.
- запросы:

    - GET   api/human/{:groupId}
    - GET   api/human/all/{:groupId}
  
В качестве базы данных можно использовать: MySQL, PostgreSQL

В качестве движка миграций migrate/v4

В миграциях должны добавляться  тестовые данные для демонстрации