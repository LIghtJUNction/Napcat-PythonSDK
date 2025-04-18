# -*- coding: utf-8 -*-
from enum import Enum
# region ActionType
class ActionType(Enum):
    """API动作类型枚举"""
    # 消息相关
    SEND_PRIVATE_MSG = "send_private_msg"
    SEND_GROUP_MSG = "send_group_msg"
    SEND_MSG = "send_msg"
    DELETE_MSG = "delete_msg"
    GET_MSG = "get_msg"
    GET_FORWARD_MSG = "get_forward_msg"
    SEND_LIKE = "send_like"
    SEND_PRIVATE_FORWARD_MSG = "send_private_forward_msg"
    SEND_GROUP_FORWARD_MSG = "send_group_forward_msg"
    
    # 群组管理
    SET_GROUP_KICK = "set_group_kick"
    SET_GROUP_BAN = "set_group_ban"
    SET_GROUP_ANONYMOUS_BAN = "set_group_anonymous_ban"
    SET_GROUP_WHOLE_BAN = "set_group_whole_ban"
    SET_GROUP_ADMIN = "set_group_admin"
    SET_GROUP_ANONYMOUS = "set_group_anonymous"
    SET_GROUP_CARD = "set_group_card"
    SET_GROUP_NAME = "set_group_name"
    SET_GROUP_LEAVE = "set_group_leave"
    SET_GROUP_SPECIAL_TITLE = "set_group_special_title"
    
    # 好友相关
    FRIEND_POKE = "send_friend_poke"
    GROUP_POKE = "send_group_poke"
    DELETE_FRIEND = "delete_friend"
    
    # 请求处理
    SET_FRIEND_ADD_REQUEST = "set_friend_add_request"
    SET_GROUP_ADD_REQUEST = "set_group_add_request"
    
    # 信息获取
    GET_LOGIN_INFO = "get_login_info"
    GET_STRANGER_INFO = "get_stranger_info"
    GET_FRIEND_LIST = "get_friend_list"
    GET_GROUP_INFO = "get_group_info"
    GET_GROUP_LIST = "get_group_list"
    GET_GROUP_MEMBER_INFO = "get_group_member_info"
    GET_GROUP_MEMBER_LIST = "get_group_member_list"
    GET_GROUP_HONOR_INFO = "get_group_honor_info"
    
    # 文件操作
    UPLOAD_GROUP_FILE = "upload_group_file"
    DELETE_GROUP_FILE = "delete_group_file"
    GET_GROUP_FILE_SYSTEM_INFO = "get_group_file_system_info"
    
    # 系统相关
    GET_STATUS = "get_status"
    GET_VERSION_INFO = "get_version_info"
    SET_RESTART = "set_restart"
    CLEAN_CACHE = "clean_cache"
    
    # 扩展功能
    CAN_SEND_IMAGE = "can_send_image"
    CAN_SEND_RECORD = "can_send_record"
    OCR_IMAGE = "ocr_image"
    GET_WORD_SLICES = "get_word_slices"
    
    # QQ频道相关
    GET_GUILD_SERVICE_PROFILE = "get_guild_service_profile"
    GET_GUILD_LIST = "get_guild_list"
    GET_CHANNEL_LIST = "get_channel_list"
    GET_CHANNEL_INFO = "get_channel_info"
    
    @classmethod
    def from_string(cls, action_name: str) -> "ActionType":
        """
        从字符串获取动作类型枚举
        
        :param action_name: 动作名称字符串
        :return: 对应的ActionType枚举值
        :raise ValueError: 如果找不到对应的动作类型
        """
        for action in cls:
            if action.value == action_name:
                return action
        raise ValueError(f"未知的动作类型: {action_name}")
    
    @classmethod
    def is_valid(cls, action_name: str) -> bool:
        """
        检查动作名称是否有效
        
        :param action_name: 动作名称字符串
        :return: 是否是有效的动作类型
        """
        try:
            _ = cls.from_string(action_name)
            return True
        except ValueError:
            return False
