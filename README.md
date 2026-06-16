# clean_cli_py

指定したフォルダ配下を再帰的に検索し、名前に特定の文字列を含むファイルまたはフォルダを削除する Python CLI です。

## 機能

- サブフォルダまで再帰的に検索
- 第3引数で削除対象を指定
  - `e`: ファイルを削除
  - `f`: フォルダを削除
- 第3引数省略時は `e`（ファイル削除）

## 使い方

```bash
python delete_targets.py <folder_name> <target_text> [e|f]
```

### 例

#### ファイルを削除

```bash
python delete_targets.py ./test abc e
```

#### フォルダを削除

```bash
python delete_targets.py ./test abc f
```

#### 第3引数を省略

```bash
python delete_targets.py ./test abc
```

## 引数

1. `folder_name`  
   検索開始フォルダ
2. `target_text`  
   ファイル名またはフォルダ名に含まれる対象文字列
3. `target_type`（省略可）  
   - `e`: ファイルを削除
   - `f`: フォルダを削除
   - 省略時: `e`

## 注意

- 判定対象は**ファイル内容ではなく名前**です。
- フォルダ削除時は中身ごと削除されます。
- 削除は元に戻せません。
