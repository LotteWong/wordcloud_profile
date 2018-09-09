# wordcloud_profile  
---  

#### 项目介绍
该脚本可实现登录微信后自动**爬取头像和信息**，并自动**生成对应的词云头像**。  

#### 包含文件
- `wordcloud_profile.py` PY文件
- `PingFang-W1.ttc` 字体文件

#### 实现原理
1. **爬取头像和信息**：详细参考 `itchat` 的模块文档
2. **生成对应的词云头像**：
   - 先使用 `jieba` 模块进行 **中文分词**  
   - 再使用 `worldcloud` 模块进行词云的 **形状绘制**[`Wordcloud()`]、**文字填充**[`generate()`]、**图案上色**[`recolor()`]  

#### 注意事项  
- 先 `generate(cut_text)` 再 `recolor(color_func=color)`  

#### 如何运行  
1. 复制本目录下的所有文件至本地  
2. 打开相关解释器运行 `wordcloud_profile.py`即可  

#### 操作指南  
- 首次需要扫码登录，在一定时间内支持热加载即无须重复扫码登录  
- 向微信用户本人发送带有 `Hello world!` 关键词在内的文本，即可获得词云头像  
- 该脚本作用于微信端，在解释器端会显示相关操作信息  

#### Bug
- 目前仅对轮廓分明且背景为白的头像有较好的支持  
- 若用户不补充更多信息，仅依靠微信爬取的资料，词云将因语料不足而效果不佳