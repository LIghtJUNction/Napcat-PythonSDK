# NapCat API 测试备忘录

## 测试环境信息
- 测试日期：2025年4月18日
- 测试用户QQ：2418701971
- API文档参考：https://napcat.apifox.cn/llms.txt

机器人qq：3481455217
超级管理员qq：2418701971

## 配置信息
- 默认端口配置：
  - HTTP_CLIENT: 10143
  - HTTP_SSE_CLIENT: 10144
  - WS_CLIENT: 10145
  - HTTP_SERVER: 10146
  - WS_SERVER: 10147
- 测试用token：与对应端口号相同


特别注意，端口全部开放
禁止模拟客户端，而是直接连接到服务器端口进行测试

## 测试项目
1. HTTP 客户端测试
   - 基本连接 
   - 消息发送功能 
   - 事件接收功能 

2. WebSocket 客户端测试
   - 连接与重连机制 
   - 消息发送功能 
   - 事件监听功能 
   - 消息解析工具 

3. 高级封装功能测试
   - 消息构建工具 
   - 事件处理装饰器
   - 便捷消息发送方法
   
4. 全面API覆盖测试
   - 基础消息API 
   - 特殊消息类型 
   - 群组管理API 
   - 用户信息API 
   - 文件操作API 
   - 消息解析工具 

## 测试进度记录
- [x] 创建HTTP客户端测试脚本
- [x] 创建WebSocket客户端测试脚本
- [x] 创建高级API功能测试脚本
- [x] 执行并验证HTTP客户端功能
- [x] 执行并验证WebSocket客户端功能
- [x] 执行高级API功能测试脚本
- [x] 创建全面API覆盖测试脚本
- [x] 执行全面API覆盖测试
- [x] 验证API端点完整性
- [x] 完善未实现的API方法
- [x] 创建NapCat封装测试脚本
- [x] 验证消息构建工具的封装正确性
- [x] 验证客户端工厂方法的封装
- [x] 测试事件处理系统

## 测试结果
等待测试

1. NapCat封装测试
   - MessageBuilder类链式调用功能正常
   - 所有消息段类型工作正常
   - 客户端工厂方法正确创建对应类型的客户端
   - 事件过滤与分发机制工作正常
   - 消息构建与客户端集成测试通过

## 解决的问题
- 修复了消息构建器在处理复杂消息时的问题
- 增强了各种消息段类型的类型检查和验证
- 修复了事件处理系统中事件分发的问题
- 完善了消息段接口的一致性

## 注意事项
- 在创建WebSocket客户端时需确保正确处理连接超时
- 发送图片、视频等资源类型消息时应正确设置文件路径
- 消息构建工具支持链式调用，但需注意顺序

## 新一轮测试计划
- 添加更多边缘案例测试，如超大消息、特殊字符处理等
- 增加性能测试，特别是高并发消息处理场景
- 添加网络错误恢复和重试机制测试


# NapCat

## Docs
- [NapCat 接口文档](https://napcat.apifox.cn/5430207m0.md): 
- [账号相关](https://napcat.apifox.cn/54405734f0.md): 
- [消息相关](https://napcat.apifox.cn/54406081f0.md): 
- 消息相关 [发送群聊消息](https://napcat.apifox.cn/43942125f0.md): 
- 消息相关 [发送私聊消息](https://napcat.apifox.cn/43942137f0.md): 
- [群聊相关](https://napcat.apifox.cn/54406088f0.md): 
- [文件相关](https://napcat.apifox.cn/54405744f0.md): 
- [密钥相关](https://napcat.apifox.cn/54407705f0.md): 
- [系统操作](https://napcat.apifox.cn/54407785f0.md): 

## API Docs
- 账号相关 [设置账号信息](https://napcat.apifox.cn/226657374e0.md): 
- 账号相关 [获取推荐好友/群聊卡片](https://napcat.apifox.cn/226658965e0.md): 
- 账号相关 [发送戳一戳](https://napcat.apifox.cn/250286923e0.md): 
- 账号相关 [获取当前账号在线客户端列表](https://napcat.apifox.cn/226657379e0.md): 
- 账号相关 [设置消息已读](https://napcat.apifox.cn/226657389e0.md): 
- 账号相关 [获取推荐群聊卡片](https://napcat.apifox.cn/226658971e0.md): 
- 账号相关 [设置在线状态](https://napcat.apifox.cn/226658977e0.md): ## 状态列表
- 账号相关 [获取好友分组列表](https://napcat.apifox.cn/226658978e0.md): 
- 账号相关 [设置头像](https://napcat.apifox.cn/226658980e0.md): 
- 账号相关 [点赞](https://napcat.apifox.cn/226656717e0.md): 
- 账号相关 [设置私聊已读](https://napcat.apifox.cn/226659165e0.md): 
- 账号相关 [设置群聊已读](https://napcat.apifox.cn/226659167e0.md): 
- 账号相关 [创建收藏](https://napcat.apifox.cn/226659178e0.md): 
- 账号相关 [处理好友请求](https://napcat.apifox.cn/226656932e0.md): 
- 账号相关 [设置个性签名](https://napcat.apifox.cn/226659186e0.md): 
- 账号相关 [获取登录号信息](https://napcat.apifox.cn/226656952e0.md): 
- 账号相关 [最近消息列表](https://napcat.apifox.cn/226659190e0.md): 获取的最新消息是每个会话最新的消息
- 账号相关 [获取账号信息](https://napcat.apifox.cn/226656970e0.md): 
- 账号相关 [获取好友列表](https://napcat.apifox.cn/226656976e0.md): 
- 账号相关 [_设置所有消息已读](https://napcat.apifox.cn/226659194e0.md): 
- 账号相关 [获取点赞列表](https://napcat.apifox.cn/226659197e0.md): 
- 账号相关 [获取收藏表情](https://napcat.apifox.cn/226659210e0.md): 
- 账号相关 [删除好友](https://napcat.apifox.cn/227237873e0.md): 
- 账号相关 [_获取在线机型](https://napcat.apifox.cn/227233981e0.md): 
- 账号相关 [_设置在线机型](https://napcat.apifox.cn/227233993e0.md): 
- 账号相关 [获取用户状态](https://napcat.apifox.cn/226659292e0.md): 
- 账号相关 [获取状态](https://napcat.apifox.cn/226657083e0.md): 
- 账号相关 [获取小程序卡片](https://napcat.apifox.cn/227738594e0.md): 
- 账号相关 [获取单向好友列表](https://napcat.apifox.cn/266151878e0.md): 
- 账号相关 [设置自定义在线状态](https://napcat.apifox.cn/266151905e0.md): 
- 消息相关 > 发送群聊消息 [发送群文本](https://napcat.apifox.cn/226799128e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群艾特](https://napcat.apifox.cn/226832594e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群图片](https://napcat.apifox.cn/226857476e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群系统表情](https://napcat.apifox.cn/226855594e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群JSON](https://napcat.apifox.cn/226867165e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群语音](https://napcat.apifox.cn/226868634e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群视频](https://napcat.apifox.cn/226872680e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群回复](https://napcat.apifox.cn/226858810e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群聊音乐卡片](https://napcat.apifox.cn/228099094e0.md): 
- 消息相关 > 发送群聊消息 [发送群聊超级表情 骰子](https://napcat.apifox.cn/228097721e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群聊超级表情 猜拳](https://napcat.apifox.cn/228097933e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [发送群合并转发消息](https://napcat.apifox.cn/226657396e0.md): 
- 消息相关 > 发送群聊消息 [发送群文件](https://napcat.apifox.cn/244510830e0.md): 发送群消息
- 消息相关 > 发送群聊消息 [消息转发到群](https://napcat.apifox.cn/226659074e0.md): 
- 消息相关 > 发送群聊消息 [发送群聊戳一戳](https://napcat.apifox.cn/226659265e0.md): 
- 消息相关 > 发送群聊消息 [发送群聊自定义音乐卡片](https://napcat.apifox.cn/228099151e0.md): 
- 消息相关 > 发送私聊消息 [发送私聊文本](https://napcat.apifox.cn/226888843e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊图片](https://napcat.apifox.cn/226889234e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊系统表情](https://napcat.apifox.cn/226889538e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊JSON](https://napcat.apifox.cn/226889555e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊语音](https://napcat.apifox.cn/226889604e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊视频](https://napcat.apifox.cn/226889623e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊回复](https://napcat.apifox.cn/226889308e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊音乐卡片](https://napcat.apifox.cn/228099194e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊自定义音乐卡片](https://napcat.apifox.cn/228099213e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊超级表情 骰子](https://napcat.apifox.cn/228097912e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊超级表情 猜拳](https://napcat.apifox.cn/228098500e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊合并转发消息](https://napcat.apifox.cn/226657399e0.md): 
- 消息相关 > 发送私聊消息 [消息转发到私聊](https://napcat.apifox.cn/226659051e0.md): 
- 消息相关 > 发送私聊消息 [发送私聊文件](https://napcat.apifox.cn/244510838e0.md): 发送群消息
- 消息相关 > 发送私聊消息 [发送私聊戳一戳](https://napcat.apifox.cn/226659255e0.md): 
- 消息相关 [撤回消息](https://napcat.apifox.cn/226919954e0.md): 
- 消息相关 [获取群历史消息](https://napcat.apifox.cn/226657401e0.md): 
- 消息相关 [获取消息详情](https://napcat.apifox.cn/226656707e0.md): 
- 消息相关 [获取合并转发消息](https://napcat.apifox.cn/226656712e0.md): 
- 消息相关 [贴表情](https://napcat.apifox.cn/226659104e0.md): 
- 消息相关 [获取好友历史消息](https://napcat.apifox.cn/226659174e0.md): 
- 消息相关 [获取贴表情详情](https://napcat.apifox.cn/226659219e0.md): 
- 消息相关 [发送合并转发消息](https://napcat.apifox.cn/226659136e0.md): 
- 消息相关 [获取语音消息详情](https://napcat.apifox.cn/226657058e0.md): 
- 消息相关 [获取图片消息详情](https://napcat.apifox.cn/226657066e0.md): 
- 消息相关 [发送群AI语音](https://napcat.apifox.cn/229486774e0.md): 
- 群聊相关 [设置群备注](https://napcat.apifox.cn/283136268e0.md): 
- 群聊相关 [群踢人](https://napcat.apifox.cn/226656748e0.md): 
- 群聊相关 [获取群系统消息](https://napcat.apifox.cn/226658660e0.md): 
- 群聊相关 [群禁言](https://napcat.apifox.cn/226656791e0.md): 
- 群聊相关 [获取群精华消息](https://napcat.apifox.cn/226658664e0.md): 
- 群聊相关 [全体禁言](https://napcat.apifox.cn/226656802e0.md): 
- 群聊相关 [设置群头像](https://napcat.apifox.cn/226658669e0.md): 
- 群聊相关 [设置群管理](https://napcat.apifox.cn/226656815e0.md): 
- 群聊相关 [设置群成员名片](https://napcat.apifox.cn/226656913e0.md): 
- 群聊相关 [设置群精华消息](https://napcat.apifox.cn/226658674e0.md): 
- 群聊相关 [设置群名](https://napcat.apifox.cn/226656919e0.md): 
- 群聊相关 [删除群精华消息](https://napcat.apifox.cn/226658678e0.md): 
- 群聊相关 [退群](https://napcat.apifox.cn/226656926e0.md): 
- 群聊相关 [_发送群公告](https://napcat.apifox.cn/226658740e0.md): 
- 群聊相关 [设置群头衔](https://napcat.apifox.cn/226656931e0.md): 
- 群聊相关 [_获取群公告](https://napcat.apifox.cn/226658742e0.md): 
- 群聊相关 [处理加群请求](https://napcat.apifox.cn/226656947e0.md): 
- 群聊相关 [获取群信息](https://napcat.apifox.cn/226656979e0.md): 
- 群聊相关 [获取群列表](https://napcat.apifox.cn/226656992e0.md): 
- 群聊相关 [_删除群公告](https://napcat.apifox.cn/226659240e0.md): 
- 群聊相关 [获取群成员信息](https://napcat.apifox.cn/226657019e0.md): 
- 群聊相关 [获取群成员列表](https://napcat.apifox.cn/226657034e0.md): 
- 群聊相关 [获取群荣誉](https://napcat.apifox.cn/226657036e0.md): 
- 群聊相关 [获取群信息ex](https://napcat.apifox.cn/226659229e0.md): 
- 群聊相关 [获取群 @全体成员 剩余次数](https://napcat.apifox.cn/227245941e0.md): 
- 群聊相关 [获取群禁言列表](https://napcat.apifox.cn/226659300e0.md): 
- 群聊相关 [获取群过滤系统消息](https://napcat.apifox.cn/226659323e0.md): 
- 群聊相关 [群打卡](https://napcat.apifox.cn/226659329e0.md): 
- 群聊相关 [群打卡](https://napcat.apifox.cn/230897177e0.md): 
- 文件相关 [移动群文件](https://napcat.apifox.cn/283136359e0.md): 
- 文件相关 [转存为永久文件](https://napcat.apifox.cn/283136366e0.md): 
- 文件相关 [重命名群文件](https://napcat.apifox.cn/283136375e0.md): 
- 文件相关 [获取文件信息](https://napcat.apifox.cn/226658985e0.md): 
- 文件相关 [上传群文件](https://napcat.apifox.cn/226658753e0.md): 
- 文件相关 [创建群文件文件夹](https://napcat.apifox.cn/226658773e0.md): 
- 文件相关 [删除群文件](https://napcat.apifox.cn/226658755e0.md): 
- 文件相关 [删除群文件夹](https://napcat.apifox.cn/226658779e0.md): 
- 文件相关 [上传私聊文件](https://napcat.apifox.cn/226658883e0.md): 
- 文件相关 [获取群文件系统信息](https://napcat.apifox.cn/226658789e0.md): 
- 文件相关 [下载文件到缓存目录](https://napcat.apifox.cn/226658887e0.md): 
- 文件相关 [获取群根目录文件列表](https://napcat.apifox.cn/226658823e0.md): 
- 文件相关 [获取群子目录文件列表](https://napcat.apifox.cn/226658865e0.md): 
- 文件相关 [获取群文件链接](https://napcat.apifox.cn/226658867e0.md): 
- 文件相关 [获取私聊文件链接](https://napcat.apifox.cn/266151849e0.md): 
- 密钥相关 [获取clientkey](https://napcat.apifox.cn/250286915e0.md): 
- 密钥相关 [获取cookies](https://napcat.apifox.cn/226657041e0.md): 
- 密钥相关 [获取 CSRF Token](https://napcat.apifox.cn/226657044e0.md): 
- 密钥相关 [获取 QQ 相关接口凭证](https://napcat.apifox.cn/226657054e0.md): 
- 密钥相关 [nc获取rkey](https://napcat.apifox.cn/226659297e0.md): 
- 密钥相关 [获取rkey](https://napcat.apifox.cn/283136230e0.md): 
- 密钥相关 [获取rkey服务](https://napcat.apifox.cn/283136236e0.md): 
- 个人操作 [OCR 图片识别](https://napcat.apifox.cn/226658231e0.md): 
- 个人操作 [.OCR 图片识别](https://napcat.apifox.cn/226658234e0.md): 
- 个人操作 [英译中](https://napcat.apifox.cn/226659102e0.md): 
- 个人操作 [设置输入状态](https://napcat.apifox.cn/226659225e0.md): ## 状态列表
- 个人操作 [.对事件执行快速操作](https://napcat.apifox.cn/226658889e0.md): 相当于http的快速操作
- 个人操作 [检查是否可以发送图片](https://napcat.apifox.cn/226657071e0.md): 
- 个人操作 [检查是否可以发送语音](https://napcat.apifox.cn/226657080e0.md): 
- 个人操作 [获取AI语音人物](https://napcat.apifox.cn/229485683e0.md): 
- 个人操作 [获取AI语音](https://napcat.apifox.cn/229486818e0.md): 
- 系统操作 [获取机器人账号范围](https://napcat.apifox.cn/226658975e0.md): 
- 系统操作 [账号退出](https://napcat.apifox.cn/283136399e0.md): 
- 系统操作 [发送自定义组包](https://napcat.apifox.cn/250286903e0.md): 
- 系统操作 [获取packet状态](https://napcat.apifox.cn/226659280e0.md): 
- 系统操作 [获取版本信息](https://napcat.apifox.cn/226657087e0.md): 
- 其他 > 保留 [send_private_msg](https://napcat.apifox.cn/226656553e0.md): 
- 其他 > 保留 [send_group_msg](https://napcat.apifox.cn/226656598e0.md): 发送群消息
- 其他 > 保留 [send_msg](https://napcat.apifox.cn/226656652e0.md): 
- 其他 > 接口 [unknown](https://napcat.apifox.cn/226658925e0.md): 
- 其他 > 接口 [get_guild_list](https://napcat.apifox.cn/226659311e0.md): 
- 其他 > 接口 [get_guild_service_profile](https://napcat.apifox.cn/226659317e0.md): 
- 其他 > 接口 [检查链接安全性](https://napcat.apifox.cn/228534361e0.md): 
- 其他 > 接口 [点击按钮](https://napcat.apifox.cn/266151864e0.md): 
- 其他 > bug [获取收藏列表](https://napcat.apifox.cn/226659182e0.md): 
- 其他 > bug [获取被过滤的加群请求](https://napcat.apifox.cn/226659234e0.md): 
- 其他 > bug [fetch_user_profile_like](https://napcat.apifox.cn/226659254e0.md): 
- 其他 > bug [获取中文分词](https://napcat.apifox.cn/228534368e0.md):