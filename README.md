# Napcat Python SDK

## ***介绍***

> 本项目原为AIVK项目前置 功能抽离出来供其他项目使用
> 目前正在开发中
> 设计为MCP服务

**客户端实现**

* [X] [HTTP客户端](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/src/napcat/clients/http) - 支持同步和异步请求
* [X] [SSE客户端](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/src/napcat/clients/sse/) - 支持事件流接收
* [X] [WebSocket客户端](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/src/napcat/clients/websocket/) - 支持双向实时通信

**服务端实现**

* [ ] [HTTP](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/src/napcat/severs/http/)Napcat服务器
* [ ] WebSocket 服务器

# FastNapcat

综合上述所有客户端，并优化使用体验

**已完成端点**

** account **
====================

* [ ] [ArkShareGroup.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/ArkShareGroup.py)
* [ ] [ArkSharePeer.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/ArkSharePeer.py)
* [ ] [create_collection.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/create_collection.py)
* [ ] [delete_friend.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/delete_friend.py)
* [ ] [fetch_custom_face.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/fetch_custom_face.py)
* [ ] [get_account_info.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_account_info.py)
* [ ] [get_friends_with_category.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_friends_with_category.py)
* [ ] [get_friend_group_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_friend_group_list.py)
* [ ] [get_friend_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_friend_list.py)
* [ ] [get_login_info.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_login_info.py)
* [ ] [get_mini_app_ark.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_mini_app_ark.py)
* [ ] [get_online_clients.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_online_clients.py)
* [ ] [get_profile_like.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_profile_like.py)
* [ ] [get_recent_contact.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_recent_contact.py)
* [ ] [get_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_status.py)
* [ ] [get_stranger_info.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_stranger_info.py)
* [ ] [get_unidirectional_friend_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_unidirectional_friend_list.py)
* [ ] [get_user_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_user_status.py)
* [ ] [mark_group_msg_as_read.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/mark_group_msg_as_read.py)
* [ ] [mark_msg_as_read.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/mark_msg_as_read.py)
* [ ] [mark_private_msg_as_read.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/mark_private_msg_as_read.py)
* [ ] [nc_get_user_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/nc_get_user_status.py)
* [ ] [send_like.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_like.py)
* [ ] [send_poke.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_poke.py)
* [ ] [set_custom_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_custom_status.py)
* [ ] [set_diy_online_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_diy_online_status.py)
* [ ] [set_friend_add_request.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_friend_add_request.py)
* [ ] [set_online_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_online_status.py)
* [ ] [set_qq_avatar.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_qq_avatar.py)
* [ ] [set_qq_profie.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_qq_profie.py)
* [ ] [set_self_longnick.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_self_longnick.py)
* [ ] [set_signature.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_signature.py)
* [ ] [_get_model_show.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/_get_model_show.py)
* [ ] [_mark_all_as_read.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/_mark_all_as_read.py)
* [ ] [_set_model_show.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/_set_model_show.py)
** base **
====================

* [ ] [emus.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/emus.py)
* [ ] [models.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/models.py)
* [ ] [utils.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/utils.py)
** file **
====================

* [ ] [create_group_file_folder.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/create_group_file_folder.py)
* [ ] [delete_group_file.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/delete_group_file.py)
* [ ] [delete_group_folder.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/delete_group_folder.py)
* [ ] [download_file.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/download_file.py)
* [ ] [get_file.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_file.py)
* [ ] [get_group_files_by_folder.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_files_by_folder.py)
* [ ] [get_group_file_system_info.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_file_system_info.py)
* [ ] [get_group_file_url.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_file_url.py)
* [ ] [get_group_root_files.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_root_files.py)
* [ ] [get_private_file_url.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_private_file_url.py)
* [ ] [move_group_file.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/move_group_file.py)
* [ ] [rename_group_file.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/rename_group_file.py)
* [ ] [save_to_permanent.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/save_to_permanent.py)
* [ ] [trans_group_file.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/trans_group_file.py)
* [ ] [upload_group_file.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/upload_group_file.py)
* [ ] [upload_private_file.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/upload_private_file.py)
** group **
====================

* [ ] [delete_essence_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/delete_essence_msg.py)
* [ ] [get_essence_msg_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_essence_msg_list.py)
* [ ] [get_group_at_all_remain.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_at_all_remain.py)
* [ ] [get_group_honor_info.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_honor_info.py)
* [ ] [get_group_ignored_notifies.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_ignored_notifies.py)
* [ ] [get_group_info.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_info.py)
* [ ] [get_group_info_ex.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_info_ex.py)
* [ ] [get_group_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_list.py)
* [ ] [get_group_member_info.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_member_info.py)
* [ ] [get_group_member_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_member_list.py)
* [ ] [get_group_shut_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_shut_list.py)
* [ ] [get_group_system_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_system_msg.py)
* [ ] [leave_group.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/leave_group.py)
* [ ] [send_group_sign.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_group_sign.py)
* [ ] [set_essence_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_essence_msg.py)
* [ ] [set_group_add_request.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_add_request.py)
* [ ] [set_group_admin.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_admin.py)
* [ ] [set_group_ban.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_ban.py)
* [ ] [set_group_card.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_card.py)
* [ ] [set_group_kick.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_kick.py)
* [ ] [set_group_leave.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_leave.py)
* [ ] [set_group_name.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_name.py)
* [ ] [set_group_portrait.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_portrait.py)
* [ ] [set_group_remark.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_remark.py)
* [ ] [set_group_sign.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_sign.py)
* [ ] [set_group_special_title.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_special_title.py)
* [ ] [set_group_whole_ban.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_group_whole_ban.py)
* [ ] [set_leave_group.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_leave_group.py)
* [ ] [_del_group_notice.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/_del_group_notice.py)
* [ ] [_get_group_notice.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/_get_group_notice.py)
* [ ] [_send_group_notice.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/_send_group_notice.py)
** key **
====================

* [ ] [get_clientkey.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_clientkey.py)
* [ ] [get_client_key.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_client_key.py)
* [ ] [get_cookies.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_cookies.py)
* [ ] [get_credentials.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_credentials.py)
* [ ] [get_csrf_token.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_csrf_token.py)
* [ ] [get_rkey.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_rkey.py)
* [ ] [get_rkey_server.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_rkey_server.py)
* [ ] [nc_get_rkey.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/nc_get_rkey.py)
** messages **
====================

* [ ] [delete_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/delete_msg.py)
* [ ] [fetch_emoji_like.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/fetch_emoji_like.py)
* [ ] [get_forward_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_forward_msg.py)
* [ ] [get_friend_msg_history.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_friend_msg_history.py)
* [ ] [get_group_msg_history.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_msg_history.py)
* [ ] [get_history_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_history_msg.py)
* [ ] [get_image.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_image.py)
* [ ] [get_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_msg.py)
* [ ] [get_record.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_record.py)
** group **
====================

* [ ] [send_group_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_group_msg.py)
** private **
====================

* [ ] [send_private_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_private_msg.py)
* [ ] [recall_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/recall_msg.py)
* [ ] [send_forward_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_forward_msg.py)
* [ ] [send_group_ai_record.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_group_ai_record.py)
* [ ] [send_group_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_group_msg.py)
* [ ] [send_private_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_private_msg.py)
* [ ] [set_msg_emoji_like.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_msg_emoji_like.py)
** other **
====================

** bug **
====================

* [ ] [.get_word_slices.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/.get_word_slices.py)
* [ ] [fetch_user_profile_like.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/fetch_user_profile_like.py)
* [ ] [get_collection_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_collection_list.py)
* [ ] [get_group_ignore_add_request.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_group_ignore_add_request.py)
** interface **
====================

* [ ] [check_url_safely.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/check_url_safely.py)
* [ ] [click_inline_keyboard_button.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/click_inline_keyboard_button.py)
* [ ] [get_guild_list.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_guild_list.py)
* [ ] [get_guild_service_profile.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_guild_service_profile.py)
* [ ] [unknown.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/unknown.py)
** reserve **
====================

* [ ] [send_group_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_group_msg.py)
* [ ] [send_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_msg.py)
* [ ] [send_private_msg.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_private_msg.py)
** personal **
====================

* [ ] [.handle_quick_operation.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/.handle_quick_operation.py)
* [ ] [.ocr_image.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/.ocr_image.py)
* [ ] [can_send_image.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/can_send_image.py)
* [ ] [can_send_record.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/can_send_record.py)
* [ ] [get_ai_characters.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_ai_characters.py)
* [ ] [get_ai_record.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_ai_record.py)
* [ ] [ocr_image.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/ocr_image.py)
* [ ] [set_input_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_input_status.py)
* [ ] [translate_en2zh.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/translate_en2zh.py)
** system **
====================

* [ ] [account_logout.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/account_logout.py)
* [ ] [bot_exit.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/bot_exit.py)
* [ ] [get_robot_uid_range.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_robot_uid_range.py)
* [ ] [get_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_status.py)
* [ ] [get_version.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_version.py)
* [ ] [get_version_info.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/get_version_info.py)
* [ ] [nc_get_packet_status.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/nc_get_packet_status.py)
* [ ] [send_packet.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/send_packet.py)
* [ ] [set_restart.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/set_restart.py)
* [ ] [__init__.py](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/__init__.py)


# 贡献指南

## 序言

推荐使用vscode + pyright
然后打开插件设置，进行基础设置

## 类型标注

启用严格模式
使用list代替List 而无需额外导入：from typing import List
使用dict代替Dict 而无需额外导入：from typing import Dict
使用tuple代替Tuple 而无需额外导入：from typing import Tuple
使用set代替Set 而无需额外导入：from typing import Set
使用deque代替Deque 而无需额外导入：from collections import deque
使用type代替Type 而无需额外导入：from typing import Type

使用 | None 代替 Optional
使用 | 代替 Union

## 代码注释规范

* 所有类、方法和函数都应该有文档字符串
* API类需包含完整的功能描述、接口地址、参数和返回值说明
* 复杂逻辑应添加行内注释
* 推荐使用 # region 和 # endregion 区域划分代码，方便阅读

## API开发规范

* 参考 `src/napcat/api/memo.md` 中的规范进行开发
* 所有API实现都应遵循标准API类结构
* 使用pydantic进行数据验证和序列化
* 每个API文件末尾应包含测试代码

## AI使用规范

请准备好合适的提示词
例如：llms.txt

## 不接受的PR

pyright检查不通过的PR
大量使用Any类型标注的PR
注释不清楚的PR
不符合项目编码风格的PR
缺少测试代码的PR

## 代码规范

pyright 检查通过即为规范
推荐使用 # region 区域划分代码 方便阅读
欢迎使用script/pyupgrade.py脚本 来自动化部分升级代码到python3.13规范
