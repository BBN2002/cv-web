# Beining BAO — Academic homepage

Static academic homepage (layout inspired by [bkzhao.github.io](https://github.com/BKZhao/bkzhao.github.io)): sidebar profile, About, News, Experience, Publications, Projects.

**Repository:** [github.com/BBN2002/cv-web](https://github.com/BBN2002/cv-web)

**Live site:** [https://bbn2002.github.io/cv-web/](https://bbn2002.github.io/cv-web/) (after Pages is enabled for the `gh-pages` branch.)

## Local preview

```bash
cd "/Users/文件资料/个人资料/CV_web"
python3 -m http.server 8080 --bind 127.0.0.1
```

Open `http://127.0.0.1:8080`.

## Optional avatar

Add a square photo as `assets/photo.jpg` and replace the initials block in `index.html` with an `<img class="avatar-photo" src="assets/photo.jpg" alt="Beining BAO" />` inside `.avatar-wrap` if desired.

## Deploy

Push to `main`; GitHub Actions publishes the `gh-pages` branch. In the repo **Settings → Pages**, set **Deploy from a branch** → **gh-pages** / **(root)**.
