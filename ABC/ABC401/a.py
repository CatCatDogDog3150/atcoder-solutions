# AtCoder Beginner Contest 401 - Problem A
# 問題リンク: https://atcoder.jp/contests/abc401/tasks/abc401_a
# 実行時間: 33 ms
# メモリ: 14260 KB
# アルゴリズム: 条件分岐

# 問題の概要:
# 100以上999以下の整数Sが与えられる。
# Sが200以上299以下のときSuccess、そうでないときFailureと出力する。

# 解法:
# 与えられた整数が指定された範囲にあるかを単純に確認する。

# コード:
S = int(input())

if 200 <= S <= 299:
    print("Success")
else:
    print("Failure")
