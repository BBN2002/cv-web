# 个人主页（静态站点）

基于 HTML / CSS / JavaScript 的个人简历页，通过 GitHub Actions 部署到 GitHub Pages。

## 本地预览

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

浏览器打开 `http://127.0.0.1:8080`。

## 推送到 GitHub（本机已 `git init` 并完成首次提交）

在终端执行（需已安装 `gh`，本机路径一般为 `/opt/homebrew/bin/gh`）：

```bash
cd "/Users/文件资料/个人资料/CV_web"
gh auth login
```

按提示用浏览器或 Token 登录 GitHub。登录成功后创建远程仓库并推送（仓库名可改成你喜欢的，需全小写且无空格更稳妥）：

```bash
gh repo create cv-web --public --source=. --remote=origin --push
```

若提示仓库名已存在，换一个名字，例如：`gh repo create bbn-cv --public --source=. --remote=origin --push`

**首次开启 GitHub Pages：**

1. 打开 GitHub 上该仓库页面 → **Settings** → **Pages**
2. **Build and deployment** 里把 **Source** 选成 **GitHub Actions**（不要选 Deploy from a branch）
3. 回到 **Actions** 等 workflow 跑绿；再刷新 **Settings → Pages**，会显示站点地址

发布成功后，站点一般为：`https://<你的用户名>.github.io/<仓库名>/`

### 不用 GitHub CLI 时

在 GitHub 网页新建空仓库（不要勾选 README），然后：

```bash
cd "/Users/文件资料/个人资料/CV_web"
git remote add origin https://github.com/<你的用户名>/<仓库名>.git
git push -u origin main
```

同样需要在 **Settings → Pages** 里把 **Source** 设为 **GitHub Actions**。
