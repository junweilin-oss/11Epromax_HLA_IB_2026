# Python 3，无需安装第三方库。
# 比较同一起点、已经对齐、没有插入/缺失的两条 CDS 序列。
# 每条序列粘贴为一行，不包含 FASTA 标题、行号或 Query 名称。
# 完整 CDS 的起点填 1；截图最后一段的起点填 181。
# 突变体中的英文句点 . 表示该位置与 WT 相同。
# CDS 编号从起始密码子 ATG 的 A = c.1 开始。

start_text = input("这段序列的 CDS 起点（直接回车表示 1）：").strip()
if start_text == "":
    start_text = "1"
if not start_text.isdecimal() or int(start_text) < 1:
    raise SystemExit("错误：起点必须是大于等于 1 的整数。")
start = int(start_text)

wt = "".join(input("WT 序列：").split()).upper()
mut = "".join(input("突变体序列（允许 .）：").split()).upper()

if not wt or len(wt) != len(mut):
    raise SystemExit("错误：两条序列必须非空且长度相同；本程序不处理插入或缺失。")
if any(base not in "ACGT" for base in wt):
    raise SystemExit("错误：WT 只能含 A、C、G、T。")
if any(base not in "ACGT." for base in mut):
    raise SystemExit("错误：突变体只能含 A、C、G、T 或英文句点 .。")

# 把突变体中的 . 还原成对应的 WT 碱基。
mut = "".join(wt[i] if mut[i] == "." else mut[i] for i in range(len(wt)))

found = False
for i in range(len(wt)):
    if wt[i] != mut[i]:
        found = True
        position = start + i              # CDS 碱基编号，从 1 开始
        codon = (position - 1) // 3 + 1   # 第几个密码子
        inside = (position - 1) % 3 + 1  # 密码子内的第几个碱基
        left = i - (inside - 1)          # 该密码子在输入字符串中的起始下标

        print(f"\n单个位点变化：c.{position}{wt[i]}>{mut[i]}")
        print(f"第 {codon} 个密码子，第 {inside} 个碱基")
        if 0 <= left and left + 3 <= len(wt):
            print(f"密码子：{wt[left:left + 3]} -> {mut[left:left + 3]}")
        else:
            print("该密码子有一部分在输入片段之外，请补充相邻序列。")

if not found:
    print("输入片段内没有发现差异。")

# 截图示例：依次输入下面三行（不含 # 和空格）。
# 181
# ACAAACTACAATGCTGGAGACAGAAGCACTGATTATGGGATATTTCAGATCAATAGCCGC
# ACAAACTACAATGCTGGAGACAGAAGCACTGATTATGGGACATTTCAGATCAATAGCCGC
# 预期：CDS 第 221 位 T -> C；第 74 个密码子第 2 位；ATA -> ACA。
# 若有多个差异，本程序逐个定位，不将它们组合成完整的 HGVS 变异描述。
