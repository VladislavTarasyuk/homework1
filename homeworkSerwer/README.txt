# ToDo Server

Функционал
Сервер поддерживает следующие операции:
- Создание задачи
curl -X POST http://localhost:8000/tasks \-H "Content-Type: application/json" \-d '{"title":"Buy a laptop","priority":"high"}'
- Получение списка всех задач
curl http://localhost:8000/tasks
- Отметка задачи как выполненной
curl -X POST http://localhost:8000/tasks/1/complete
- Сохранение задач в файл
- Восстановление задач при перезапуске сервера

Структура задачи
Каждая задача содержит поля:

- `id` — уникальный идентификатор
- `title` — название задачи
- `priority` — приоритет (`low`, `normal`, `high`)
- `isDone` — статус выполнения (`true / false`)