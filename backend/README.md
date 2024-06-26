## Терминология
- Бизнес-логика - набор правил, практик, процессов, которые диктуются самим бизнесом, то есть заказчиком.
- DI, dependency injection - процесс внедренния зависимостей в классы-сервисы.
- Класс-сервис - класс, который реализует какую-то логику и не имеет состояния (либо слабо зависит от своего состояния).

## MVC
Бекенд построен по MVC структуре, каждый можель отвечает имеет свою зону ответственности:
- `service` - модуль бизнес-логики. Состоит из классов, которые реализуют какую-либо бизнес-логику.
- `repository` - модуль репозиториев. Состоит из классов, которые реализуют максимально простые CRUD операции с СУБД.
- `persistence` - модуль моделей СУБД. Состоит из, например, SQLAlchemy моделей.
- `supplier` - модель поставщиков. Состоит из классов, которые реализуют максимально простые операции взаимодействия с внешними системами, например, с очередями, гигачатами и тд.
- `schemas` - DTO модели.
- `presentation` - модуль презентативного слоя, то есть интерфейсов взаимодействия с данным проектов. Например, телеграм-ботов, фастапи и тд.
- `shared` - все, что нельзя классифицировать. Настройки, логгеры, утилиты.
