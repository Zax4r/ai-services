### **Практическое задание**

**Задача:**
Разверните LLM на вашем компьютере (например, Ollama). Создайте скрипт на Python, который будет взаимодействовать LLM API. Скрипт должен принимать неструктурированный текстовый ввод (например, необработанное электронное письмо или log-файл) и извлекать определенные поля в чистый формат JSON.

**Требования:**

- **Промты:** Реализуйте **Few-Shot Prompting**, чтобы научить модель точной требуемой структуре JSON.
- **Подсчет токенов:** Перед отправкой запроса используйте `tiktoken` (или аналогичную библиотеку) для подсчета количества токенов на входе.
- **Защита от превышения бюджета:** Реализуйте логическую проверку: если входной текст превышает определенный лимит токенов (например, 500 токенов), скрипт должен автоматически обрезать или суммировать входные данные *перед* отправкой модели для экономии средств.
- **Логирование:** Записывайте статистику использования (prompt_tokens, completion_tokens), возвращаемую API для каждого вызова.

**Критерии успеха:** Скрипт обрабатывает 10 входных данных, корректно форматирует их в формате JSON и никогда не превышает заданный лимит токенов на один вызов.

### Результат:

```bash
2026-09-29 13:57:19.459 | INFO     | app.file_processer:process_dir:15 - Processing file files/mail2.txt
2026-09-29 13:57:32.852 | INFO     | app.ollama_client:chat:40 - Successful response: prompt_tokens=540 completion_tokens=73
{
  "sender": "Robert Johnson",
  "email": "robert.johnson@example.com",
  "subject": "Payment charged twice for the same order",
  "date": "2026-09-29",
  "order_number": "67890",
  "problem": "Двойная задержка платежа"
}
2026-09-29 13:57:32.852 | INFO     | app.file_processer:process_dir:15 - Processing file files/mail1.txt
2026-09-29 13:57:50.180 | INFO     | app.ollama_client:chat:40 - Successful response: prompt_tokens=584 completion_tokens=94
{
  "sender": "Елена Морозова",
  "email": "elena.morozova@example.com",
  "subject": "Поврежденный товар в заказе",
  "date": "2026-09-28",
  "order_number": "54321",
  "problem": "Клиент обнаружил царапины и трещину на товаре, а также повреждение упаковки"
}
2026-09-29 13:57:50.180 | INFO     | app.file_processer:process_dir:15 - Processing file files/mail4.txt
2026-09-29 13:57:50.182 | ERROR    | app.ollama_client:_check_tokens:54 - MAX_INPUT_TOKENS limit was exceeded: MAX1000 CURR:3981
2026-09-29 13:57:50.183 | WARNING  | app.ollama_client:_truncate_prompt:59 - Text was truncated:MAX=1000 CURR=3981
2026-09-29 13:58:15.754 | INFO     | app.ollama_client:chat:40 - Successful response: prompt_tokens=779 completion_tokens=108
{
  "sender": "Александр Петров",
  "email": "alex.petrov@example.com",
  "subject": "Проблема с заказом, доставкой, оплатой и качеством полученного товара",
  "date": "2026-09-29",
  "order_number": "784512",
  "problem": "Клиент жалуется на проблемы с заказом, доставкой, оплатой и качеством товара"
}
2026-09-29 13:58:15.754 | INFO     | app.file_processer:process_dir:15 - Processing file files/mail3.txt
2026-09-29 13:58:32.580 | INFO     | app.ollama_client:chat:40 - Successful response: prompt_tokens=597 completion_tokens=79
{
  "sender": "Дмитрий Волков",
  "email": "dmitry.volkov@example.com",
  "subject": "Заказ не доставлен в указанный срок",
  "date": "2026-09-29",
  "order_number": "13579",
  "problem": "Заказ не доставлен вовремя"
}
```
