# 条件分岐（Conditional Statements）

## 概要
条件分岐は、プログラムの流れを制御するための基本的な構文です。

## 基本形
```python
if condition:
    # conditionが真の場合に実行
    process_true()
else:
    # conditionが偽の場合に実行
    process_false()
if x >= a and x <= b:
    print("範囲内")
else:
    print("範囲外")

# 簡略化記法
if a <= x <= b:
    print("範囲内")
使用した問題

ABC401 A - Arrange

注意点

等号の向きに注意（<=、>=）
複数条件の組み合わせはandやorを使用
Pythonでは a <= x <= b のような範囲指定が可能
