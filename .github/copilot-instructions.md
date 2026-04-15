# Project Guidelines

## Scope
DS Open Hub is a knowledge repository with three top-level areas:
- 1. PROJECTS: runnable analytics projects and notebooks
- 2. EBOOK: reference books and study materials
- 3. DATASET: source datasets for learning and analysis

Default behavior:
- Treat this workspace as education/research focused.
- Avoid changing files under EBOOK and DATASET unless explicitly requested.
- Prefer minimal, targeted edits and preserve existing folder naming.

## Architecture
Main development work happens in 1. PROJECTS:
- 1.3. Stock_Screener: Streamlit app with app.py and core.py
- 1.2. Telecom-Customer-Churn-Analysis: notebooks, model artifacts, and Streamlit prediction app
- 1.4. bank-churn-analysis: notebook + Power BI assets
- 1.1. Retail Customer Classification & Segmentation Analysis: notebook analysis

For project-specific details, link to existing READMEs instead of duplicating content:
- README.md (repo overview)
- 1. PROJECTS/1.3. Stock_Screener/README.md
- 1. PROJECTS/1.2. Telecom-Customer-Churn-Analysis/Telecom-Customer-Churn-Analysis/README.md
- 1. PROJECTS/1.4. bank-churn-analysis/README.md
- 1. PROJECTS/1.1. Retail Customer Classification & Segmentation Analysis/README.md

## Build and Run
No single root build/test pipeline is defined.

Use per-project commands:
- Stock Screener:
  - pip install -r 1. PROJECTS/1.3. Stock_Screener/requirements.txt
  - streamlit run 1. PROJECTS/1.3. Stock_Screener/app.py
- Telecom churn prediction app:
  - streamlit run 1. PROJECTS/1.2. Telecom-Customer-Churn-Analysis/Telecom-Customer-Churn-Analysis/predict/predict_streamlit.py

Notebook projects:
- Run with Jupyter using the notebook in each project folder.
- Keep notebook edits scoped and avoid reformatting unrelated cells.

## Conventions
- Keep comments and commit-facing text concise; bilingual context is acceptable (Vietnamese + English).
- For Python edits, prefer:
  - clear function names and type hints where practical
  - explicit exception handling over broad bare except
  - pathlib or project-relative paths instead of hardcoded absolute paths
- Do not rename top-level folders unless explicitly requested because names are used as catalog labels.

## Safe Editing Rules
- Preserve data files and model artifacts unless task explicitly requires updating them.
- When changing analysis logic, update nearby README notes if behavior/output expectations changed.
- If a project has its own requirements.txt, update that local file rather than introducing a root dependency file unless asked.
