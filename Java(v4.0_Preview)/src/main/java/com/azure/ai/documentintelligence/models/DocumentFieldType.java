// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) TypeSpec Code Generator.

package com.azure.ai.documentintelligence.models;

import com.azure.core.annotation.Generated;
import com.azure.core.util.ExpandableStringEnum;
import com.fasterxml.jackson.annotation.JsonCreator;
import java.util.Collection;

/**
 * Semantic data type of the field value.
 */
public final class DocumentFieldType extends ExpandableStringEnum<DocumentFieldType> {
    /**
     * Plain text.
     */
    @Generated
    public static final DocumentFieldType STRING = fromString("string");

    /**
     * Date, normalized to ISO 8601 (YYYY-MM-DD) format.
     */
    @Generated
    public static final DocumentFieldType DATE = fromString("date");

    /**
     * Time, normalized to ISO 8601 (hh:mm:ss) format.
     */
    @Generated
    public static final DocumentFieldType TIME = fromString("time");

    /**
     * Phone number, normalized to E.164 (+{CountryCode}{SubscriberNumber}) format.
     */
    @Generated
    public static final DocumentFieldType PHONE_NUMBER = fromString("phoneNumber");

    /**
     * Floating point number, normalized to double precision floating point.
     */
    @Generated
    public static final DocumentFieldType NUMBER = fromString("number");

    /**
     * Integer number, normalized to 64-bit signed integer.
     */
    @Generated
    public static final DocumentFieldType INTEGER = fromString("integer");

    /**
     * Is field selected?.
     */
    @Generated
    public static final DocumentFieldType SELECTION_MARK = fromString("selectionMark");

    /**
     * Country/region, normalized to ISO 3166-1 alpha-3 format (ex. USA).
     */
    @Generated
    public static final DocumentFieldType COUNTRY_REGION = fromString("countryRegion");

    /**
     * Is signature present?.
     */
    @Generated
    public static final DocumentFieldType SIGNATURE = fromString("signature");

    /**
     * List of subfields of the same type.
     */
    @Generated
    public static final DocumentFieldType ARRAY = fromString("array");

    /**
     * Named list of subfields of potentially different types.
     */
    @Generated
    public static final DocumentFieldType OBJECT = fromString("object");

    /**
     * Currency amount with optional currency symbol and unit.
     */
    @Generated
    public static final DocumentFieldType CURRENCY = fromString("currency");

    /**
     * Parsed address.
     */
    @Generated
    public static final DocumentFieldType ADDRESS = fromString("address");

    /**
     * Boolean value, normalized to true or false.
     */
    @Generated
    public static final DocumentFieldType BOOLEAN = fromString("boolean");

    /**
     * Array of selected string values.
     */
    @Generated
    public static final DocumentFieldType SELECTION_GROUP = fromString("selectionGroup");

    /**
     * Creates a new instance of DocumentFieldType value.
     * 
     * @deprecated Use the {@link #fromString(String)} factory method.
     */
    @Generated
    @Deprecated
    public DocumentFieldType() {
    }

    /**
     * Creates or finds a DocumentFieldType from its string representation.
     * 
     * @param name a name to look for.
     * @return the corresponding DocumentFieldType.
     */
    @Generated
    @JsonCreator
    public static DocumentFieldType fromString(String name) {
        return fromString(name, DocumentFieldType.class);
    }

    /**
     * Gets known DocumentFieldType values.
     * 
     * @return known DocumentFieldType values.
     */
    @Generated
    public static Collection<DocumentFieldType> values() {
        return values(DocumentFieldType.class);
    }
}