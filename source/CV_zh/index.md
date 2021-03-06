---
title: lxw_Resume_zh.md
date: 2018-03-05 18:00:00
---
# 刘晓伟 简历

**通信地址:** 北京市海淀区中关村南四街四号中科院软件园4号楼(100190)  
**性别:** 男&emsp;&emsp;**Tel:** (+86)131-2672-6993&emsp;&emsp;**Email:** liu_xiaowei@foxmail.com  
**GitHub:** [https://github.com/lxw0109](https://github.com/lxw0109)  


### 教育经历
|  |  |  |  |
| - | - | - | - |
| 2013-2016 | 中国科学院 | 计算机网络信息中心 | 硕士&nbsp;(保送) |
| 2009-2013 | 吉林大学 | 计算机科学与技术学院 | 学士&nbsp;(top 5%) |
|  |  |  |  |


### 工作经历
|  |  |  |  |
| - | - | - | - |
| 2016.7-至今 | 中国科学院软件研究所 | 协同创新中心 | 软件研发工程师, 自然语言处理工程师 |
| 2015.2-2015.3 | 百度 | 系统部 | 系统研发(CDN)工程师(**实习**) |
| 2012.10-2013.8 | SIMI科技有限公司 | 研发部 | 软件研发工程师(**实习**) |
|  |  |  |  |


### 开源项目学习
[solving_captchas_code_examples](https://github.com/lxw0109/ML-Experiments/tree/master/CAPTCHA/solving_captchas_code_examples)&emsp;&emsp;[pdf_table_extract](https://github.com/ashima/pdf-table-extract)&emsp;&emsp;[threadpool](https://github.com/SpotlightKid/threadpool)


### 专业技能
+ 熟悉Python, 熟悉Shell脚本编程
+ 熟练使用Linux, Git, Vim
+ 熟悉常用的算法和数据结构
+ 熟悉计算机网络, TCP/IP协议, 网络爬虫(scrapy, requests)
+ 熟练使用MongoDB, MySQL, Redis
+ 通过CET-6, 能够快速查阅英文资料, 具备良好的听说读写译能力
+ 熟悉常用的机器学习算法, 熟悉 pandas, numpy, scikit-learn 等机器学习库, 会用 Keras 深度学习框架


### 项目经验
+ **Sentiment Analysis on Movie Reviews&nbsp;&nbsp;&nbsp;2018.05-2018.06&nbsp;&nbsp;&nbsp;关键技术: Python, word2vec, Keras, LSTM, RF**  
**项目简介**: 基于电影评论数据的多类别情感分析任务. 共156,060条标注数据, 每条标注数据包含短语内容以及该短语所属的情感类别(共五个等级). 本项目完成了基于 LSTM、随机森林等多分类算法模型的实现  
**本人工作**:  
1. 数据预处理: 进行样本均衡性统计、缺失值统计、停用词去除、样本去重等预处理操作
2. 数据准备: 通过使用Google News 预训练词向量模型, 获取短语中每个词的词向量, 并构建短语向量作为模型的输入数据; 将五个等级的情感类别进行离散化处理, 作为模型的输出数据(训练标签)
3. 模型训练和评估: 使用 LSTM、随机森林算法构建多分类模型, 并使用处理的数据进行模型的训练和评估
4. 模型调优: 短语向量的优化: 使用词向量矩阵的形式表示短语, 而不是各个词的向量和求平均, 测试集准确率由58.64%提升至 62.89%; 停用词表的调整: snownlp 的英文停用词表中包含 cannot, never, always, awfully, really 等否定词和程度副词，去除这些词语对情感分类的准确率影响较大, 调整后测试集准确率进一步提升至 65.14% (排名前 15%)

+ **基于 LSTM, RF 等算法的股票涨跌预测&nbsp;&nbsp;&nbsp;2017.12 - 2018.02&nbsp;&nbsp;&nbsp;关键技术: Python, Keras, LSTM, RF**  
**项目简介**: 针对数据量有限的股票交易数据进行特征提取、特征选择, 构建基于 LSTM 等算法的股票涨跌预测模型, 为金融领域提供股票筛选和时机选择服务.  
**本人工作**:  
1. 数据获取: 通过 Tushare 股票数据接口, 获取股票历史交易数据(包括开盘价、收盘价等六个基本特征)并进行预处理, 作为模型的输入数据; 计算未来五日收益率涨跌并进行离散化处理, 作为监督学习模型的标签数据
2. 模型训练: 模型的每个训练样本为时间窗口(调参确定最优值为 20)内的六个基本特征所形成的矩阵, 样本数量采用2000 年以来共 4400 条交易数据; 通过时间窗口的滑动形成时间序列数据, 并传入 LSTM 模型进行训练
3. 模型评估: 测试模型在训练集和验证集上的准确率, 模型调优前在训练集上的准确率仅有 55.85% (欠拟合)
4. 模型调优: 增加情感特征, 并重新训练和评估模型, 训练集准确率由 55.85%提升至 62.04%, 验证集准确率由 53.26%提升至58.04%; 增加历史收益率特征(通过五日前开盘价和当日收盘价计算得到), 并重新训练和评估模型, 训练集准确率进一步提升至 74.68%, 验证集准确率进一步提升至 66.55%

+ **嗅金牛智能投研平台&nbsp;&nbsp;&nbsp;2016.07 - 2017.07&nbsp;&nbsp;&nbsp;关键技术: Python, numpy, Redis, scrapy, LVS**  
**项目简介**: 嗅金牛是一个针对国内 A 股上市公司的数据服务平台, 为用户提供企业数据查询、企业数据推送、智能投资研究等金融信息服务  
**本人工作**:  
1. PDF 表格数据解析: 基于开源的 PDF 表格解析项目进行重构和优化, 新增同一页内不同表格的切割、彩色表格解析、跨行跨列表格解析等功能
2. 数据抓取(架构设计、实现和优化): 基于 IP 代理、请求 Header 伪造、多线程、消息队列等技术完成中国知网、裁判文书网、天眼查等网站数据的抓取
3. 使用 ThinkPHP 框架完成网站的后端开发, 完成网站的部署(Nginx)并实现负载均衡(LVS)

### 科研成果
**学术论文**:
+ RPKI Deployment Risks and Solutions
+ RPKI中CA资源分配风险及防护技术研究

**专利**:
+ 一种加强RPKI中CA证书签发安全的事前控制方法
+ 一种基于区域识别与分割的PDF表格数据解析方法
