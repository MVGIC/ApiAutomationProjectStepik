## Проект API Automation Stepik

### [Курс](https://stepik.org/course/127716/syllabus)

**Шаги запуска тестов**:

1. Склонировать проект командой `git clone https://github.com/MVGIC/ApiAutomationProjectStepik.git`
2. Установить зависимости командой `pip install -r requirements.txt`
3. Запустить тесты командой `pytest -sv --alluredir=test_results tests/test_google_maps_api.py`
4. Запустить отчёт по запуску тестов командой `allure serve test_results`

**CI Status:**

[![Python application](https://github.com/MVGIC/ApiAutomationProjectStepik/actions/workflows/python-app.yml/badge.svg)](https://github.com/MVGIC/ApiAutomationProjectStepik/actions/workflows/python-app.yml)
