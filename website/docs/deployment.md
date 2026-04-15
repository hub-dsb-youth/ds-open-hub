---
sidebar_position: 5
---

# Deployment

Trang này mô tả cách publish website Docusaurus miễn phí bằng GitHub Pages.

## Chạy local

```bash
cd website
npm install
npm start
```

## Build production

```bash
cd website
npm run build
```

## Cấu hình bắt buộc trước khi deploy

Cập nhật các giá trị sau trong file website/docusaurus.config.ts:

- organizationName: GitHub username hoặc organization
- projectName: ds-open-hub hoặc tên repo thực tế
- url: dạng https://your-github-username.github.io
- baseUrl: dạng /your-repository-name/

## Deploy bằng GitHub Actions

Workflow đã được thêm tại .github/workflows/deploy-docs.yml.

Luồng deploy:

1. Push lên nhánh main
2. Action build website ở thư mục website
3. Xuất artifact và publish lên GitHub Pages

## Triển khai app động

GitHub Pages không chạy Python backend.

Các app Streamlit nên deploy riêng, sau đó gắn link public vào mục Projects:

- Stock Screener
- Telecom Churn Predictor
