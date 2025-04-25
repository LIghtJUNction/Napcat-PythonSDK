"""Napcat API 模型包

自动生成的API模型类
"""

__all__ = [  # 导出所有API类
    "SendPrivateMsgAPI",    "SendGroupMsgAPI",    "SendMsgAPI",    "GetMsgAPI",    "GetForwardMsgAPI",    "SendLikeAPI",    "SetGroupKickAPI",    "SetGroupBanAPI",    "SetGroupWholeBanAPI",    "SetGroupAdminAPI",    "SetGroupCardAPI",    "SetGroupNameAPI",    "SetGroupLeaveAPI",    "SetGroupSpecialTitleAPI",    "SetFriendAddRequestAPI",    "SetGroupAddRequestAPI",    "GetLoginInfoAPI",    "GetStrangerInfoAPI",    "GetFriendListAPI",    "GetGroupInfoAPI",    "GetGroupListAPI",    "GetGroupMemberInfoAPI",    "GetGroupMemberListAPI",    "GetGroupHonorInfoAPI",    "GetCookiesAPI",    "GetCsrfTokenAPI",    "GetCredentialsAPI",    "GetRecordAPI",    "GetImageAPI",    "CanSendImageAPI",    "CanSendRecordAPI",    "GetStatusAPI",    "GetVersionInfoAPI",    "SetQqProfileAPI",    "GetOnlineClientsAPI",    "MarkMsgAsReadAPI",    "SendGroupForwardMsgAPI",    "SendPrivateForwardMsgAPI",    "GetGroupMsgHistoryAPI",    "OcrImageAPI",    "GetGroupSystemMsgAPI",    "GetEssenceMsgListAPI",    "SetGroupPortraitAPI",    "SetEssenceMsgAPI",    "DeleteEssenceMsgAPI",    "SendGroupNoticeAPI",    "GetGroupNoticeAPI",    "UploadGroupFileAPI",    "DeleteGroupFileAPI",    "CreateGroupFileFolderAPI",    "DeleteGroupFolderAPI",    "GetGroupFileSystemInfoAPI",    "GetGroupRootFilesAPI",    "GetGroupFilesByFolderAPI",    "GetGroupFileUrlAPI",    "UploadPrivateFileAPI",    "DownloadFileAPI",    "HandleQuickOperationAPI",    "UnknownAPI",    "ArksharepeerAPI",    "ArksharegroupAPI",    "GetRobotUinRangeAPI",    "SetOnlineStatusAPI",    "GetFriendsWithCategoryAPI",    "SetQqAvatarAPI",    "GetFileAPI",    "ForwardFriendSingleMsgAPI",    "ForwardGroupSingleMsgAPI",    "TranslateEn2zhAPI",    "SetMsgEmojiLikeAPI",    "SendForwardMsgAPI",    "MarkPrivateMsgAsReadAPI",    "MarkGroupMsgAsReadAPI",    "GetFriendMsgHistoryAPI",    "CreateCollectionAPI",    "GetCollectionListAPI",    "SetSelfLongnickAPI",    "GetRecentContactAPI",    "MarkAllAsReadAPI",    "GetProfileLikeAPI",    "FetchCustomFaceAPI",    "FetchEmojiLikeAPI",    "SetInputStatusAPI",    "GetGroupInfoExAPI",    "GetGroupIgnoreAddRequestAPI",    "DelGroupNoticeAPI",    "FetchUserProfileLikeAPI",    "FriendPokeAPI",    "GroupPokeAPI",    "NcGetPacketStatusAPI",    "NcGetUserStatusAPI",    "NcGetRkeyAPI",    "GetGroupShutListAPI",    "GetGuildListAPI",    "GetGuildServiceProfileAPI",    "GetGroupIgnoredNotifiesAPI",    "DeleteMsgAPI",    "GetModelShowAPI",    "SetModelShowAPI",    "DeleteFriendAPI",    "GetGroupAtAllRemainAPI",    "GetMiniAppArkAPI",    "CheckUrlSafelyAPI",    "GetWordSlicesAPI",    "GetAiCharactersAPI",    "SendGroupAiRecordAPI",    "GetAiRecordAPI",    "SendGroupSignAPI",    "SendPacketAPI",    "GetClientkeyAPI",    "SendPokeAPI",    "GetPrivateFileUrlAPI",    "ClickInlineKeyboardButtonAPI",    "GetUnidirectionalFriendListAPI",    "SetDiyOnlineStatusAPI",    "GetRkeyAPI",    "GetRkeyServerAPI",    "SetGroupRemarkAPI",    "MoveGroupFileAPI",    "TransGroupFileAPI",    "RenameGroupFileAPI",    "BotExitAPI",
]

from .sendprivatemsgapi import SendPrivateMsgAPI

from .sendgroupmsgapi import SendGroupMsgAPI

from .sendmsgapi import SendMsgAPI

from .getmsgapi import GetMsgAPI

from .getforwardmsgapi import GetForwardMsgAPI

from .sendlikeapi import SendLikeAPI

from .setgroupkickapi import SetGroupKickAPI

from .setgroupbanapi import SetGroupBanAPI

from .setgroupwholebanapi import SetGroupWholeBanAPI

from .setgroupadminapi import SetGroupAdminAPI

from .setgroupcardapi import SetGroupCardAPI

from .setgroupnameapi import SetGroupNameAPI

from .setgroupleaveapi import SetGroupLeaveAPI

from .setgroupspecialtitleapi import SetGroupSpecialTitleAPI

from .setfriendaddrequestapi import SetFriendAddRequestAPI

from .setgroupaddrequestapi import SetGroupAddRequestAPI

from .getlogininfoapi import GetLoginInfoAPI

from .getstrangerinfoapi import GetStrangerInfoAPI

from .getfriendlistapi import GetFriendListAPI

from .getgroupinfoapi import GetGroupInfoAPI

from .getgrouplistapi import GetGroupListAPI

from .getgroupmemberinfoapi import GetGroupMemberInfoAPI

from .getgroupmemberlistapi import GetGroupMemberListAPI

from .getgrouphonorinfoapi import GetGroupHonorInfoAPI

from .getcookiesapi import GetCookiesAPI

from .getcsrftokenapi import GetCsrfTokenAPI

from .getcredentialsapi import GetCredentialsAPI

from .getrecordapi import GetRecordAPI

from .getimageapi import GetImageAPI

from .cansendimageapi import CanSendImageAPI

from .cansendrecordapi import CanSendRecordAPI

from .getstatusapi import GetStatusAPI

from .getversioninfoapi import GetVersionInfoAPI

from .setqqprofileapi import SetQqProfileAPI

from .getonlineclientsapi import GetOnlineClientsAPI

from .markmsgasreadapi import MarkMsgAsReadAPI

from .sendgroupforwardmsgapi import SendGroupForwardMsgAPI

from .sendprivateforwardmsgapi import SendPrivateForwardMsgAPI

from .getgroupmsghistoryapi import GetGroupMsgHistoryAPI

from .ocrimageapi import OcrImageAPI

from .getgroupsystemmsgapi import GetGroupSystemMsgAPI

from .getessencemsglistapi import GetEssenceMsgListAPI

from .setgroupportraitapi import SetGroupPortraitAPI

from .setessencemsgapi import SetEssenceMsgAPI

from .deleteessencemsgapi import DeleteEssenceMsgAPI

from .sendgroupnoticeapi import SendGroupNoticeAPI

from .getgroupnoticeapi import GetGroupNoticeAPI

from .uploadgroupfileapi import UploadGroupFileAPI

from .deletegroupfileapi import DeleteGroupFileAPI

from .creategroupfilefolderapi import CreateGroupFileFolderAPI

from .deletegroupfolderapi import DeleteGroupFolderAPI

from .getgroupfilesysteminfoapi import GetGroupFileSystemInfoAPI

from .getgrouprootfilesapi import GetGroupRootFilesAPI

from .getgroupfilesbyfolderapi import GetGroupFilesByFolderAPI

from .getgroupfileurlapi import GetGroupFileUrlAPI

from .uploadprivatefileapi import UploadPrivateFileAPI

from .downloadfileapi import DownloadFileAPI

from .handlequickoperationapi import HandleQuickOperationAPI

from .unknownapi import UnknownAPI

from .arksharepeerapi import ArksharepeerAPI

from .arksharegroupapi import ArksharegroupAPI

from .getrobotuinrangeapi import GetRobotUinRangeAPI

from .setonlinestatusapi import SetOnlineStatusAPI

from .getfriendswithcategoryapi import GetFriendsWithCategoryAPI

from .setqqavatarapi import SetQqAvatarAPI

from .getfileapi import GetFileAPI

from .forwardfriendsinglemsgapi import ForwardFriendSingleMsgAPI

from .forwardgroupsinglemsgapi import ForwardGroupSingleMsgAPI

from .translateen2zhapi import TranslateEn2zhAPI

from .setmsgemojilikeapi import SetMsgEmojiLikeAPI

from .sendforwardmsgapi import SendForwardMsgAPI

from .markprivatemsgasreadapi import MarkPrivateMsgAsReadAPI

from .markgroupmsgasreadapi import MarkGroupMsgAsReadAPI

from .getfriendmsghistoryapi import GetFriendMsgHistoryAPI

from .createcollectionapi import CreateCollectionAPI

from .getcollectionlistapi import GetCollectionListAPI

from .setselflongnickapi import SetSelfLongnickAPI

from .getrecentcontactapi import GetRecentContactAPI

from .markallasreadapi import MarkAllAsReadAPI

from .getprofilelikeapi import GetProfileLikeAPI

from .fetchcustomfaceapi import FetchCustomFaceAPI

from .fetchemojilikeapi import FetchEmojiLikeAPI

from .setinputstatusapi import SetInputStatusAPI

from .getgroupinfoexapi import GetGroupInfoExAPI

from .getgroupignoreaddrequestapi import GetGroupIgnoreAddRequestAPI

from .delgroupnoticeapi import DelGroupNoticeAPI

from .fetchuserprofilelikeapi import FetchUserProfileLikeAPI

from .friendpokeapi import FriendPokeAPI

from .grouppokeapi import GroupPokeAPI

from .ncgetpacketstatusapi import NcGetPacketStatusAPI

from .ncgetuserstatusapi import NcGetUserStatusAPI

from .ncgetrkeyapi import NcGetRkeyAPI

from .getgroupshutlistapi import GetGroupShutListAPI

from .getguildlistapi import GetGuildListAPI

from .getguildserviceprofileapi import GetGuildServiceProfileAPI

from .getgroupignorednotifiesapi import GetGroupIgnoredNotifiesAPI

from .deletemsgapi import DeleteMsgAPI

from .getmodelshowapi import GetModelShowAPI

from .setmodelshowapi import SetModelShowAPI

from .deletefriendapi import DeleteFriendAPI

from .getgroupatallremainapi import GetGroupAtAllRemainAPI

from .getminiapparkapi import GetMiniAppArkAPI

from .checkurlsafelyapi import CheckUrlSafelyAPI

from .getwordslicesapi import GetWordSlicesAPI

from .getaicharactersapi import GetAiCharactersAPI

from .sendgroupairecordapi import SendGroupAiRecordAPI

from .getairecordapi import GetAiRecordAPI

from .sendgroupsignapi import SendGroupSignAPI

from .sendpacketapi import SendPacketAPI

from .getclientkeyapi import GetClientkeyAPI

from .sendpokeapi import SendPokeAPI

from .getprivatefileurlapi import GetPrivateFileUrlAPI

from .clickinlinekeyboardbuttonapi import ClickInlineKeyboardButtonAPI

from .getunidirectionalfriendlistapi import GetUnidirectionalFriendListAPI

from .setdiyonlinestatusapi import SetDiyOnlineStatusAPI

from .getrkeyapi import GetRkeyAPI

from .getrkeyserverapi import GetRkeyServerAPI

from .setgroupremarkapi import SetGroupRemarkAPI

from .movegroupfileapi import MoveGroupFileAPI

from .transgroupfileapi import TransGroupFileAPI

from .renamegroupfileapi import RenameGroupFileAPI

from .botexitapi import BotExitAPI
