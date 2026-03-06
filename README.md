# 非 Hot100 手撕题合集

这个仓库主要用于收集和整理一些**不在 Hot100 里的手撕题**，偏后端与工程实战场景。

## 项目结构

- `question/`：题目描述（`*.md`）
- `src/`：题目对应实现代码
- `test/`：对应测试代码
- `scripts/build_problem_site.py`：生成静态文档站点脚本
- `docs/`：生成后的 HTML 页面（可直接浏览）

默认按文件名前缀数字关联题目与代码，例如：
- `question/1_xxx.md`
- `src/1_xxx.go`
- `test/1_xxx_test.go`

## 生成文档（docs）

在仓库根目录执行：

```bash
./scripts/build_problem_site.py
```

执行成功后会在 `docs/` 下生成：
- `index.html`（主页）
- `problem-*.html`（每道题的详情页，左题目右代码）

## 如何查看 docs

有两种方式：

1. 直接双击或浏览器打开 `docs/index.html`
2. 本地起一个静态服务后访问（更推荐）

```bash
cd docs
python3 -m http.server 8000
```

然后在浏览器访问：`http://localhost:8000`

## 备注

- 页面支持代码高亮和浅色/深色主题切换
- 新增题目后，重新执行一次生成脚本即可更新站点
