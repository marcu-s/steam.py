# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_player.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


class ENotificationSetting(betterproto.Enum):
    NotifyUseDefault = 0
    Always = 1
    Never = 2


@dataclass
class CPlayer_GetMutualFriendsForIncomingInvites_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_IncomingInviteMutualFriendList(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    mutual_friend_account_ids: List[int] = betterproto.uint32_field(2)


@dataclass
class CPlayer_GetMutualFriendsForIncomingInvites_Response(betterproto.Message):
    incoming_invite_mutual_friends_lists: List["CPlayer_IncomingInviteMutualFriendList"] = betterproto.message_field(1)


@dataclass
class CPlayer_GetFriendsGameplayInfo_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetFriendsGameplayInfo_Response(betterproto.Message):
    your_info: "CPlayer_GetFriendsGameplayInfo_ResponseOwnGameplayInfo" = betterproto.message_field(1)
    in_game: List["CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"] = betterproto.message_field(2)
    played_recently: List["CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"] = betterproto.message_field(3)
    played_ever: List["CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"] = betterproto.message_field(4)
    owns: List["CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"] = betterproto.message_field(5)
    in_wishlist: List["CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo"] = betterproto.message_field(6)


@dataclass
class CPlayer_GetFriendsGameplayInfo_ResponseFriendsGameplayInfo(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    minutes_played: int = betterproto.uint32_field(2)
    minutes_played_forever: int = betterproto.uint32_field(3)


@dataclass
class CPlayer_GetFriendsGameplayInfo_ResponseOwnGameplayInfo(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    minutes_played: int = betterproto.uint32_field(2)
    minutes_played_forever: int = betterproto.uint32_field(3)
    in_wishlist: bool = betterproto.bool_field(4)
    owned: bool = betterproto.bool_field(5)


@dataclass
class CPlayer_GetFriendsAppsActivity_Request(betterproto.Message):
    news_language: str = betterproto.string_field(1)
    request_flags: int = betterproto.uint32_field(2)


@dataclass
class CPlayer_GetFriendsAppsActivity_Response(betterproto.Message):
    trending: List["CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo"] = betterproto.message_field(1)
    recent_purchases: List["CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo"] = betterproto.message_field(2)
    unowned: List["CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo"] = betterproto.message_field(3)
    popular: List["CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo"] = betterproto.message_field(4)
    dont_forget: List["CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo"] = betterproto.message_field(5)
    being_discussed: List["CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo"] = betterproto.message_field(6)
    new_to_group: List["CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo"] = betterproto.message_field(7)
    returned_to_group: List["CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo"] = betterproto.message_field(8)
    active_friend_count: int = betterproto.uint32_field(9)


@dataclass
class CPlayer_GetFriendsAppsActivity_ResponseFriendPlayTime(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    minutes_played_this_week: int = betterproto.uint32_field(2)
    minutes_played_two_weeks: int = betterproto.uint32_field(3)
    minutes_played_forever: int = betterproto.uint32_field(4)
    event_count: int = betterproto.uint32_field(5)


@dataclass
class CPlayer_GetFriendsAppsActivity_ResponseAppFriendsInfo(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    friends: List["CPlayer_GetFriendsAppsActivity_ResponseFriendPlayTime"] = betterproto.message_field(2)
    display_order: int = betterproto.uint32_field(3)


@dataclass
class CPlayer_GetGameBadgeLevels_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetGameBadgeLevels_Response(betterproto.Message):
    player_level: int = betterproto.uint32_field(1)
    badges: List["CPlayer_GetGameBadgeLevels_ResponseBadge"] = betterproto.message_field(2)


@dataclass
class CPlayer_GetGameBadgeLevels_ResponseBadge(betterproto.Message):
    level: int = betterproto.int32_field(1)
    series: int = betterproto.int32_field(2)
    border_color: int = betterproto.uint32_field(3)


@dataclass
class CPlayer_GetEmoticonList_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_GetEmoticonList_Response(betterproto.Message):
    emoticons: List["CPlayer_GetEmoticonList_ResponseEmoticon"] = betterproto.message_field(1)


@dataclass
class CPlayer_GetEmoticonList_ResponseEmoticon(betterproto.Message):
    name: str = betterproto.string_field(1)
    count: int = betterproto.int32_field(2)
    time_last_used: int = betterproto.uint32_field(3)
    use_count: int = betterproto.uint32_field(4)
    time_received: int = betterproto.uint32_field(5)


@dataclass
class CPlayer_GetAchievementsProgress_Request(betterproto.Message):
    steamid: int = betterproto.uint64_field(1)
    language: str = betterproto.string_field(2)
    appids: List[int] = betterproto.uint32_field(3)


@dataclass
class CPlayer_GetAchievementsProgress_Response(betterproto.Message):
    achievement_progress: List[
        "CPlayer_GetAchievementsProgress_ResponseAchievementProgress"
    ] = betterproto.message_field(1)


@dataclass
class CPlayer_GetAchievementsProgress_ResponseAchievementProgress(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    unlocked: int = betterproto.uint32_field(2)
    total: int = betterproto.uint32_field(3)
    percentage: float = betterproto.float_field(4)
    all_unlocked: bool = betterproto.bool_field(5)
    cache_time: int = betterproto.uint32_field(6)


@dataclass
class CPlayer_PostStatusToFriends_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    status_text: str = betterproto.string_field(2)


@dataclass
class CPlayer_PostStatusToFriends_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetPostedStatus_Request(betterproto.Message):
    steamid: int = betterproto.uint64_field(1)
    postid: int = betterproto.uint64_field(2)


@dataclass
class CPlayer_GetPostedStatus_Response(betterproto.Message):
    accountid: int = betterproto.uint32_field(1)
    postid: int = betterproto.uint64_field(2)
    status_text: str = betterproto.string_field(3)
    deleted: bool = betterproto.bool_field(4)
    appid: int = betterproto.uint32_field(5)


@dataclass
class CPlayer_DeletePostedStatus_Request(betterproto.Message):
    postid: int = betterproto.uint64_field(1)


@dataclass
class CPlayer_DeletePostedStatus_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetLastPlayedTimes_Request(betterproto.Message):
    min_last_played: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetLastPlayedTimes_Response(betterproto.Message):
    games: List["CPlayer_GetLastPlayedTimes_ResponseGame"] = betterproto.message_field(1)


@dataclass
class CPlayer_GetLastPlayedTimes_ResponseGame(betterproto.Message):
    appid: int = betterproto.int32_field(1)
    last_playtime: int = betterproto.uint32_field(2)
    playtime_2weeks: int = betterproto.int32_field(3)
    playtime_forever: int = betterproto.int32_field(4)
    first_playtime: int = betterproto.uint32_field(5)
    playtime_windows_forever: int = betterproto.int32_field(6)
    playtime_mac_forever: int = betterproto.int32_field(7)
    playtime_linux_forever: int = betterproto.int32_field(8)
    first_windows_playtime: int = betterproto.uint32_field(9)
    first_mac_playtime: int = betterproto.uint32_field(10)
    first_linux_playtime: int = betterproto.uint32_field(11)
    last_windows_playtime: int = betterproto.uint32_field(12)
    last_mac_playtime: int = betterproto.uint32_field(13)
    last_linux_playtime: int = betterproto.uint32_field(14)


@dataclass
class CPlayer_AcceptSSA_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_AcceptSSA_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetNicknameList_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_GetNicknameList_Response(betterproto.Message):
    nicknames: List["CPlayer_GetNicknameList_ResponsePlayerNickname"] = betterproto.message_field(1)


@dataclass
class CPlayer_GetNicknameList_ResponsePlayerNickname(betterproto.Message):
    accountid: float = betterproto.fixed32_field(1)
    nickname: str = betterproto.string_field(2)


@dataclass
class CPlayer_GetPerFriendPreferences_Request(betterproto.Message):
    pass


@dataclass
class PerFriendPreferences(betterproto.Message):
    accountid: float = betterproto.fixed32_field(1)
    nickname: str = betterproto.string_field(2)
    notifications_showingame: "ENotificationSetting" = betterproto.enum_field(3)
    notifications_showonline: "ENotificationSetting" = betterproto.enum_field(4)
    notifications_showmessages: "ENotificationSetting" = betterproto.enum_field(5)
    sounds_showingame: "ENotificationSetting" = betterproto.enum_field(6)
    sounds_showonline: "ENotificationSetting" = betterproto.enum_field(7)
    sounds_showmessages: "ENotificationSetting" = betterproto.enum_field(8)
    notifications_sendmobile: "ENotificationSetting" = betterproto.enum_field(9)


@dataclass
class CPlayer_GetPerFriendPreferences_Response(betterproto.Message):
    preferences: List["PerFriendPreferences"] = betterproto.message_field(1)


@dataclass
class CPlayer_SetPerFriendPreferences_Request(betterproto.Message):
    preferences: "PerFriendPreferences" = betterproto.message_field(1)


@dataclass
class CPlayer_SetPerFriendPreferences_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_AddFriend_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CPlayer_AddFriend_Response(betterproto.Message):
    invite_sent: bool = betterproto.bool_field(1)
    friend_relationship: int = betterproto.uint32_field(2)
    result: int = betterproto.int32_field(3)


@dataclass
class CPlayer_RemoveFriend_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CPlayer_RemoveFriend_Response(betterproto.Message):
    friend_relationship: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_IgnoreFriend_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    unignore: bool = betterproto.bool_field(2)


@dataclass
class CPlayer_IgnoreFriend_Response(betterproto.Message):
    friend_relationship: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetCommunityPreferences_Request(betterproto.Message):
    pass


@dataclass
class CPlayer_CommunityPreferences(betterproto.Message):
    hide_adult_content_violence: bool = betterproto.bool_field(1)
    hide_adult_content_sex: bool = betterproto.bool_field(2)
    parenthesize_nicknames: bool = betterproto.bool_field(4)
    timestamp_updated: int = betterproto.uint32_field(3)


@dataclass
class CPlayer_GetCommunityPreferences_Response(betterproto.Message):
    preferences: "CPlayer_CommunityPreferences" = betterproto.message_field(1)


@dataclass
class CPlayer_SetCommunityPreferences_Request(betterproto.Message):
    preferences: "CPlayer_CommunityPreferences" = betterproto.message_field(1)


@dataclass
class CPlayer_SetCommunityPreferences_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetNewSteamAnnouncementState_Request(betterproto.Message):
    language: int = betterproto.int32_field(1)


@dataclass
class CPlayer_GetNewSteamAnnouncementState_Response(betterproto.Message):
    state: int = betterproto.int32_field(1)
    announcement_headline: str = betterproto.string_field(2)
    announcement_url: str = betterproto.string_field(3)
    time_posted: int = betterproto.uint32_field(4)
    announcement_gid: int = betterproto.uint64_field(5)


@dataclass
class CPlayer_UpdateSteamAnnouncementLastRead_Request(betterproto.Message):
    announcement_gid: int = betterproto.uint64_field(1)
    time_posted: int = betterproto.uint32_field(2)


@dataclass
class CPlayer_UpdateSteamAnnouncementLastRead_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetPrivacySettings_Request(betterproto.Message):
    pass


@dataclass
class CPrivacySettings(betterproto.Message):
    privacy_state: int = betterproto.int32_field(1)
    privacy_state_inventory: int = betterproto.int32_field(2)
    privacy_state_gifts: int = betterproto.int32_field(3)
    privacy_state_ownedgames: int = betterproto.int32_field(4)
    privacy_state_playtime: int = betterproto.int32_field(5)
    privacy_state_friendslist: int = betterproto.int32_field(6)


@dataclass
class CPlayer_GetPrivacySettings_Response(betterproto.Message):
    privacy_settings: "CPrivacySettings" = betterproto.message_field(1)


@dataclass
class CPlayer_GetDurationControl_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass
class CPlayer_GetDurationControl_Response(betterproto.Message):
    is_enabled: bool = betterproto.bool_field(1)
    seconds: int = betterproto.int32_field(2)
    seconds_today: int = betterproto.int32_field(3)
    is_steamchina_account: bool = betterproto.bool_field(4)
    is_age_verified: bool = betterproto.bool_field(5)


@dataclass
class CPlayer_LastPlayedTimes_Notification(betterproto.Message):
    games: List["CPlayer_GetLastPlayedTimes_ResponseGame"] = betterproto.message_field(1)


@dataclass
class CPlayer_FriendNicknameChanged_Notification(betterproto.Message):
    accountid: float = betterproto.fixed32_field(1)
    nickname: str = betterproto.string_field(2)
    is_echo_to_self: bool = betterproto.bool_field(3)


@dataclass
class CPlayer_NewSteamAnnouncementState_Notification(betterproto.Message):
    state: int = betterproto.int32_field(1)
    announcement_headline: str = betterproto.string_field(2)
    announcement_url: str = betterproto.string_field(3)
    time_posted: int = betterproto.uint32_field(4)
    announcement_gid: int = betterproto.uint64_field(5)


@dataclass
class CPlayer_CommunityPreferencesChanged_Notification(betterproto.Message):
    preferences: "CPlayer_CommunityPreferences" = betterproto.message_field(1)


@dataclass
class CPlayer_PerFriendPreferencesChanged_Notification(betterproto.Message):
    accountid: float = betterproto.fixed32_field(1)
    preferences: "PerFriendPreferences" = betterproto.message_field(2)


@dataclass
class CPlayer_PrivacySettingsChanged_Notification(betterproto.Message):
    privacy_settings: "CPrivacySettings" = betterproto.message_field(1)
