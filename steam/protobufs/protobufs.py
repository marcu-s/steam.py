# -*- coding: utf-8 -*-

from . import (
    steammessages_base,
    steammessages_clientserver,
    steammessages_clientserver_2,
    steammessages_clientserver_friends,
    steammessages_clientserver_login,
)
from .emsg import *

__all__ = ("PROTOBUFS",)


PROTOBUFS = {
    EMsg.Multi: steammessages_base.CMsgMulti,
    EMsg.ClientHeartBeat: steammessages_clientserver_login.CMsgClientHeartBeat,
    EMsg.ClientServerTimestampRequest: steammessages_clientserver_login.CMsgClientServerTimestampRequest,
    EMsg.TimestampResponse: steammessages_clientserver_login.CMsgClientServerTimestampResponse,
    EMsg.ClientLogon: steammessages_clientserver_login.CMsgClientLogon,
    EMsg.ClientLogonGameServer: steammessages_clientserver_login.CMsgClientLogon,
    EMsg.ClientLogOnResponse: steammessages_clientserver_login.CMsgClientLogonResponse,
    EMsg.ClientLogOff: steammessages_clientserver_login.CMsgClientLogOff,
    EMsg.ClientLoggedOff: steammessages_clientserver_login.CMsgClientLoggedOff,
    EMsg.ClientNewLoginKey: steammessages_clientserver_login.CMsgClientNewLoginKey,
    EMsg.ClientNewLoginKeyAccepted: steammessages_clientserver_login.CMsgClientNewLoginKeyAccepted,
    EMsg.ClientRequestWebAPIAuthenticateUserNonce: steammessages_clientserver_login.CMsgClientRequestWebApiAuthenticateUserNonce,
    EMsg.ClientRequestWebAPIAuthenticateUserNonceResponse: steammessages_clientserver_login.CMsgClientRequestWebApiAuthenticateUserNonceResponse,
    EMsg.ClientCMList: steammessages_clientserver.CMsgClientCMList,
    EMsg.ClientItemAnnouncements: steammessages_clientserver_2.CMsgClientItemAnnouncements,
    EMsg.ClientRequestItemAnnouncements: steammessages_clientserver_2.CMsgClientRequestItemAnnouncements,
    EMsg.ClientCommentNotifications: steammessages_clientserver_2.CMsgClientCommentNotifications,
    EMsg.ClientRequestCommentNotifications: steammessages_clientserver_2.CMsgClientRequestCommentNotifications,
    EMsg.ClientUserNotifications: steammessages_clientserver_2.CMsgClientUserNotifications,
    EMsg.ClientChatOfflineMessageNotification: steammessages_clientserver_2.CMsgClientOfflineMessageNotification,
    EMsg.ClientChatRequestOfflineMessageCount: steammessages_clientserver_2.CMsgClientRequestOfflineMessageCount,
    EMsg.ClientGamesPlayed: steammessages_clientserver.CMsgClientGamesPlayed,
    EMsg.ClientGamesPlayedWithDataBlob: steammessages_clientserver.CMsgClientGamesPlayed,
    EMsg.ClientAccountInfo: steammessages_clientserver_login.CMsgClientAccountInfo,
    EMsg.ClientEmailAddrInfo: steammessages_clientserver_2.CMsgClientEmailAddrInfo,
    EMsg.ClientIsLimitedAccount: steammessages_clientserver.CMsgClientIsLimitedAccount,
    EMsg.ClientWalletInfoUpdate: steammessages_clientserver.CMsgClientWalletInfoUpdate,
    EMsg.ClientLicenseList: steammessages_clientserver.CMsgClientLicenseList,
    EMsg.ClientGMSServerQuery: steammessages_clientserver_2.CMsgClientGmsServerQuery,
    EMsg.GMSClientServerQueryResponse: steammessages_clientserver_2.CMsgGmsClientServerQueryResponse,
    EMsg.ClientPICSChangesSinceRequest: steammessages_clientserver.CMsgClientPICSChangesSinceRequest,
    EMsg.ClientPICSChangesSinceResponse: steammessages_clientserver.CMsgClientPICSChangesSinceResponse,
    EMsg.ClientPICSProductInfoRequest: steammessages_clientserver.CMsgClientPICSProductInfoRequest,
    EMsg.ClientPICSProductInfoResponse: steammessages_clientserver.CMsgClientPICSProductInfoResponse,
    EMsg.ClientPICSAccessTokenRequest: steammessages_clientserver.CMsgClientPICSAccessTokenRequest,
    EMsg.ClientPICSAccessTokenResponse: steammessages_clientserver.CMsgClientPICSAccessTokenResponse,
    EMsg.EconTradingInitiateTradeRequest: steammessages_clientserver_2.CMsgTradingInitiateTradeRequest,
    EMsg.EconTradingInitiateTradeResponse: steammessages_clientserver_2.CMsgTradingInitiateTradeResponse,
    EMsg.EconTradingCancelTradeRequest: steammessages_clientserver_2.CMsgTradingCancelTradeRequest,
    EMsg.EconTradingInitiateTradeProposed: steammessages_clientserver_2.CMsgTradingInitiateTradeRequest,
    EMsg.EconTradingInitiateTradeResult: steammessages_clientserver_2.CMsgTradingInitiateTradeResponse,
    EMsg.EconTradingStartSession: steammessages_clientserver_2.CMsgTradingStartSession,
    EMsg.ClientChangeStatus: steammessages_clientserver_friends.CMsgClientChangeStatus,
    EMsg.ClientAddFriend: steammessages_clientserver_friends.CMsgClientAddFriend,
    EMsg.ClientAddFriendResponse: steammessages_clientserver_friends.CMsgClientAddFriendResponse,
    EMsg.ClientRemoveFriend: steammessages_clientserver_friends.CMsgClientRemoveFriend,
    EMsg.ClientFSGetFriendsSteamLevels: steammessages_clientserver_2.CMsgClientFsGetFriendsSteamLevels,
    EMsg.ClientFSGetFriendsSteamLevelsResponse: steammessages_clientserver_2.CMsgClientFsGetFriendsSteamLevelsResponse,
    EMsg.ClientPersonaState: steammessages_clientserver_friends.CMsgClientPersonaState,
    EMsg.ClientClanState: steammessages_clientserver.CMsgClientClanState,
    EMsg.ClientFriendsList: steammessages_clientserver_friends.CMsgClientFriendsList,
    EMsg.ClientRequestFriendData: steammessages_clientserver_friends.CMsgClientRequestFriendData,
    EMsg.ClientFriendMsg: steammessages_clientserver_friends.CMsgClientFriendMsg,
    EMsg.ClientChatInvite: steammessages_clientserver.CMsgClientChatInvite,
    EMsg.ClientFriendMsgIncoming: steammessages_clientserver_friends.CMsgClientFriendMsgIncoming,
    EMsg.ClientFriendMsgEchoToSender: steammessages_clientserver_friends.CMsgClientFriendMsgIncoming,
    EMsg.ClientChatGetFriendMessageHistory: steammessages_clientserver_2.CMsgClientChatGetFriendMessageHistory,
    EMsg.ClientChatGetFriendMessageHistoryResponse: steammessages_clientserver_2.CMsgClientChatGetFriendMessageHistoryResponse,
    EMsg.ClientFriendsGroupsList: steammessages_clientserver_friends.CMsgClientFriendsGroupsList,
    EMsg.AMClientCreateFriendsGroup: steammessages_clientserver_friends.CMsgClientCreateFriendsGroup,
    EMsg.AMClientCreateFriendsGroupResponse: steammessages_clientserver_friends.CMsgClientCreateFriendsGroupResponse,
    EMsg.AMClientDeleteFriendsGroup: steammessages_clientserver_friends.CMsgClientDeleteFriendsGroup,
    EMsg.AMClientDeleteFriendsGroupResponse: steammessages_clientserver_friends.CMsgClientDeleteFriendsGroupResponse,
    EMsg.AMClientAddFriendToGroup: steammessages_clientserver_friends.CMsgClientAddFriendToGroup,
    EMsg.AMClientAddFriendToGroupResponse: steammessages_clientserver_friends.CMsgClientAddFriendToGroupResponse,
    EMsg.AMClientRemoveFriendFromGroup: steammessages_clientserver_friends.CMsgClientRemoveFriendFromGroup,
    EMsg.AMClientRemoveFriendFromGroupResponse: steammessages_clientserver_friends.CMsgClientRemoveFriendFromGroupResponse,
    EMsg.ClientPlayerNicknameList: steammessages_clientserver_friends.CMsgClientPlayerNicknameList,
    EMsg.AMClientSetPlayerNickname: steammessages_clientserver_friends.CMsgClientSetPlayerNickname,
    EMsg.AMClientSetPlayerNicknameResponse: steammessages_clientserver_friends.CMsgClientSetPlayerNicknameResponse,
    EMsg.ClientRegisterKey: steammessages_clientserver_2.CMsgClientRegisterKey,
    EMsg.ClientPurchaseResponse: steammessages_clientserver_2.CMsgClientPurchaseResponse,
    EMsg.ClientRequestFreeLicense: steammessages_clientserver_2.CMsgClientRequestFreeLicense,
    EMsg.ClientRequestFreeLicenseResponse: steammessages_clientserver_2.CMsgClientRequestFreeLicenseResponse,
    EMsg.ClientGetNumberOfCurrentPlayersDP: steammessages_clientserver_2.CMsgDpGetNumberOfCurrentPlayers,
    EMsg.ClientGetNumberOfCurrentPlayersDPResponse: steammessages_clientserver_2.CMsgDpGetNumberOfCurrentPlayersResponse,
    EMsg.ClientGetAppOwnershipTicket: steammessages_clientserver.CMsgClientGetAppOwnershipTicket,
    EMsg.ClientGetAppOwnershipTicketResponse: steammessages_clientserver.CMsgClientGetAppOwnershipTicketResponse,
    EMsg.ClientGameConnectTokens: steammessages_clientserver.CMsgClientGameConnectTokens,
    EMsg.ClientAuthList: steammessages_clientserver.CMsgClientAuthList,
    EMsg.ClientAuthListAck: steammessages_clientserver.CMsgClientAuthListAck,
    EMsg.ClientTicketAuthComplete: steammessages_clientserver.CMsgClientTicketAuthComplete,
    EMsg.ClientCurrentUIMode: steammessages_clientserver_2.CMsgClientUiMode,
    EMsg.ClientVanityURLChangedNotification: steammessages_clientserver_2.CMsgClientVanityUrlChangedNotification,
    EMsg.ClientAMGetPersonaNameHistory: steammessages_clientserver.CMsgClientAMGetPersonaNameHistory,
    EMsg.ClientAMGetPersonaNameHistoryResponse: steammessages_clientserver.CMsgClientAMGetPersonaNameHistoryResponse,
    EMsg.ClientUnlockStreaming: steammessages_clientserver_2.CMsgAmUnlockStreaming,
    EMsg.ClientUnlockStreamingResponse: steammessages_clientserver_2.CMsgAmUnlockStreamingResponse,
    EMsg.ClientGetDepotDecryptionKey: steammessages_clientserver_2.CMsgClientGetDepotDecryptionKey,
    EMsg.ClientGetDepotDecryptionKeyResponse: steammessages_clientserver_2.CMsgClientGetDepotDecryptionKeyResponse,
    EMsg.ClientGetCDNAuthToken: steammessages_clientserver_2.CMsgClientGetCdnAuthToken,
    EMsg.ClientGetCDNAuthTokenResponse: steammessages_clientserver_2.CMsgClientGetCdnAuthTokenResponse,
    EMsg.ClientCheckAppBetaPassword: steammessages_clientserver_2.CMsgClientCheckAppBetaPassword,
    EMsg.ClientCheckAppBetaPasswordResponse: steammessages_clientserver_2.CMsgClientCheckAppBetaPasswordResponse,
    EMsg.ClientKickPlayingSession: steammessages_clientserver_2.CMsgClientKickPlayingSession,
    EMsg.ClientConcurrentSessionsBase: steammessages_clientserver_2.CMsgClientPlayingSessionState,
    EMsg.ClientToGC: steammessages_clientserver_2.CMsgGcClient,
    EMsg.ClientFromGC: steammessages_clientserver_2.CMsgGcClient,
    EMsg.ClientRichPresenceUpload: steammessages_clientserver_2.CMsgClientRichPresenceUpload,
    EMsg.ClientGetEmoticonList: steammessages_clientserver_friends.CMsgClientGetEmoticonList,
    EMsg.ClientEmoticonList: steammessages_clientserver_friends.CMsgClientEmoticonList,
    EMsg.ClientServersAvailable: steammessages_clientserver.CMsgClientServersAvailable,
    EMsg.ClientRequestedClientStats: steammessages_clientserver.CMsgClientRequestedClientStats,
}
