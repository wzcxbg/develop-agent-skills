---
name: miniqmt-quant-dev
description: MiniQMT / XtQuant Python 量化开发辅助技能。用户询问 MiniQMT、QMT、XtQuant、xtdata、xttrader、行情接口、交易接口、账号/委托/持仓查询、信用交易或本地 MiniQMT 官方文档时使用。
---

# MiniQMT 量化开发辅助

使用本技能回答 MiniQMT / XtQuant 开发问题，并辅助编写或审查使用 `xtquant.xtdata`、`xtquant.xttrader` 的 Python 代码。

## 文档优先级

默认优先使用简版文档；当简版没有覆盖、用户明确需要 Level2/期货/CTP 内容，或需要核对完整官方说明时，再读取官方原文。

1. 行情、历史 K 线、本地数据、财务数据、板块、合约基础信息：优先读 [references/concise/xtdata-concise.md](references/concise/xtdata-concise.md)。
2. 交易连接、下单撤单、资产/委托/成交/持仓查询、信用交易、回调：优先读 [references/concise/xttrader-concise.md](references/concise/xttrader-concise.md)。
3. 简版缺少的信息、被刻意删除的 Level2 行情、期货/CTP、更新日志或完整字段表：读 [references/official/xtdata.md](references/official/xtdata.md) 或 [references/official/xttrader.md](references/official/xttrader.md)。

## 快速路由

- 行情订阅与获取：`subscribe_quote`、`subscribe_quote2`、`subscribe_whole_quote`、`get_market_data`、`get_local_data`、`get_full_tick`，读 `xtdata-concise.md` 的“行情接口”。
- 历史数据下载：`download_history_data`、`download_history_data2`，读 `xtdata-concise.md` 的“行情接口”。
- 财务数据：`get_financial_data`、`download_financial_data`、`download_financial_data2`，读 `xtdata-concise.md` 的“财务数据接口”。
- 基础行情信息：合约详情、合约类型、交易日、板块、自定义板块、指数成分权重，读 `xtdata-concise.md` 的“基础行情信息”。
- 交易环境与连接：`XtQuantTrader`、回调类、`start`、`connect`、`stop`、`run_forever`，读 `xttrader-concise.md` 的“系统设置接口”。
- 股票交易：`order_stock`、`order_stock_async`、`cancel_order_stock`、`cancel_order_stock_async`，读 `xttrader-concise.md` 的“操作接口”。
- 账号查询：资产、委托、成交、持仓、账号信息、股东账户，读 `xttrader-concise.md` 的“股票查询接口”和“其他查询接口”。
- 信用交易查询：信用资产、负债合约、融资融券标的、可融券数据、担保品，读 `xttrader-concise.md` 的“信用查询接口”。
- 回调处理：连接状态、资产、委托、成交、持仓、下单/撤单错误、异步下单回报，读 `xttrader-concise.md` 的“回调类”。

## 使用准则

- 回答 MiniQMT 代码问题时，优先给出可运行的最小片段，并提醒用户按本地 MiniQMT 安装路径、账号类型和交易权限调整。
- 对行情问题，说明是否需要先下载/订阅数据，以及返回值通常是 `dict`、`DataFrame`、`ndarray` 或对象列表。
- 对交易问题，区分同步接口返回值和异步接口回调；不要在不了解用户账户权限时假设可以真实下单。
- 如果问题涉及 Level2 行情、逐笔、千档盘口、全速盘口、期货持仓统计、CTP 资金内转或期货/期权专用常量，直接查官方原文。
- 回答时说明具体 API 名称、必要导入、关键参数、返回结构和常见失败点。
- 除非用户明确说明已有相关权限，否则不要默认其拥有 Level2 行情权限或期货/CTP 交易支持。

## 文档维护原则

`references/official/` 下的文件复制自 MiniQMT 官方文档，必须保持原样，方便以后直接替换升级。

`references/concise/` 下的文件是一次性生成的简版文档，刻意删除了更新日志、较少使用的权限专属内容和期货专属内容，方便 AI 优先加载最相关的信息。
