# HCIA 华为认证学习笔记

> HCIA (Huawei Certified ICT Associate) 华为认证 ICT 工程师。基于数通课程体系，覆盖 OSI 七层、VRP 系统、路由、交换、网络服务、WLAN。

---

## 📑 目录

- [1. 数通基础（01-13）](#1-数通基础)
- [2. VRP 系统（14-19）](#2-vrp-系统)
- [3. 路由技术（20-26）](#3-路由技术)
- [4. 交换技术（27-32）](#4-交换技术)
- [5. 网络服务与 WAN（33-38）](#5-网络服务与-wan)
- [6. WLAN 无线局域网（39-41）](#6-wlan-无线局域网)
- [速查表与常见面试题](#速查表与常见面试题)

---

## 1. 数通基础

> 对应课程 00-13，逐层理解网络通信原理。

### 1-1 课程介绍与数通基础

> **数通 (Datacom)** = 数据通信，计算机网络的核心技术栈。

**网络三要素：**
- 通信主体：计算机、交换机、路由器等终端设备
- 通信介质：双绞线、光纤、同轴电缆、无线电磁波
- 通信协议：TCP/IP、HTTP、OSPF 等规则

**常见网络拓扑：**
- 星型：中心节点连接所有设备（最常用）
- 总线型：所有设备共享一条线路
- 环型：每个设备连接两个邻居
- 网状：多个节点之间全互联

### 1-2 网络模型

> OSI 七层模型是理论标准，TCP/IP 四层模型是实际使用标准。

| 层号 | OSI 七层 | 功能 | 协议/设备 |
|------|---------|------|----------|
| 7 | 应用层 | 用户接口 | HTTP, FTP, DNS |
| 6 | 表示层 | 加密/压缩/格式转换 | SSL, JPEG, ASCII |
| 5 | 会话层 | 建立/管理/终止会话 | NetBIOS, RPC |
| 4 | 传输层 | 端到端可靠传输 | **TCP**, **UDP** |
| 3 | 网络层 | 逻辑寻址、路由选择 | **IP**, ICMP, 路由器 |
| 2 | 数据链路层 | 物理寻址、帧封装 | MAC, 交换机 |
| 1 | 物理层 | 比特流传输 | 线缆、光纤、集线器 |

**TCP/IP 四层与 OSI 对应：**

| TCP/IP 层 | 对应 OSI | 核心协议 |
|-----------|---------|---------|
| 应用层 | 5~7 | HTTP, DNS, SMTP, FTP |
| 传输层 | 4 | TCP, UDP |
| 网络层 | 3 | IP, ICMP, ARP |
| 网络接入层 | 1~2 | 以太网, Wi-Fi |

> **口诀**：物数网传会表应 —— 物理层、数据链路层、网络层、传输层、会话层、表示层、应用层

### 1-3 应用层

> 应用层是 OSI 最顶层，直接为用户程序提供网络服务。

| 协议 | 全称 | 端口 | 说明 |
|------|------|------|------|
| **HTTP** | HyperText Transfer Protocol | 80 | 网页浏览 |
| **HTTPS** | HTTP Secure | 443 | 加密网页 |
| **FTP** | File Transfer Protocol | 20/21 | 文件传输 |
| **DNS** | Domain Name System | 53 | 域名→IP |
| **SMTP** | Simple Mail Transfer | 25 | 发送邮件 |
| **POP3** | Post Office Protocol v3 | 110 | 接收邮件 |
| **Telnet** | Terminal Network | 23 | 远程登录（明文） |
| **SSH** | Secure Shell | 22 | 安全远程登录 |
| **DHCP** | Dynamic Host Config | 67/68 | 动态分配 IP |
| **SNMP** | Simple Network Mgmt | 161/162 | 网络管理 |

### 1-4 SNMP

> SNMP (Simple Network Management Protocol) 用于集中管理网络设备，监控状态、收集信息。

**SNMP 三组件：**

| 组件 | 说明 |
|------|------|
| **NMS** (管理站) | 管理端软件，主动查询或接收告警 |
| **Agent** (代理) | 被管设备上的 SNMP 服务 |
| **MIB** (管理信息库) | 设备的可管理信息集合（CPU、内存、接口流量等） |

**版本对比：**

| 版本 | 安全性 | 说明 |
|------|--------|------|
| SNMPv1 | 弱（community 明文） | 基本功能 |
| SNMPv2c | 弱 | 增强了性能和告警 |
| SNMPv3 | 强（加密+认证） | 推荐使用 |

### 1-5 传输层

> 传输层提供端到端的数据传输服务，核心协议是 TCP 和 UDP。

| | **TCP** | **UDP** |
|---|---|---|
| 连接 | 面向连接（三次握手） | 无连接 |
| 可靠性 | 可靠，确认重传 | 不可靠，不确认 |
| 速度 | 慢 | 快 |
| 头部大小 | 20 字节 | 8 字节 |
| 场景 | 网页、文件、邮件 | 视频、语音、DNS、DHCP |

**TCP 三次握手：**

```
客户端                服务器
  │──── SYN ──────→│  # 1. 客户端请求连接
  │←── SYN+ACK ────│  # 2. 服务器确认
  │──── ACK ──────→│  # 3. 客户端确认
  │   连接建立 ✅    │
```

**TCP 四次挥手：**

```
  │──── FIN ──────→│  # 客户端请求断开
  │←── ACK ───────│  # 服务器确认
  │←── FIN ───────│  # 服务器请求断开（数据发完）
  │──── ACK ──────→│  # 客户端确认
  │   连接关闭 ✅    │
```

### 1-6 网络层

> 网络层负责**逻辑寻址和路径选择**，实现跨网段通信。

**核心功能：**
- IP 地址编址与路由
- IP 数据包封装与解封装
- ICMP 差错检测与网络诊断

**网络层协议：**
| 协议 | 说明 |
|------|------|
| IP | 互联网核心协议，寻址和转发 |
| ICMP | 网络诊断（ping/tracert 基于它） |
| ARP | IP → MAC 地址解析 |

### 1-7 IP 协议

> IP (Internet Protocol) 是 TCP/IP 栈的核心，提供无连接、尽力而为的数据传输。

**IPv4 数据包头部关键字段：**

| 字段 | 位数 | 说明 |
|------|------|------|
| Version | 4 | IPv4=4 |
| TTL | 8 | 生存时间，每经过一跳减 1，减到 0 丢弃 |
| Protocol | 8 | 上层协议（6=TCP, 17=UDP） |
| Source IP | 32 | 源 IP 地址 |
| Dest IP | 32 | 目的 IP 地址 |

### 1-8 IP 地址与子网划分

> IPv4 共 32 位，4 组，每组 8 位，点分十进制表示。

**IP 地址分类：**

| 类别 | 首字节 | 默认掩码 | 网络数 | 主机数 |
|------|--------|---------|--------|--------|
| **A 类** | 0xxx... 1~126 | `255.0.0.0` /8 | 126 | ~1600 万 |
| **B 类** | 10xx... 128~191 | `255.255.0.0` /16 | ~1.6 万 | 65534 |
| **C 类** | 110x... 192~223 | `255.255.255.0` /24 | ~200 万 | 254 |
| **D 类** | 1110... 224~239 | — | 组播地址 | — |
| **E 类** | 1111... 240~255 | — | 保留 | — |

**私有地址（RFC 1918）：**

| 类别 | 范围 |
|------|------|
| A 类 | `10.0.0.0 ~ 10.255.255.255` |
| B 类 | `172.16.0.0 ~ 172.31.255.255` |
| C 类 | `192.168.0.0 ~ 192.168.255.255` |

**子网掩码与 CIDR：**

```
IP:    192.168.  1.  100
掩码:  255.255.255.   0     = /24
       └──网络位──┘ └主机位┘

可用主机数 = 2^(32 - 掩码位数) - 2
可用子网数 = 2^(借用位数)
```

**VLSM 示例** — 192.168.1.0/24 分 4 个子网（借 2 位，/26）：

```
子网1: 192.168.1.0   /26  主机: .1 ~ .62
子网2: 192.168.1.64  /26  主机: .65 ~ .126
子网3: 192.168.1.128 /26  主机: .129 ~ .190
子网4: 192.168.1.192 /26  主机: .193 ~ .254
```

### 1-9 ICMP

> ICMP (Internet Control Message Protocol) 网络诊断协议，封装在 IP 包中。

**常见 ICMP 类型和应用：**

| 类型 | 说明 | 工具 |
|------|------|------|
| Echo Request (8) / Reply (0) | 连通性测试 | `ping` |
| TTL Exceeded (11) | 跳数超限 | `tracert` |
| Destination Unreachable (3) | 目标不可达 | — |

```bash
ping 8.8.8.8                     # ICMP Echo 测试连通性
tracert 8.8.8.8                  # 追踪路径（逐跳发送，TTL递增）
```

### 1-10 数据链路层

> 数据链路层在物理层之上，提供**物理寻址（MAC）和差错检测**，以"帧"为单位传输。

**MAC 地址：** 48 位，6 组十六进制，全球唯一。
```
格式： xx:xx:xx:xx:xx:xx
示例： 00:e0:fc:12:34:56
        └─前24位厂商OUI─┘ └─后24位设备编号─┘
```

**以太网帧结构：**
```
┌──────┬──────┬──────┬────┬──────────┬──────┐
│前导码│目的MAC│源MAC │类型│  数据载荷  │ CRC  │
│ 8B  │ 6B  │ 6B  │2B │  46~1500B │ 4B  │
└──────┴──────┴──────┴────┴──────────┴──────┘
```

### 1-11 ARP

> ARP (Address Resolution Protocol) 将 IP 地址解析为 MAC 地址。

**工作原理：**
```
主机A (192.168.1.1) 想给 192.168.1.2 发数据：
  1. 查 ARP 缓存表 — 没有 192.168.1.2 的 MAC
  2. 发送 ARP Request（广播）：谁的 IP 是 192.168.1.2？
  3. 主机B 回复 ARP Reply（单播）：是我，MAC=00:11:22:33:44:55
  4. 主机A 把映射写入 ARP 缓存表
```

### 1-12 物理层

> 物理层是 OSI 最底层，负责比特流的**传输介质和信号标准**。

| 介质类型 | 说明 |
|---------|------|
| **双绞线** | 最常用以太网介质，RJ45 接口 |
| **光纤** | 长距离、高带宽、抗干扰 |
| **同轴电缆** | 早期使用，已基本淘汰 |
| **无线电磁波** | Wi-Fi、蓝牙、卫星通信 |

| 传输方式 | 说明 |
|---------|------|
| **单工** | 单向（广播电台） |
| **半双工** | 双向但不能同时（对讲机） |
| **全双工** | 双向同时（电话） |

### 1-13 数据转发过程

> 数据从源到目的经过逐层封装（发送端）和逐层解封装（接收端）。

```
发送端封装：应用数据 → [TCP头] → [IP头] → [MAC头+尾] → 物理信号
接收端解封：物理信号 → [去MAC] → [去IP] → [去TCP] → 应用数据
```

**单播、广播、组播对比：**

| 类型 | 目标 | MAC 地址 | 场景 |
|------|------|---------|------|
| **单播** | 单一设备 | 具体 MAC | 正常通信 |
| **广播** | 所有设备 | `FF:FF:FF:FF:FF:FF` | ARP 请求 |
| **组播** | 一组设备 | `01:00:5E:...` | 视频会议 |

---

## 2. VRP 系统

> 对应课程 14-19，华为设备操作系统。

### 2-1 VRP 系统介绍

> VRP 运行在华为路由器和交换机上，类似 Windows 对 PC 的角色。

**VRP 的核心特点：**
- 统一的命令行界面（CLI）
- 模块化架构，支持多种协议栈
- 丰富的管理和维护功能

### 2-2 VRP 命令基础

**命令行视图层级：**

```bash
用户视图       <Huawei>           # 查看简单信息，最小权限
系统视图       [Huawei]           # system-view 进入，全局配置
接口视图       [Huawei-GigabitEthernet0/0/1]
路由协议视图   [Huawei-ospf-1]
VLAN 视图      [Huawei-vlan10]

# 视图切换
<Huawei> system-view            # 用户→系统
[Huawei] interface g0/0/1       # 系统→接口
[Huawei-GigabitEthernet0/0/1] quit  # 返回上一级
[Huawei-GigabitEthernet0/0/1] return  # 直接返回用户视图
```

**命令行帮助：**

| 操作 | 说明 | 示例 |
|------|------|------|
| `?` | 查看当前可用的所有命令 | `?` |
| `命令 ?` | 查看该命令后续可选参数 | `display ?` |
| `Tab` | 自动补全命令 | `sys` → `system-view` |

### 2-3 VRP 文件系统

> VRP 使用类似 Linux 的文件系统管理设备文件。

| 目录/文件 | 说明 |
|----------|------|
| `flash:/` | 主存储，存放系统文件和配置 |
| `vrpcfg.zip` | 配置文件 |
| `*.cc` | 系统软件包 |
| `*.pat` | 补丁文件 |

```bash
<Huawei> dir                        # 查看文件列表
<Huawei> copy flash:/vrpcfg.zip ftp: # 备份配置到 FTP
<Huawei> delete flash:/old.cc       # 删除文件
```

### 2-4 VRP 基本配置

```bash
# ===== 设备基本信息 =====
<Huawei> system-view
[Huawei] sysname Core-SW-01         # 设备命名

# ===== 接口配置 =====
[Huawei] interface GigabitEthernet 0/0/1
[Huawei-GigabitEthernet0/0/1] description To-PC-01
[Huawei-GigabitEthernet0/0/1] ip address 192.168.1.1 255.255.255.0
[Huawei-GigabitEthernet0/0/1] undo shutdown    # 开启接口

# ===== 查看信息 =====
<Huawei> display version             # 系统版本
<Huawei> display current-configuration  # 当前运行配置
<Huawei> display ip interface brief     # 接口 IP 摘要
<Huawei> display interface brief        # 接口状态摘要
<Huawei> display cpu-usage              # CPU 使用率
<Huawei> display memory-usage           # 内存使用率

# ===== 保存/恢复 =====
<Huawei> save                        # 保存当前配置
<Huawei> reset saved-configuration   # 清除已保存配置
<Huawei> reboot                      # 重启设备
```

### 2-5 VRP 远程管理

```bash
# Telnet 配置（不加密，不推荐）
[Huawei] user-interface vty 0 4
[Huawei-ui-vty0-4] authentication-mode password
[Huawei-ui-vty0-4] set authentication password cipher 123456

# SSH 配置（推荐）
[Huawei] rsa local-key-pair create              # 生成密钥对
[Huawei] user-interface vty 0 4
[Huawei-ui-vty0-4] authentication-mode aaa      # 使用 AAA 认证
[Huawei-ui-vty0-4] protocol inbound ssh         # 只允许 SSH
[Huawei] ssh user admin authentication-type password
[Huawei] ssh user admin service-type stelnet
```

### 2-6 VRP 系统升级

> 通过 FTP/TFTP 将新的系统软件包上传到设备，指定下次启动文件后重启。

```bash
# 升级流程
<Huawei> dir                               # 确认剩余空间
<Huawei> tftp 10.0.0.100 get new.cc        # 从 TFTP 下载新版本
<Huawei> startup system-software new.cc    # 指定下次启动文件
<Huawei> display startup                   # 确认启动文件
<Huawei> reboot                            # 重启完成升级
```

---

## 3. 路由技术

> 对应课程 20-26，静态路由、OSPF、路由汇总与认证。

### 3-1 路由基础

> 路由器根据**路由表**转发数据包。路由表中包含目的网络、下一跳、出接口等信息。

**路由表来源：**

| 来源 | 优先级 | 说明 |
|------|--------|------|
| **直连路由** | 0 | 接口配置 IP 后自动生成 |
| **静态路由** | 60 | 管理员手动配置 |
| **OSPF** | 10（内部）/ 150（外部） | 链路状态协议 |
| **RIP** | 100 | 距离矢量协议 |

> 数字越小优先级越高。优先级相同时比较度量值。

**路由选路三原则：**
1. 最长掩码匹配（最精确的路由优先）
2. 优先级越小越优先
3. 度量值（Cost）越小越优先

### 3-2 静态路由

> 管理员手动配置路由，不随网络变化自动调整。

```bash
# 静态路由命令格式
ip route-static 目标网络 掩码 {下一跳IP | 出接口} [preference 优先级]

# 示例：去往 192.168.2.0/24 走下一跳 10.0.0.2
[Huawei] ip route-static 192.168.2.0 24 10.0.0.2

# 查看路由表
<Huawei> display ip routing-table
```

**默认路由（缺省路由）：**
```bash
# 0.0.0.0/0 匹配所有网络，作为"兜底"路由
[Huawei] ip route-static 0.0.0.0 0.0.0.0 10.0.0.254
```

### 3-3 路由汇总

> 将多个子网合并为一个更大的网络，减小路由表规模。

**汇总前需要满足的条件：**
- 子网连续
- 网络位数相同（或可合并）

```bash
# 汇总前：
192.168.1.0/24  → 10.0.0.2
192.168.2.0/24  → 10.0.0.2
192.168.3.0/24  → 10.0.0.2

# 汇总后（一条代替三条）：
192.168.0.0/22  → 10.0.0.2
```

### 3-4 动态路由与 OSPF

> OSPF (Open Shortest Path First) 是链路状态路由协议，适用于中大型网络。

**OSPF 核心概念：**

| 概念 | 说明 |
|------|------|
| **Router ID** | 路由器唯一标识 |
| **Area** | 区域，Area 0 是骨干区域 |
| **Cost** | 开销 = 100Mbps / 接口带宽 |
| **邻居关系** | Full、2-Way 等状态 |
| **LSA** | 链路状态通告 |

**OSPF 三张表：**
1. **邻居表** — 记录邻居路由器
2. **链路状态数据库 (LSDB)** — 全网拓扑
3. **路由表** — 最优路由

**基本配置：**
```bash
[Huawei] ospf 1 router-id 1.1.1.1
[Huawei-ospf-1] area 0
[Huawei-ospf-1-area-0.0.0.0] network 10.0.0.0 0.0.0.255
[Huawei-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255

<Huawei> display ospf peer brief    # 查看邻居
<Huawei> display ospf routing       # 查看 OSPF 路由
```

### 3-5 路由认证与缺省路由发布

**OSPF 接口认证（防止非法路由器接入）：**
```bash
[Huawei] interface GigabitEthernet 0/0/1
[Huawei-GigabitEthernet0/0/1] ospf authentication-mode md5 1 cipher 123456
```

**OSPF 缺省路由发布：**
```bash
# 让区域内的其他路由器学到这条默认路由
[Huawei-ospf-1] default-route-advertise always
```

---

## 4. 交换技术

> 对应课程 27-32，VLAN、STP、链路聚合、堆叠。

### 4-1 交换基础

> 交换机基于 **MAC 地址表** 转发帧。收到帧时学习源 MAC + 端口，查表转发目的 MAC。

**交换机转发行为：**

| 行为 | 条件 | 说明 |
|------|------|------|
| **单播** | 目标 MAC 在表中 | 精准转发 |
| **泛洪** | 目标 MAC 未知或广播 | 向所有端口发送（接收口除外） |
| **丢弃** | 目标端口 = 源端口 | 同端口不转发 |

### 4-2 VLAN 原理与配置

> VLAN 将物理交换机逻辑划分为多个独立广播域。不同 VLAN 默认不能通信。

**VLAN 的好处：**
- 隔离广播域，减少广播风暴
- 提高安全性（部门之间隔离）
- 灵活组网（跨交换机划分 VLAN）

**VLAN 接口类型：**

| 类型 | 携带 VLAN | 适用场景 |
|------|----------|---------|
| **Access** | 一个 VLAN，去标签 | 连接终端（PC） |
| **Trunk** | 多个 VLAN，打 802.1Q 标签 | 交换机之间 |
| **Hybrid** | 灵活控制（华为特有） | 混合场景 |

```bash
# 创建 VLAN
[Huawei] vlan 10
[Huawei-vlan10] description Sales

# Access 端口
[Huawei] interface GigabitEthernet 0/0/1
[Huawei-GE0/0/1] port link-type access
[Huawei-GE0/0/1] port default vlan 10

# Trunk 端口
[Huawei] interface GigabitEthernet 0/0/24
[Huawei-GE0/0/24] port link-type trunk
[Huawei-GE0/0/24] port trunk allow-pass vlan 10 20 30

# 查看 VLAN
<Huawei> display vlan
<Huawei> display port vlan
```

### 4-3 VLAN 间路由

> 不同 VLAN 之间的通信必须经过三层设备（路由器或三层交换机）。

```bash
# 三层交换机配置 VLANIF（SVI 接口）
[Huawei] interface Vlanif 10
[Huawei-Vlanif10] ip address 192.168.10.1 24

[Huawei] interface Vlanif 20
[Huawei-Vlanif20] ip address 192.168.20.1 24

# VLAN 10 的主机网关 → 192.168.10.1
# VLAN 20 的主机网关 → 192.168.20.1
# 两个 VLAN 通过三层交换机互通
```

### 4-4 STP 生成树协议

> STP 通过阻塞冗余链路避免广播风暴，同时提供链路备份。

**STP 角色：**
- **根桥**：全网唯一，选举标准（Bridge ID 最小）
- **根端口**：非根桥上离根最近的端口
- **指定端口**：每个网段上离根最近的端口
- **阻塞端口**：既不是根端口也不是指定端口，被阻塞

**RSTP**（快速生成树）收敛更快，端口状态更少。

### 4-5 以太网链路聚合

> 将多个物理端口捆绑为一个逻辑端口，提升带宽和可靠性。

```bash
[Huawei] interface Eth-Trunk 1
[Huawei-Eth-Trunk1] mode manual load-balance

[Huawei] interface GigabitEthernet 0/0/1
[Huawei-GE0/0/1] eth-trunk 1

[Huawei] interface GigabitEthernet 0/0/2
[Huawei-GE0/0/2] eth-trunk 1
```

### 4-6 堆叠与集群

> 将多台物理交换机虚拟化为一个逻辑交换机，简化管理和提升可靠性。

| 特性 | 堆叠 (iStack) | 集群 (CSS) |
|------|-------------|-----------|
| **适用** | 盒式交换机 | 框式交换机 |
| **管理** | 一个 IP 统一管理 | 一个 IP 统一管理 |
| **冗余** | 主备倒换 | 主备倒换 |

---

## 5. 网络服务与 WAN

> 对应课程 33-38，DHCP、ACL、NAT、广域网协议。

### 5-1 DHCP

> DHCP 自动分配 IP 地址。DORA 四次交互：Discover→Offer→Request→ACK。

```bash
[Huawei] dhcp enable
[Huawei] ip pool VLAN10_Pool
[Huawei-ip-pool-VLAN10_Pool] network 192.168.10.0 mask 24
[Huawei-ip-pool-VLAN10_Pool] gateway-list 192.168.10.1
[Huawei-ip-pool-VLAN10_Pool] dns-list 8.8.8.8
[Huawei-ip-pool-VLAN10_Pool] excluded-ip-address 192.168.10.1 192.168.10.10

[Huawei] interface Vlanif 10
[Huawei-Vlanif10] dhcp select global

<Huawei> display ip pool
```

### 5-2 ACL 访问控制列表

> ACL 通过规则匹配流量，实现访问控制。

| ACL 类型 | 编号 | 匹配依据 |
|---------|------|---------|
| **基本 ACL** | 2000~2999 | 只匹配源 IP |
| **高级 ACL** | 3000~3999 | 源/目的 IP、端口、协议 |

```bash
# 基本 ACL：禁止 192.168.1.100 访问外网
[Huawei] acl 2000
[Huawei-acl-basic-2000] rule deny source 192.168.1.100 0
[Huawei-acl-basic-2000] rule permit source any

# 高级 ACL：只允许 192.168.1.0/24 访问 10.0.0.1 的 80 端口
[Huawei] acl 3000
[Huawei-acl-adv-3000] rule permit tcp source 192.168.1.0 0.0.0.255 destination 10.0.0.1 0 destination-port eq 80
```

### 5-3 NAT 网络地址转换

> NAT 将私有 IP 转为公网 IP，解决 IPv4 地址枯竭问题。

| 类型 | 说明 | 配置 |
|------|------|------|
| **静态 NAT** | 一对一 | `nat static` |
| **动态 NAT** | 多对多（地址池） | `nat address-group` |
| **NAPT** | 多对一 + 端口 | 最常用（Easy IP） |

```bash
# Easy IP：内网上网都用出接口的公网 IP
[Huawei] acl 2000
[Huawei-acl-basic-2000] rule permit source 192.168.0.0 0.0.255.255
[Huawei] interface GigabitEthernet 0/0/1
[Huawei-GE0/0/1] nat outbound 2000
```

### 5-4 广域网概述与 PPP

> WAN (Wide Area Network) 连接分布在不同地理位置的局域网。

**广域网协议对比：**

| 协议 | 特点 |
|------|------|
| **PPP** | 点到点，支持认证（PAP/CHAP） |
| **PPPoE** | PPP over Ethernet，用于宽带拨号 |
| **HDLC** | 华为默认串口封装，简单高效 |

### 5-5 PPPoE

> PPPoE 在以太网上运行 PPP 协议，用于 ADSL/宽带拨号。

```bash
# PPPoE 客户端配置（路由器拨号上网）
[Huawei] dialer-rule
[Huawei-dialer-rule] dialer-rule 1 ip permit
[Huawei] interface Dialer 1
[Huawei-Dialer1] dialer user admin
[Huawei-Dialer1] dialer bundle 1
[Huawei-Dialer1] ppp chap user admin
[Huawei-Dialer1] ppp chap password cipher 123456
[Huawei-Dialer1] ip address ppp-negotiate
```

---

## 6. WLAN 无线局域网

> 对应课程 39-41，基础概念、频段、组网方式。

### 6-1 WLAN 基础

> WLAN (Wireless LAN) 通过无线电磁波通信，标准为 IEEE 802.11。

**WLAN 组件：**

| 组件 | 说明 |
|------|------|
| **STA** | 终端（Station），手机/笔记本 |
| **AP** | 接入点 (Access Point)，无线信号发射 |
| **AC** | 控制器，集中管理多个 AP |
| **DS** | 分布式系统，连接有线网络 |

### 6-2 WLAN 频段

| 频段 | 频率 | 信道 | 特点 |
|------|------|------|------|
| **2.4 GHz** | 2.4~2.4835 GHz | 1~13（互不干扰基本只有 3 个） | 覆盖远，干扰多 |
| **5 GHz** | 5.15~5.85 GHz | 更多信道 | 速度快，干扰少 |

### 6-3 WLAN 组网

**组网模式对比：**

| 模式 | 说明 | 适用 |
|------|------|------|
| **FAT AP** | 独立 AP，自行管理 | 小型场景（家用） |
| **FIT AP + AC** | AC 集中管理 AP | 企业级（最常用） |

**CAPWAP 协议：** AC 和 AP 之间的管理和数据隧道协议。

---

## 7. 速查表与常见面试题

### 协议端口速查

| 协议 | 端口 | 协议 | 端口 |
|------|------|------|------|
| HTTP | 80 | HTTPS | 443 |
| DNS | 53 | DHCP | 67/68 |
| FTP | 20/21 | SSH | 22 |
| Telnet | 23 | SMTP | 25 |
| POP3 | 110 | SNMP | 161/162 |

### VRP 命令速查

| 命令 | 作用 |
|------|------|
| `display version` | 查看版本 |
| `display current-configuration` | 当前配置 |
| `display ip routing-table` | 路由表 |
| `display vlan` | VLAN 信息 |
| `display ospf peer brief` | OSPF 邻居 |
| `display ip interface brief` | 接口 IP 摘要 |
| `display interface brief` | 接口状态摘要 |
| `save` | 保存配置 |

### 常见面试题

**1. TCP 为什么是三次握手而不是两次？**
> 防止失效的连接请求到达服务器导致误开连接。两次握手无法确认客户端接收能力。

**2. VLAN 的作用？**
> 隔离广播域、提高安全性、灵活组网。不同 VLAN 必须通过三层设备（路由器/三层交换机）互通。

**3. OSPF 的 Area 0 作用？**
> 骨干区域，所有非骨干区域必须与 Area 0 直连。防止路由环路。

**4. STP 的作用？**
> 避免二层环路导致的广播风暴，同时提供链路冗余备份。

**5. NAT 的工作原理？**
> 将内网私有 IP+端口 映射为公网 IP+端口，实现多个内网主机共享一个公网地址上网。

**6. Access 和 Trunk 端口的区别？**
> Access 只承载一个 VLAN（去标签），连接终端；Trunk 承载多个 VLAN（带 802.1Q 标签），连接交换机之间。

---

*最后更新：2026-06-28*
