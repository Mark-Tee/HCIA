"""
==================== HCIA 子网划分练习 ====================

📌 知识点：IP 地址分类、子网掩码、VLSM、可用主机计算

用 Python 验证你的子网计算能力。
"""


# === 题目一：判断 IP 地址类别 ===
# 输入一个 IP 地址的首字节，返回它的类别（A/B/C/D/E）
# hint: 参考笔记中 IP 地址分类表

def ip_class(first_octet: int) -> str:
    """返回 IP 的类别：A / B / C / D / E"""
    # TODO
    pass


# === 题目二：计算子网信息 ===
# 给定 网络地址/掩码位数，返回 (网络地址, 广播地址, 可用主机数)

def subnet_info(network: str, mask_bits: int):
    """
    示例输入: network="192.168.1.0", mask_bits=26
    示例输出: ("192.168.1.0", "192.168.1.63", 62)
    """
    # TODO: 计算可用主机数 = 2^(32-mask_bits) - 2
    # TODO: 计算广播地址（主机位全为1）
    pass


# === 题目三：判断两个 IP 是否在同一网段 ===
# IP+掩码，判断是否同一子网

def same_subnet(ip1: str, ip2: str, mask: str) -> bool:
    """
    示例: ip1="192.168.1.10", ip2="192.168.1.130", mask="255.255.255.128"
    返回: False（192.168.1.10/25 和 192.168.1.130/25 不在同一网段）
    """
    # TODO: 将 IP 和掩码转为二进制，网络位比较
    pass


# === 题目四：VLSM 划分子网 ===
# 将 192.168.1.0/24 划分为子网，满足各部门主机数需求

def vlsm_plan(network: str, base_mask: int, requirements: list):
    """
    requirements = [60, 30, 10]  # 三个部门分别需要 60、30、10 台主机
    返回每个部门的子网信息列表
    """
    # TODO
    pass


# ==================== 测试区域 ====================
if __name__ == "__main__":
    print("=== 题目一 ===")
    print("192 →", ip_class(192))  # C
    print("10 →", ip_class(10))    # A

    print("\n=== 题目二 ===")
    net, bcast, hosts = subnet_info("192.168.1.0", 26)
    print(f"网络: {net}, 广播: {bcast}, 可用主机: {hosts}")
    # → 网络: 192.168.1.0, 广播: 192.168.1.63, 可用主机: 62

    print("\n=== 题目三 ===")
    same = same_subnet("192.168.1.10", "192.168.1.130", "255.255.255.128")
    print(f"同网段? {same}")   # False

    print("\n=== 题目四 ===")
    plan = vlsm_plan("192.168.1.0", 24, [60, 30, 10])
    for i, subnet in enumerate(plan):
        print(f"部门{i+1}: {subnet}")
