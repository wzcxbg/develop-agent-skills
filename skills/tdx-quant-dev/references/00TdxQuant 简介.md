# [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#tdxquant-简介)TdxQuant 简介

TdxQuant是由深圳市财富趋势科技股份有限公司研发的专业量化投研平台，专注于为国内量化投资者提供从策略研究到投资决策的全流程解决方案。平台以高效、简洁为核心设计理念，致力于降低量化交易门槛，提升策略开发与执行的效率。

依托通达信近三十余年在金融科技领域的深厚积累，TdxQuant集成了完备的实时和历史行情数据、金融数据库及稳定的交易系统基础设施，为策略的研发、回测、验证和执行提供了坚实可靠的技术支持。

平台采用分层化、模块化的服务体系，可灵活适配从高校学生、独立研究者、个人投资者到专业机构等不同用户的需求，实现从策略构思到交易落地的无缝衔接。

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#tdxquant-服务介绍)TdxQuant 服务介绍

TdxQuant 是一套基于通达信金融终端构建的 Python 量化策略运行框架。该框架通过 API 接口形式，为策略交易提供所需的行情数据获取与交易指令执行功能。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#运行环境要求)运行环境要求

TdxQuant 支持 64 位 Python 3.7、3.8、3.9、3.10、3.11、3.12、3.13等版本，系统会自动适配当前 Python 版本，建议使用3.13版本。
**请注意**：运行 TdxQuant 程序前，需预先启动支持TQ策略功能的 **通达信金融终端、专业研究版等版本**。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#核心运行逻辑)核心运行逻辑

TdxQuant 以 **tqcenter** 行情模块为核心，专注于为量化交易者提供高效、直接的数据服务，主要包含以下内容：

- **行情数据**：实时与历史的快照、K 线、分笔（Tick）数据
- **基本面数据**：除权除息、基本财务、专业财务、股票交易数据、市场数据等
- **新股和合约等信息**：标的基础信息、可转债、新股申购等
- **分类数据**：市场类型、行业分类、自定义板块等

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#核心应用场景)核心应用场景

TdxQuant提供覆盖量化投研全流程的核心功能模块，主要应用场景包括：

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_1-策略研发与历史回测)1. 策略研发与历史回测

平台提供“即用型”标准化数据。所有历史与实时数据均在服务端完成清洗、对齐，并预加载至客户端。支持用户快速获取指定时间维度的历史数据，并进行策略信号计算与回测分析。既提供复权因子，也提供各种类型的复权后的数据。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_2-实时监控与信号预警)2. 实时监控与信号预警

支持实时行情数据订阅，用户可基于自定义的指标与因子模型进行在线计算。当预设条件触发时，系统通过信号接口实时推送预警信息至客户端，助力研究者及时捕捉市场动态与交易机会。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_3-交易模拟与实盘执行)3. 交易模拟与实盘执行

平台构建了完整的策略交易闭环，提供模拟交易、券商实盘等两种执行环境：

- **模拟交易**：在仿真市场环境中，使用实时行情数据对策略进行持续跟踪与验证，评估其实际表现，全程无资金风险。
- **实盘交易**：通过稳定的交易总线，安全对接券商报盘系统，实现策略信号的自动化、高可靠性下单与交易管理。

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#量化交易的核心价值)量化交易的核心价值

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_1-利用历史数据高效验证策略-提升研究效率数百倍)1. 利用历史数据高效验证策略，提升研究效率数百倍

在验证交易策略时，历史回测是评估其有效性的关键环节，但传统人工方式难以处理海量数据与复杂计算。量化交易可在几分钟内完成一次全面回测，快速获得统计验证结果，极大提升了策略研发的迭代效率。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_2-实时捕捉基于概率的获胜机会)2. 实时捕捉基于概率的获胜机会

量化交易借助计算机强大的数据处理能力，能够从海量市场信息中发掘人工难以察觉的规律与机会。面对全市场数千只股票的实时波动，量化系统可同时监控多重条件，避免机会错失。它能够综合考量选股、择时、资产配置与风险管理，构建并执行具有较大概率的投资组合，追求收益最大化。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_3-实现科学、客观的投资决策)3. 实现科学、客观的投资决策

与传统主观投资不同，量化交易将投资理念、经验甚至市场直觉转化为严谨的数学模型。通过系统化的信号生成与执行机制，有效克服人性中的情绪偏差，使投资决策过程更具纪律性、可重复性与可优化性。

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#量化交易的工具挑战)量化交易的工具挑战

**工欲善其事，必先利其器。** 对于个人投资者而言，独立搭建一套完整的量化交易体系，复杂繁琐，涉及数据、系统、策略等多层面的巨大投入。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#一、需要准确、全面的金融数据基础)一、需要准确、全面的金融数据基础

量化交易依赖于高质量的历史与实时数据，包括行情、财务、宏观及基本面数据等。构建和维护这样一个数据仓库，不仅需要持续的数据采购、清洗、更新与运维成本，还需在数据存储、访问速度与系统稳定性方面进行深入的技术投入。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#二、需要易用、可靠的量化交易系统)二、需要易用、可靠的量化交易系统

一个成熟的量化平台需要支持多样的策略开发语言、具备高速的回测与模拟引擎、提供科学的策略评估体系，并为实盘交易提供全方位的保障。过往，研究者往往需要兼具复杂的金融数据知识与工程构建能力。如今，TdxQuant让您只需专注于策略逻辑本身，其余复杂工作交给平台。

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#tdxquant的核心优势)TdxQuant的核心优势

TdxQuant是一款集金融数据与策略投研工具于一体的量化平台，结构清晰，简洁易上手，数据获取快捷，算法资源丰富。我们的目标是为投资者提供"开箱即用"的完整解决方案。

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_1-全方位保障策略安全与自主)1. 全方位保障策略安全与自主

- 支持策略在本地IDE环境中开发与运行，保障代码安全与私密性
- 分离式模块化架构，策略的编码和调试更加自由和灵活

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_2-大幅降低量化交易门槛)2. 大幅降低量化交易门槛

- 提供高质量、高精度、快速接入的金融元数据
- 支持多种策略类型的便捷编写、回测、模拟与实盘

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/#_3-助力构建专业量化成长路径)3. 助力构建专业量化成长路径

- 通过"投资学院"系统学习量化交易相关知识体系
- 通过"宽客社区"交流心得、解答疑惑
- 全程助力用户从入门到精通，成为专业的量化投资者





# 安装通达信并获取策略

# 1. 安装通达信终端

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_1-1-下载地址)1.1 下载地址

内测版下载入口： [通达信金融终端内测版(opens new window)](https://sns.tdx.com.cn/site/tdx_sns/page_index.html#/detail?resId=6c4c201e08844129b1c0f3f124623ad7&resType=14&uid=RL160331210204479321WHW)
正式版下载入口： [通达信金融终端64位版、通达信专业研究版(opens new window)](https://www.tdx.com.cn/soft.html)

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_1-2-登录通达信金融终端)1.2 登录通达信金融终端

![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_639d56c125ceb46e6a1719ba4a495e43_r.png)

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_1-3-系统-盘后数据下载)1.3 系统-盘后数据下载

进行日线和分钟线等数据下载
![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_8930de5bb5d39dc288970070d58aac6c_r.png)

# [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_2-使用vscode集成环境)2. 使用VSCode集成环境

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_2-1-使用vscode运行py)2.1 使用VSCode运行py

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_2-1-1-打开py文件)2.1.1 打开py文件

- 在 VS Code 中点击打开一个本地文件夹，“文件”->"打开文件夹"。
  ![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_6d836cdbbe0e8fd857a90dcb478b3127_r.png)

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_2-1-2-运行py文件)2.1.2 运行py文件

- 在VSCode中打开通达信终端目录`.../PYPlugins/user`文件夹，运行tdxdata_test.py文件。
  ![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_05fe551c426523752a860b08389247fe_r.png)

**注意：客户端安装目录下面的`.../PYPlugins/user`文件夹中的`tqcenter.py`是最主要的TQData支撑文件，请勿修改或删除，否则需要重新下载。**

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_2-2-使用vscode编辑新文件)2.2 使用VSCode编辑新文件

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_2-2-1-新建py文件)2.2.1 新建py文件

在打开的文件夹中鼠标右键创建新的".py" python 文件，文件名例如tdxdemo.py。
![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_0526f3435990c820405d8a5b979cf34b_r.png)

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1d00kk3jsibbc.html#_2-2-2-编辑py文件)2.2.2 编辑py文件

```python
# 使用tqcenter的API函数查看平安银行日线数据示例
from tqcenter import tq

#初始化
tq.initialize(__file__) #所有策略连接通达信客户端都必须调用此函数进行初始化

#获取平安银行日线前复权收盘数据
df = tq.get_market_data(
        field_list = ['Close'],
        stock_list = ["000001.SZ"],
        start_time = '20251219',
        end_time = '20251225',
        dividend_type='front',
        period='1d',
    )
print(df)
```

- 运行结果如图：
  ![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_24c2cbd40590dbf30bf4401028ab29bb_r.png)







# 快速开始第一个策略

一个完整选股入自定义板块策略只需要两步:

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1cv7o3nje2gu8.html#第一步-客户端新增自定义板块)第一步：客户端新增自定义板块

![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_7f2f39c8b0aa6318eb7c7a26efe0beed_r.png)

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1cv7o3nje2gu8.html#第二步-在vscode里面运行以下python代码)第二步：在VSCode里面运行以下python代码

实现运行函数：在这个策略里, 我们会根据运行结果做出相应操作:

```python
# 策略说明：如果运行时间点价格高出昨收5%, 则进入涨幅选股板块，否则清空该板块
import pandas as pd
import numpy as np
from datetime import datetime
from tqcenter import tq 

# 初始化tq
tq.initialize(__file__)

# 1. 基础配置
batch_codes = tq.get_stock_list_in_sector('通达信88')     # 目标板块
start_time = "20251025"                                  # 数据起始日期
target_end = datetime.now().strftime("%Y%m%d")           # 数据结束日期（当前日期）
target_gain = 5.0                                        # 目标涨幅（%），可修改
target_block_name = 'ZFXG'                               # 目标自定义板块简称

# 2. 获取并整理收盘价数据
df_real = tq.get_market_data(
    field_list=['Close'],
    stock_list=batch_codes,
    start_time=start_time,
    end_time=target_end,
    dividend_type='front',  # 前复权
    period='1d',            # 日线
    fill_data=True          # 填充缺失数据
)
# 转换为「日期×股票代码」的收盘价宽表
close_df = tq.price_df(df_real, 'Close', column_names=batch_codes)

# 3. 核心：计算当日相较于昨日的涨幅（%）
# 昨日收盘价（向下平移1行）
prev_close = close_df.shift(1)
# 计算涨幅：(当日收盘价 - 昨日收盘价) / 昨日收盘价 × 100%
daily_gain = (close_df - prev_close) / prev_close * 100

# 4. 筛选符合条件的股票（最新交易日涨幅超target_gain%）
latest_date = daily_gain.index[-1]              # 最新交易日
latest_daily_gain = daily_gain.loc[latest_date] # 每只股票最新交易日的涨幅
# 筛选条件：涨幅 > target_gain%（排除NaN，避免数据异常）
target_stocks = latest_daily_gain[latest_daily_gain > target_gain].sort_values(ascending=False)
target_stocks_list = target_stocks.index.tolist()  # 提取符合条件的股票代码列表

# 5. 结果输出与自定义板块操作（可按需注释）
print(f"\n=== 筛选结果（当日涨幅＞{target_gain}%）===")
if not target_stocks.empty:
    # ===================== 模块1：打印筛选结果 =====================
    print("【模块1：打印筛选结果】")
    print(f"符合条件的股票共 {len(target_stocks)} 只：")
    print(f"{'股票代码':<12} {'昨日收盘价':<12} {'当日收盘价':<12} {'当日涨幅':<10}")
    print("-" * 50)
    for stock_code, gain in target_stocks.items():
        prev_price = prev_close.loc[latest_date, stock_code]
        curr_price = close_df.loc[latest_date, stock_code]
        print(f"{stock_code:<12} {prev_price:<12.2f} {curr_price:<12.2f} {gain:<.2f}%")
    print("-" * 50)

    # ===================== 模块2：添加至自定义板块 =====================
    try:
        print("【模块2：自定义板块操作】")
        tq.send_user_block(block_code=target_block_name, stocks=target_stocks_list, show=True)
        print(f"✅ 已成功将股票添加至自定义板块「{target_block_name}」")
    except Exception as e:
        print(f"❌ 添加自定义板块失败：{e}")
    print("-" * 50)



else:
    # ===================== 模块1：打印空结果 =====================
    print("【模块1：打印筛选结果】")
    print(f"暂无当日涨幅＞{target_gain}%的股票")
    print("-" * 50)

    # ===================== 模块2：清空自定义选板块 =====================
    try:
        print("【模块2：自定义板块操作】")
        tq.send_user_block(block_code=target_block_name, stocks=[],show=True)
        print(f"✅ 已清空自定义板块「{target_block_name}」")
    except Exception as e:
        print(f"❌ 清空自定义板块失败：{e}")
    print("-" * 50)
```

## [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1cv7o3nje2gu8.html#结果示例)结果示例

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1cv7o3nje2gu8.html#vscode端)VSCode端

![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_f081ebd51243016c9cec69470d7b482b_r.png)

### [#](https://help.tdx.com.cn/quant/docs/markdown/mindoc-1cfsjkbf8f3is/mindoc-1cv7o3nje2gu8.html#通达信终端)通达信终端

![img](https://help.tdx.com.cn/quant/uploads/mindoc/images/m_a31e72f1df374561289662d227a3b8c9_r.png)
