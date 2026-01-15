# Налаштування проєкту з використанням UV Package Manager

## Кроки налаштування

1. **Створіть файл `.env`**  
   Перейменуйте `.env.example` на `.env` та впишіть свої дані.

2. **Створіть віртуальне середовище**  
   ```bash
   uv venv

3. **Встановіть залежності**  
   ```bash
     uv pip install --requirements pyproject.toml
   
4. **Запустіть проєкт**  
   ```bash
     uv run main.py
