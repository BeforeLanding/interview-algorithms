"""在仓库目录运行 python check.py，执行每题文件底部的示例断言。"""

from pathlib import Path
import runpy


if __name__ == "__main__":
    files = sorted(Path(__file__).parent.glob("[0-9][0-9][0-9][0-9]_*.py"))
    for path in files:
        runpy.run_path(str(path), run_name="__main__")
    print(f"\n全部 {len(files)} 道题的示例通过。")
