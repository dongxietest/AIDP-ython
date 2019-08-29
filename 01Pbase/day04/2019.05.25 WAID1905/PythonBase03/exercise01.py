"""
    练习１：　
    录入并打印基金数据。
"""
code = int(input("基金代码："))
name = input("基金简称：")
unit = float(input("单位净量："))
alls = float(input("累计净量："))
rate = float(input("日增长率："))
money = float(input("手续费："))

print("%-4s%-8s%-22s%8s%8s%8s%8s%8s%8s" %
      ("序号", "基金代码", "基金简称", "单位净量",
      "累计净量", "单位净量", "累计净量",
      "日增长率", "手续费"))

print("%02d    %06d      %-26s%12.4f%12.4f%12.2f%12.2f%11.2f%%%10.2f%%"
      %
      (1, code, name, unit, alls,
      unit, alls, rate, money))
