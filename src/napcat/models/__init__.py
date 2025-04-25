"""Napcat API 模型包

自动生成的API模型类
"""

__all__ = [  # 导出所有API类
    "SendprivatemsgapiAPI",    "SendgroupmsgapiAPI",    "SendmsgapiAPI",    "GetmsgapiAPI",    "GetforwardmsgapiAPI",    "SendlikeapiAPI",    "SetgroupkickapiAPI",    "SetgroupbanapiAPI",    "SetgroupwholebanapiAPI",    "SetgroupadminapiAPI",    "SetgroupcardapiAPI",    "SetgroupnameapiAPI",    "SetgroupleaveapiAPI",    "SetgroupspecialtitleapiAPI",    "SetfriendaddrequestapiAPI",    "SetgroupaddrequestapiAPI",    "GetlogininfoapiAPI",    "GetstrangerinfoapiAPI",    "GetfriendlistapiAPI",    "GetgroupinfoapiAPI",    "GetgrouplistapiAPI",    "GetgroupmemberinfoapiAPI",    "GetgroupmemberlistapiAPI",    "GetgrouphonorinfoapiAPI",    "GetcookiesapiAPI",    "GetcsrftokenapiAPI",    "GetcredentialsapiAPI",    "GetrecordapiAPI",    "GetimageapiAPI",    "CansendimageapiAPI",    "CansendrecordapiAPI",    "GetstatusapiAPI",    "GetversioninfoapiAPI",    "SetqqprofileapiAPI",    "GetonlineclientsapiAPI",    "MarkmsgasreadapiAPI",    "SendgroupforwardmsgapiAPI",    "SendprivateforwardmsgapiAPI",    "GetgroupmsghistoryapiAPI",    "OcrimageapiAPI",    "GetgroupsystemmsgapiAPI",    "GetessencemsglistapiAPI",    "SetgroupportraitapiAPI",    "SetessencemsgapiAPI",    "DeleteessencemsgapiAPI",    "SendgroupnoticeapiAPI",    "GetgroupnoticeapiAPI",    "UploadgroupfileapiAPI",    "DeletegroupfileapiAPI",    "CreategroupfilefolderapiAPI",    "DeletegroupfolderapiAPI",    "GetgroupfilesysteminfoapiAPI",    "GetgrouprootfilesapiAPI",    "GetgroupfilesbyfolderapiAPI",    "GetgroupfileurlapiAPI",    "UploadprivatefileapiAPI",    "DownloadfileapiAPI",    "HandlequickoperationapiAPI",    "UnknownapiAPI",    "ArksharepeerapiAPI",    "ArksharegroupapiAPI",    "GetrobotuinrangeapiAPI",    "SetonlinestatusapiAPI",    "GetfriendswithcategoryapiAPI",    "SetqqavatarapiAPI",    "GetfileapiAPI",    "ForwardfriendsinglemsgapiAPI",    "ForwardgroupsinglemsgapiAPI",    "Translateen2zhapiAPI",    "SetmsgemojilikeapiAPI",    "SendforwardmsgapiAPI",    "MarkprivatemsgasreadapiAPI",    "MarkgroupmsgasreadapiAPI",    "GetfriendmsghistoryapiAPI",    "CreatecollectionapiAPI",    "GetcollectionlistapiAPI",    "SetselflongnickapiAPI",    "GetrecentcontactapiAPI",    "MarkallasreadapiAPI",    "GetprofilelikeapiAPI",    "FetchcustomfaceapiAPI",    "FetchemojilikeapiAPI",    "SetinputstatusapiAPI",    "GetgroupinfoexapiAPI",    "GetgroupignoreaddrequestapiAPI",    "DelgroupnoticeapiAPI",    "FetchuserprofilelikeapiAPI",    "FriendpokeapiAPI",    "GrouppokeapiAPI",    "NcgetpacketstatusapiAPI",    "NcgetuserstatusapiAPI",    "NcgetrkeyapiAPI",    "GetgroupshutlistapiAPI",    "GetguildlistapiAPI",    "GetguildserviceprofileapiAPI",    "GetgroupignorednotifiesapiAPI",    "DeletemsgapiAPI",    "GetmodelshowapiAPI",    "SetmodelshowapiAPI",    "DeletefriendapiAPI",    "GetgroupatallremainapiAPI",    "GetminiapparkapiAPI",    "CheckurlsafelyapiAPI",    "GetwordslicesapiAPI",    "GetaicharactersapiAPI",    "SendgroupairecordapiAPI",    "GetairecordapiAPI",    "SendgroupsignapiAPI",    "SendpacketapiAPI",    "GetclientkeyapiAPI",    "SendpokeapiAPI",    "GetprivatefileurlapiAPI",    "ClickinlinekeyboardbuttonapiAPI",    "GetunidirectionalfriendlistapiAPI",    "SetdiyonlinestatusapiAPI",    "GetrkeyapiAPI",    "GetrkeyserverapiAPI",    "SetgroupremarkapiAPI",    "MovegroupfileapiAPI",    "TransgroupfileapiAPI",    "RenamegroupfileapiAPI",    "BotexitapiAPI",    "SendPrivateMsgAPI",    "SendGroupMsgAPI",    "SendMsgAPI",    "GetMsgAPI",    "GetForwardMsgAPI",    "SendLikeAPI",    "SetGroupKickAPI",    "SetGroupBanAPI",    "SetGroupWholeBanAPI",    "SetGroupAdminAPI",    "SetGroupCardAPI",    "SetGroupNameAPI",    "SetGroupLeaveAPI",    "SetGroupSpecialTitleAPI",    "SetFriendAddRequestAPI",    "SetGroupAddRequestAPI",    "GetLoginInfoAPI",    "GetStrangerInfoAPI",    "GetFriendListAPI",    "GetGroupInfoAPI",    "GetGroupListAPI",    "GetGroupMemberInfoAPI",    "GetGroupMemberListAPI",    "GetGroupHonorInfoAPI",    "GetCookiesAPI",    "GetCsrfTokenAPI",    "GetCredentialsAPI",    "GetRecordAPI",    "GetImageAPI",    "CanSendImageAPI",    "CanSendRecordAPI",    "GetStatusAPI",    "GetVersionInfoAPI",    "SetQqProfileAPI",    "GetOnlineClientsAPI",    "MarkMsgAsReadAPI",    "SendGroupForwardMsgAPI",    "SendPrivateForwardMsgAPI",    "GetGroupMsgHistoryAPI",    "OcrImageAPI",    "GetGroupSystemMsgAPI",    "GetEssenceMsgListAPI",    "SetGroupPortraitAPI",    "SetEssenceMsgAPI",    "DeleteEssenceMsgAPI",    "SendGroupNoticeAPI",    "GetGroupNoticeAPI",    "UploadGroupFileAPI",    "DeleteGroupFileAPI",    "CreateGroupFileFolderAPI",    "DeleteGroupFolderAPI",    "GetGroupFileSystemInfoAPI",    "GetGroupRootFilesAPI",    "GetGroupFilesByFolderAPI",    "GetGroupFileUrlAPI",    "UploadPrivateFileAPI",    "DownloadFileAPI",    "UnknownAPI",    "ArksharepeerAPI",    "ArksharegroupAPI",    "GetRobotUinRangeAPI",    "SetOnlineStatusAPI",    "GetFriendsWithCategoryAPI",    "SetQqAvatarAPI",    "GetFileAPI",    "ForwardFriendSingleMsgAPI",    "ForwardGroupSingleMsgAPI",    "TranslateEn2zhAPI",    "SetMsgEmojiLikeAPI",    "SendForwardMsgAPI",    "MarkPrivateMsgAsReadAPI",    "MarkGroupMsgAsReadAPI",    "GetFriendMsgHistoryAPI",    "CreateCollectionAPI",    "GetCollectionListAPI",    "SetSelfLongnickAPI",    "GetRecentContactAPI",    "MarkAllAsReadAPI",    "GetProfileLikeAPI",    "FetchCustomFaceAPI",    "FetchEmojiLikeAPI",    "SetInputStatusAPI",    "GetGroupInfoExAPI",    "GetGroupIgnoreAddRequestAPI",    "DelGroupNoticeAPI",    "FetchUserProfileLikeAPI",    "FriendPokeAPI",    "GroupPokeAPI",    "NcGetPacketStatusAPI",    "NcGetUserStatusAPI",    "NcGetRkeyAPI",    "GetGroupShutListAPI",    "GetGuildListAPI",    "GetGuildServiceProfileAPI",    "GetGroupIgnoredNotifiesAPI",    "DeleteMsgAPI",    "GetModelShowAPI",    "SetModelShowAPI",    "DeleteFriendAPI",    "GetGroupAtAllRemainAPI",    "GetMiniAppArkAPI",    "CheckUrlSafelyAPI",    "GetAiCharactersAPI",    "SendGroupAiRecordAPI",    "GetAiRecordAPI",    "SendGroupSignAPI",    "SendPacketAPI",    "GetClientkeyAPI",    "SendPokeAPI",    "GetPrivateFileUrlAPI",    "ClickInlineKeyboardButtonAPI",    "GetUnidirectionalFriendListAPI",    "SetDiyOnlineStatusAPI",    "GetRkeyAPI",    "GetRkeyServerAPI",    "SetGroupRemarkAPI",    "MoveGroupFileAPI",    "TransGroupFileAPI",    "RenameGroupFileAPI",    "BotExitAPI",
]

from .sendprivatemsgapi import SendprivatemsgapiAPI

from .sendgroupmsgapi import SendgroupmsgapiAPI

from .sendmsgapi import SendmsgapiAPI

from .getmsgapi import GetmsgapiAPI

from .getforwardmsgapi import GetforwardmsgapiAPI

from .sendlikeapi import SendlikeapiAPI

from .setgroupkickapi import SetgroupkickapiAPI

from .setgroupbanapi import SetgroupbanapiAPI

from .setgroupwholebanapi import SetgroupwholebanapiAPI

from .setgroupadminapi import SetgroupadminapiAPI

from .setgroupcardapi import SetgroupcardapiAPI

from .setgroupnameapi import SetgroupnameapiAPI

from .setgroupleaveapi import SetgroupleaveapiAPI

from .setgroupspecialtitleapi import SetgroupspecialtitleapiAPI

from .setfriendaddrequestapi import SetfriendaddrequestapiAPI

from .setgroupaddrequestapi import SetgroupaddrequestapiAPI

from .getlogininfoapi import GetlogininfoapiAPI

from .getstrangerinfoapi import GetstrangerinfoapiAPI

from .getfriendlistapi import GetfriendlistapiAPI

from .getgroupinfoapi import GetgroupinfoapiAPI

from .getgrouplistapi import GetgrouplistapiAPI

from .getgroupmemberinfoapi import GetgroupmemberinfoapiAPI

from .getgroupmemberlistapi import GetgroupmemberlistapiAPI

from .getgrouphonorinfoapi import GetgrouphonorinfoapiAPI

from .getcookiesapi import GetcookiesapiAPI

from .getcsrftokenapi import GetcsrftokenapiAPI

from .getcredentialsapi import GetcredentialsapiAPI

from .getrecordapi import GetrecordapiAPI

from .getimageapi import GetimageapiAPI

from .cansendimageapi import CansendimageapiAPI

from .cansendrecordapi import CansendrecordapiAPI

from .getstatusapi import GetstatusapiAPI

from .getversioninfoapi import GetversioninfoapiAPI

from .setqqprofileapi import SetqqprofileapiAPI

from .getonlineclientsapi import GetonlineclientsapiAPI

from .markmsgasreadapi import MarkmsgasreadapiAPI

from .sendgroupforwardmsgapi import SendgroupforwardmsgapiAPI

from .sendprivateforwardmsgapi import SendprivateforwardmsgapiAPI

from .getgroupmsghistoryapi import GetgroupmsghistoryapiAPI

from .ocrimageapi import OcrimageapiAPI

from .getgroupsystemmsgapi import GetgroupsystemmsgapiAPI

from .getessencemsglistapi import GetessencemsglistapiAPI

from .setgroupportraitapi import SetgroupportraitapiAPI

from .setessencemsgapi import SetessencemsgapiAPI

from .deleteessencemsgapi import DeleteessencemsgapiAPI

from .sendgroupnoticeapi import SendgroupnoticeapiAPI

from .getgroupnoticeapi import GetgroupnoticeapiAPI

from .uploadgroupfileapi import UploadgroupfileapiAPI

from .deletegroupfileapi import DeletegroupfileapiAPI

from .creategroupfilefolderapi import CreategroupfilefolderapiAPI

from .deletegroupfolderapi import DeletegroupfolderapiAPI

from .getgroupfilesysteminfoapi import GetgroupfilesysteminfoapiAPI

from .getgrouprootfilesapi import GetgrouprootfilesapiAPI

from .getgroupfilesbyfolderapi import GetgroupfilesbyfolderapiAPI

from .getgroupfileurlapi import GetgroupfileurlapiAPI

from .uploadprivatefileapi import UploadprivatefileapiAPI

from .downloadfileapi import DownloadfileapiAPI

from .handlequickoperationapi import HandlequickoperationapiAPI

from .unknownapi import UnknownapiAPI

from .arksharepeerapi import ArksharepeerapiAPI

from .arksharegroupapi import ArksharegroupapiAPI

from .getrobotuinrangeapi import GetrobotuinrangeapiAPI

from .setonlinestatusapi import SetonlinestatusapiAPI

from .getfriendswithcategoryapi import GetfriendswithcategoryapiAPI

from .setqqavatarapi import SetqqavatarapiAPI

from .getfileapi import GetfileapiAPI

from .forwardfriendsinglemsgapi import ForwardfriendsinglemsgapiAPI

from .forwardgroupsinglemsgapi import ForwardgroupsinglemsgapiAPI

from .translateen2zhapi import Translateen2zhapiAPI

from .setmsgemojilikeapi import SetmsgemojilikeapiAPI

from .sendforwardmsgapi import SendforwardmsgapiAPI

from .markprivatemsgasreadapi import MarkprivatemsgasreadapiAPI

from .markgroupmsgasreadapi import MarkgroupmsgasreadapiAPI

from .getfriendmsghistoryapi import GetfriendmsghistoryapiAPI

from .createcollectionapi import CreatecollectionapiAPI

from .getcollectionlistapi import GetcollectionlistapiAPI

from .setselflongnickapi import SetselflongnickapiAPI

from .getrecentcontactapi import GetrecentcontactapiAPI

from .markallasreadapi import MarkallasreadapiAPI

from .getprofilelikeapi import GetprofilelikeapiAPI

from .fetchcustomfaceapi import FetchcustomfaceapiAPI

from .fetchemojilikeapi import FetchemojilikeapiAPI

from .setinputstatusapi import SetinputstatusapiAPI

from .getgroupinfoexapi import GetgroupinfoexapiAPI

from .getgroupignoreaddrequestapi import GetgroupignoreaddrequestapiAPI

from .delgroupnoticeapi import DelgroupnoticeapiAPI

from .fetchuserprofilelikeapi import FetchuserprofilelikeapiAPI

from .friendpokeapi import FriendpokeapiAPI

from .grouppokeapi import GrouppokeapiAPI

from .ncgetpacketstatusapi import NcgetpacketstatusapiAPI

from .ncgetuserstatusapi import NcgetuserstatusapiAPI

from .ncgetrkeyapi import NcgetrkeyapiAPI

from .getgroupshutlistapi import GetgroupshutlistapiAPI

from .getguildlistapi import GetguildlistapiAPI

from .getguildserviceprofileapi import GetguildserviceprofileapiAPI

from .getgroupignorednotifiesapi import GetgroupignorednotifiesapiAPI

from .deletemsgapi import DeletemsgapiAPI

from .getmodelshowapi import GetmodelshowapiAPI

from .setmodelshowapi import SetmodelshowapiAPI

from .deletefriendapi import DeletefriendapiAPI

from .getgroupatallremainapi import GetgroupatallremainapiAPI

from .getminiapparkapi import GetminiapparkapiAPI

from .checkurlsafelyapi import CheckurlsafelyapiAPI

from .getwordslicesapi import GetwordslicesapiAPI

from .getaicharactersapi import GetaicharactersapiAPI

from .sendgroupairecordapi import SendgroupairecordapiAPI

from .getairecordapi import GetairecordapiAPI

from .sendgroupsignapi import SendgroupsignapiAPI

from .sendpacketapi import SendpacketapiAPI

from .getclientkeyapi import GetclientkeyapiAPI

from .sendpokeapi import SendpokeapiAPI

from .getprivatefileurlapi import GetprivatefileurlapiAPI

from .clickinlinekeyboardbuttonapi import ClickinlinekeyboardbuttonapiAPI

from .getunidirectionalfriendlistapi import GetunidirectionalfriendlistapiAPI

from .setdiyonlinestatusapi import SetdiyonlinestatusapiAPI

from .getrkeyapi import GetrkeyapiAPI

from .getrkeyserverapi import GetrkeyserverapiAPI

from .setgroupremarkapi import SetgroupremarkapiAPI

from .movegroupfileapi import MovegroupfileapiAPI

from .transgroupfileapi import TransgroupfileapiAPI

from .renamegroupfileapi import RenamegroupfileapiAPI

from .botexitapi import BotexitapiAPI

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
