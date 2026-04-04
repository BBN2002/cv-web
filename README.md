# 个人主页（静态站点）

基于 HTML / CSS / JavaScript 的个人简历页。推送至 `main` 后，GitHub Actions 会将站点发布到 **`gh-pages` 分支**，由 GitHub Pages 提供访问。

**仓库：** [github.com/BBN2002/cv-web](https://github.com/BBN2002/cv-web)

**线上地址（在仓库 Settings → Pages 中启用 `gh-pages` 分支后生效）：**  
[https://bbn2002.github.io/cv-web/](https://bbn2002.github.io/cv-web/)

## 本地预览

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

浏览器打开 `http://127.0.0.1:8080`。

## 开启 GitHub Pages（仅需一次）

1. 打开 [仓库 Settings → Pages](https://github.com/BBN2002/cv-web/settings/pages)
2. **Build and deployment** → **Source** 选择 **Deploy from a branch**
3. **Branch** 选 **`gh-pages`**，文件夹选 **`/ (root)`**，保存

几分钟后即可通过上方「线上地址」访问。

## 同步更新

在仓库目录修改文件后：

```bash
cd "/Users/文件资料/个人资料/CV_web"
git add -A && git commit -m "更新内容" && git push origin main
```

Actions 会自动更新 `gh-pages` 与线上站点。
