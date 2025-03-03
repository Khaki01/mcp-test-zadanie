## Оглавление

- [Оглавление](#оглавление)
- [Установка](#установка)
- [Запуск](#запуск)
- [Пример результатов](#пример-результатов)
  - [Запрос](#запрос)
  - [Результат](#результат)
  - [Продолжение](#продолжение)
- [Примечания](#примечания)

## Установка

Установить [uv](https://docs.astral.sh/uv/)  
Пример для MacOs

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Установить fastmcp

```bash
uv pip install fastmcp
```

Note: on macOS, uv may need to be installed with Homebrew (`brew install uv`) in order to make it available to the Claude Desktop app.

## Запуск

Вставьте код внутри cline_settings.json в cline_mcp_settings.json  
Инструкцию по локации файла можно найти на доках Cline

```json
{
  "mcpServers": {
    "fast-demo": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "<ВАШ ПУТЬ ДО ФАЙЛА>/server.py"
      ],
      "autoApprove": ["search_files"],
      "disabled": false
    }
  }
}
```

В Cline, после настройек, добавки API KEY  
используйте как пример внизу

```xml
<use_mcp_tool>
<server_name>fast-demo</server_name>
<tool_name>search_files</tool_name>
<arguments>
{
"fragment": ".json"
}
</arguments>
</use_mcp_tool>
```

## Пример результатов

### Запрос

![Запрос](/docs/assets/pic1.png)

### Результат

![Результат](/docs/assets/pic2.png)

### Продолжение

![Продолжение](/docs/assets/pic3.png)

## Примечания

- Добавил лимит в 20 результатов
- Без лишних контейнеров и виртуализации
- Надеюсь это то что требовалось от таска, что Cline выдает просто результаты
