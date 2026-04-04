# 个人主页（静态站点）

基于 HTML / CSS / JavaScript 的个人简历页，通过 GitHub Actions 部署到 GitHub Pages。

## 本地预览

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

浏览器打开 `http://127.0.0.1:8080`。

## 部署说明

推送至 `main` 分支后，Actions 会自动构建并发布。首次使用前请在仓库 **Settings → Pages** 中将 **Build and deployment** 的 **Source** 设为 **GitHub Actions**。

发布成功后，站点地址一般为：`https://<你的用户名>.github.io/<仓库名>/`
