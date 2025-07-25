// @generated by protoc-gen-connect-query v2.1.1 with parameter "target=js+dts,import_extension=js"
// @generated from file qdrant/cloud/account/v1/account.proto (package qdrant.cloud.account.v1, syntax proto3)
/* eslint-disable */

import { AccountService } from "./account_pb.js";

/**
 * Lists all accounts associated with the authenticated actor, where the actor has the specified permission.
 * Required permissions:
 * - read:accounts
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.ListAccounts
 */
export const listAccounts = AccountService.method.listAccounts;

/**
 * Gets an account identified by the given ID.
 * Required permissions:
 * - read:account
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.GetAccount
 */
export const getAccount = AccountService.method.getAccount;

/**
 * Creates an account for the authenticated user.
 * Required permissions:
 * - None (authenticated only)
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.CreateAccount
 */
export const createAccount = AccountService.method.createAccount;

/**
 * Updates an account identified by the given ID.
 * Required permissions:
 * - write:account
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.UpdateAccount
 */
export const updateAccount = AccountService.method.updateAccount;

/**
 * Deletes an account identified by the given ID.
 * Required permissions:
 * - delete:account
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.DeleteAccount
 */
export const deleteAccount = AccountService.method.deleteAccount;

/**
 * Lists all account invites in the account identified by the given account ID.
 * Required permissions:
 * - read:invites
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.ListAccountInvites
 */
export const listAccountInvites = AccountService.method.listAccountInvites;

/**
 * Lists all account invites for the authenticated user (across all accounts).
 * These are the invites the user has received, not the ones they have sent.
 * Required permissions:
 * - None (authenticated only)
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.ListReceivedAccountInvites
 */
export const listReceivedAccountInvites = AccountService.method.listReceivedAccountInvites;

/**
 * Gets an account invite identified by the given account ID and invite ID.
 * Required permissions:
 * - read:invites
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.GetAccountInvite
 */
export const getAccountInvite = AccountService.method.getAccountInvite;

/**
 * Creates a new account invite.
 * Required permissions:
 * - write:invites
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.CreateAccountInvite
 */
export const createAccountInvite = AccountService.method.createAccountInvite;

/**
 * Deletes an account invite.
 * Required permissions:
 * - delete:invites
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.DeleteAccountInvite
 */
export const deleteAccountInvite = AccountService.method.deleteAccountInvite;

/**
 * Accepts an account invite.
 * The authenticated user's email address must match the email address specified in
 * the invite.
 * Required permissions:
 * - None (authenticated only)
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.AcceptAccountInvite
 */
export const acceptAccountInvite = AccountService.method.acceptAccountInvite;

/**
 * Rejects an account invite.
 * The authenticated user's email address must match the email address specified in
 * the invite.
 * Required permissions:
 * - None (authenticated only)
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.RejectAccountInvite
 */
export const rejectAccountInvite = AccountService.method.rejectAccountInvite;

/**
 * Lists all account members in the account identified by the given account ID.
 * The authenticated actor must be a member of the account identified by the given account ID.
 * Required permissions:
 * - read:users
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.ListAccountMembers
 */
export const listAccountMembers = AccountService.method.listAccountMembers;

/**
 * Gets an account member by ID.
 * The authenticated actor must be a member of the same account as the member being fetch.
 * Required permissions:
 * - read:users
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.GetAccountMember
 */
export const getAccountMember = AccountService.method.getAccountMember;

/**
 * Deletes an account member.
 * The authenticated actor must be a member of the account from which the the member is being removed.
 * Required permissions:
 * - delete:users
 *
 * @generated from rpc qdrant.cloud.account.v1.AccountService.DeleteAccountMember
 */
export const deleteAccountMember = AccountService.method.deleteAccountMember;
