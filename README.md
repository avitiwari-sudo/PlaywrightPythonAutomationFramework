# Playwright Python Automation Framework

A scalable, maintainable, and enterprise‑ready **UI Automation Framework** built using:

- **Python**
- **Playwright**
- **Pytest**
- **Allure Reporting**
- **Parallel Execution (pytest‑xdist)**
- **Retry Logic (pytest‑rerunfailures)**
- **Jenkins CI/CD**
- **GitHub Actions CI**

This framework is designed for modern web automation with clean Page Object Model (POM) structure, reusable utilities, logging, screenshots, and CI integration.

---

## 🚀 Features

- Playwright browser automation (Chromium, Firefox, WebKit)
- Page Object Model (POM)
- Pytest test runner
- Parallel execution with `pytest -n worker0number`
- Retry failed tests automatically
- Allure reporting with screenshots, logs, and steps
- Worker‑based logging (`worker0_timestamp.log`)
- Log validation script to detect hidden errors , ----- not implemented yet
- Jenkins pipeline support
- GitHub Actions workflow support
- Clean folder structure for easy maintenance

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
pip install playwright pytest pytest-html pytest-xdist python-dotenv
playwright install
pip install allure-pytest
pip install pytest-rerunfailures
pytest
pytest -n auto



