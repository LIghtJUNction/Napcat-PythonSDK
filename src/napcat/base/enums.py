from enum import Enum, IntEnum
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
    


# region OLStatus
# 基本状态枚举
class OnlineStatus(IntEnum):
    ONLINE = 10  # 在线
    AWAY = 30   # 离开
    INVISIBLE = 40  # 隐身
    BUSY = 50   # 忙碌
    QME = 60    # Q我吧
    DO_NOT_DISTURB = 70  # 请勿打扰

# 扩展状态枚举
class ExtStatus(IntEnum):
    NONE = 0  # 无扩展状态
    LISTENING_MUSIC = 1028  # 听歌中
    SPRING_LIMITED = 2037  # 春日限定
    YUANMENG = 2025  # 一起元梦
    SEEKING_STAR = 2026  # 求星搭子
    DRAINED = 2014  # 被掏空
    WEATHER = 1030  # 今日天气
    CRASHED = 2019  # 我crash了
    LOVE = 2006  # 爱你
    IN_LOVE = 1051  # 恋爱中
    GOOD_LUCK = 1071  # 好运锦鲤
    RETROGRADE = 1201  # 水逆退散
    HYPED = 1056  # 嗨到飞起
    ENERGETIC = 1058  # 元气满满
    BABY_CERTIFIED = 1070  # 宝宝认证
    HARD_TO_EXPLAIN = 1063  # 一言难尽
    RARELY_CONFUSED = 2001  # 难得糊涂
    EMO = 1401  # emo中
    TOUGH = 1062  # 我太难了
    MOVED_ON = 2013  # 我想开了
    IM_FINE = 1052  # 我没事
    NEED_QUIET = 1061  # 想静静
    RELAXED = 1059  # 悠哉哉
    TRAVELING = 2015  # 去旅行
    WEAK_SIGNAL = 1011  # 信号弱
    OUT_HAVING_FUN = 2003  # 出去浪
    HOMEWORK = 2012  # 肝作业
    STUDYING = 1018  # 学习中
    WORKING = 2023  # 搬砖中
    SLACKING = 1300  # 摸鱼中
    BORED = 1060  # 无聊中
    TIMI = 1027  # timi中
    SLEEPING = 1016  # 睡觉中
    STAYING_UP = 1032  # 熬夜中
    BINGE_WATCHING = 1021  # 追剧中


























# region 状态
class 状态(Enum):
    """ 中文版在线状态枚举 
    ...
    """
    在线 = 10  # Online
    离开 = 30  # Away
    隐身 = 40  # Invisible
    忙碌 = 50  # Busy
    Q我吧 = 60  # Q我吧
    请勿打扰 = 70  # Do Not Disturb
    电量 = 1000  # Battery Status
    信号弱 = 1011  # Weak Signal
    睡觉中 = 1016  # Sleeping
    学习中 = 1018  # Studying
    追剧中 = 1021  # Watching Series
    游戏中 = 1027  # Gaming
    听歌中 = 1028  # Listening Music
    今日天气 = 1030  # Weather
    熬夜中 = 1032  # Staying Up
    恋爱中 = 1051  # In Love
    我没事 = 1052  # I'm Fine
    嗨到飞起 = 1056  # Excited
    元气满满 = 1058  # Energetic
    悠哉哉 = 1059  # Relaxing
    无聊中 = 1060  # Bored
    想静静 = 1061  # Need Peace
    我太难了 = 1062  # Too Hard
    一言难尽 = 1063  # Complicated
    宝宝认证 = 1070  # Baby Certified
    好运锦鲤 = 1071  # Lucky Koi
    摸鱼中 = 1300  # Slacking
    情绪中 = 1401  # In Emo
    水逆退散 = 1201  # Mercury Retrograde
    
    # 2000系列扩展状态
    难得糊涂 = 2001  # Muddled
    出去浪 = 2003  # Hanging Out
    爱你 = 2006  # Love You
    我想开了 = 2013  # Enlightened
    被掏空 = 2014  # Drained
    去旅行 = 2015  # Traveling
    我崩溃了 = 2019  # Crashed
    搬砖中 = 2023  # Working Hard
    一起元梦 = 2025  # Dream Together
    求星搭子 = 2026  # Seeking Star
    春日限定 = 2037  # Spring Limited
    肝作业 = 2012  # Doing Homework

