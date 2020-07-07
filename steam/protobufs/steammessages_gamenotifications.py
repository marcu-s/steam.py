# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_gamenotifications.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CGameNotifications_Variable(betterproto.Message):
    key: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CGameNotifications_LocalizedText(betterproto.Message):
    token: str = betterproto.string_field(1)
    variables: List["CGameNotifications_Variable"] = betterproto.message_field(2)
    rendered_text: str = betterproto.string_field(3)


@dataclass
class CGameNotifications_UserStatus(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    state: str = betterproto.string_field(2)
    title: "CGameNotifications_LocalizedText" = betterproto.message_field(3)
    message: "CGameNotifications_LocalizedText" = betterproto.message_field(4)


@dataclass
class CGameNotifications_CreateSession_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    context: int = betterproto.uint64_field(2)
    title: "CGameNotifications_LocalizedText" = betterproto.message_field(3)
    users: List["CGameNotifications_UserStatus"] = betterproto.message_field(4)
    steamid: float = betterproto.fixed64_field(5)


@dataclass
class CGameNotifications_CreateSession_Response(betterproto.Message):
    sessionid: int = betterproto.uint64_field(1)


@dataclass
class CGameNotifications_DeleteSession_Request(betterproto.Message):
    sessionid: int = betterproto.uint64_field(1)
    appid: int = betterproto.uint32_field(2)
    steamid: float = betterproto.fixed64_field(3)


@dataclass
class CGameNotifications_DeleteSession_Response(betterproto.Message):
    pass


@dataclass
class CGameNotifications_UpdateSession_Request(betterproto.Message):
    sessionid: int = betterproto.uint64_field(1)
    appid: int = betterproto.uint32_field(2)
    title: "CGameNotifications_LocalizedText" = betterproto.message_field(3)
    users: List["CGameNotifications_UserStatus"] = betterproto.message_field(4)
    steamid: float = betterproto.fixed64_field(6)


@dataclass
class CGameNotifications_UpdateSession_Response(betterproto.Message):
    pass


@dataclass
class CGameNotifications_EnumerateSessions_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    include_all_user_messages: bool = betterproto.bool_field(3)
    include_auth_user_message: bool = betterproto.bool_field(4)
    language: str = betterproto.string_field(5)


@dataclass
class CGameNotifications_Session(betterproto.Message):
    sessionid: int = betterproto.uint64_field(1)
    appid: int = betterproto.uint64_field(2)
    context: int = betterproto.uint64_field(3)
    title: "CGameNotifications_LocalizedText" = betterproto.message_field(4)
    time_created: int = betterproto.uint32_field(5)
    time_updated: int = betterproto.uint32_field(6)
    user_status: List["CGameNotifications_UserStatus"] = betterproto.message_field(7)


@dataclass
class CGameNotifications_EnumerateSessions_Response(betterproto.Message):
    sessions: List["CGameNotifications_Session"] = betterproto.message_field(1)


@dataclass
class CGameNotifications_GetSessionDetails_Request(betterproto.Message):
    sessions: List["CGameNotifications_GetSessionDetails_RequestRequestedSession"] = betterproto.message_field(1)
    appid: int = betterproto.uint32_field(2)
    language: str = betterproto.string_field(3)


@dataclass
class CGameNotifications_GetSessionDetails_RequestRequestedSession(betterproto.Message):
    sessionid: int = betterproto.uint64_field(1)
    include_auth_user_message: bool = betterproto.bool_field(3)


@dataclass
class CGameNotifications_GetSessionDetails_Response(betterproto.Message):
    sessions: List["CGameNotifications_Session"] = betterproto.message_field(1)


@dataclass
class GameNotificationSettings(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    allow_notifications: bool = betterproto.bool_field(2)


@dataclass
class CGameNotifications_UpdateNotificationSettings_Request(betterproto.Message):
    game_notification_settings: List["GameNotificationSettings"] = betterproto.message_field(1)


@dataclass
class CGameNotifications_UpdateNotificationSettings_Response(betterproto.Message):
    pass


@dataclass
class CGameNotifications_OnNotificationsRequested_Notification(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    appid: int = betterproto.uint32_field(2)


@dataclass
class CGameNotifications_OnUserStatusChanged_Notification(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    sessionid: int = betterproto.uint64_field(2)
    appid: int = betterproto.uint32_field(3)
    status: "CGameNotifications_UserStatus" = betterproto.message_field(4)
    removed: bool = betterproto.bool_field(5)
