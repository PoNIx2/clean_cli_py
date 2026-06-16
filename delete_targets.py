#!/usr/bin/env python3
from pathlib import Path
import argparse
import shutil
import sys


def delete_targets(folder_name: str, target_text: str, target_type: str = "e") -> None:
    """
    指定フォルダ配下を再帰的に検索し、名前に target_text を含む
    ファイルまたはフォルダを削除する。

    Args:
        folder_name (str): 検索開始フォルダ
        target_text (str): 名前に含まれる対象文字列
        target_type (str):
            "e" -> ファイルを削除
            "f" -> フォルダを削除
            省略時は "e"
    """
    base_path = Path(folder_name)

    if not base_path.exists():
        raise FileNotFoundError(f"フォルダが存在しません: {folder_name}")

    if not base_path.is_dir():
        raise NotADirectoryError(f"ディレクトリではありません: {folder_name}")

    if target_type not in ("e", "f"):
        raise ValueError("第3引数は 'e' または 'f' を指定してください。")

    if target_type == "e":
        for path in base_path.rglob("*"):
            if path.is_file() and target_text in path.name:
                path.unlink()
                print(f"削除(ファイル): {path}")
    else:
        dirs_to_delete = [
            path for path in base_path.rglob("*")
            if path.is_dir() and target_text in path.name
        ]
        dirs_to_delete.sort(key=lambda p: len(p.parts), reverse=True)

        for path in dirs_to_delete:
            if path.exists():
                shutil.rmtree(path)
                print(f"削除(フォルダ): {path}")


def main():
    parser = argparse.ArgumentParser(
        description="指定文字列を名前に含むファイルまたはフォルダを再帰的に削除するCLI"
    )
    parser.add_argument("folder_name", help="検索開始フォルダ")
    parser.add_argument("target_text", help="名前に含まれる対象文字列")
    parser.add_argument(
        "target_type",
        nargs="?",
        default="e",
        choices=["e", "f"],
        help="削除対象: e=ファイル, f=フォルダ（省略時: e）"
    )

    args = parser.parse_args()

    try:
        delete_targets(args.folder_name, args.target_text, args.target_type)
    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
