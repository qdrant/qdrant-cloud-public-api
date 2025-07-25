// @generated by protoc-gen-connect-query v2.1.1 with parameter "target=js+dts,import_extension=js"
// @generated from file qdrant/cloud/billing/v1/billing.proto (package qdrant.cloud.billing.v1, syntax proto3)
/* eslint-disable */

import { BillingService } from "./billing_pb.js";

/**
 * Lists all invoices for the account identified by the given ID.
 * Required permissions:
 * - read:payment_information
 *
 * @generated from rpc qdrant.cloud.billing.v1.BillingService.ListInvoices
 */
export const listInvoices: typeof BillingService["method"]["listInvoices"];
