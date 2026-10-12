# ホーマン遷移軌道をPythonで計算する｜衛星を別の軌道へ運ぶΔv

[![run](https://github.com/jumpei1228/space-hohmann-transfer-python/actions/workflows/run.yml/badge.svg)](https://github.com/jumpei1228/space-hohmann-transfer-python/actions/workflows/run.yml)

低軌道から静止軌道へ衛星を運ぶ「ホーマン遷移」を、Pythonで実装。2回のエンジン噴射でどれだけの速度変化（Δv）が要るのかを計算し、燃料計画の基礎を手を動かして理解します。

> 📖 このコードの詳しい解説（理論・図解つき）は元記事をどうぞ:
> **[ホーマン遷移軌道をPythonで計算する｜衛星を別の軌道へ運ぶΔv](https://space.yurufuwa.work/learn/hohmann-transfer-python)** — ゆるふわ宇宙・航空

## セットアップ

```bash
pip install -r requirements.txt
```

## 実行方法

```bash
python hohmann-transfer-python.py
```

## これは何？

[ゆるふわ宇宙・航空](https://space.yurufuwa.work) はやさしい技術解説サイト「ゆるふわ」シリーズの一つです。このリポジトリは記事内で解説しているコードをそのまま動かせる形にまとめた、記事の副教材（コンパニオンリポジトリ）です。

## License

MIT
