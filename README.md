# GitHub Actions サンプルリポジトリ

このリポジトリは、GitHub Actionsを使ったCI/CDの基本的な使い方を紹介するためのサンプルリポジトリです。

## 使用されているワークフロー

このリポジトリには、プッシュやプルリクエストが発生した際に簡単なメッセージを出力するワークフローが設定されています。

### ワークフローファイル

`.github/workflows/simple-workflow.yml`

```yaml
name: TestWorkFlow

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Print message
        run: echo "Hello, World!"
```
