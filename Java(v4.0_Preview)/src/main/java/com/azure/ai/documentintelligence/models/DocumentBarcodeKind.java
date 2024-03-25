// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) TypeSpec Code Generator.

package com.azure.ai.documentintelligence.models;

import com.azure.core.annotation.Generated;
import com.azure.core.util.ExpandableStringEnum;
import com.fasterxml.jackson.annotation.JsonCreator;
import java.util.Collection;

/**
 * Barcode kind.
 */
public final class DocumentBarcodeKind extends ExpandableStringEnum<DocumentBarcodeKind> {
    /**
     * QR code, as defined in ISO/IEC 18004:2015.
     */
    @Generated
    public static final DocumentBarcodeKind QRCODE = fromString("QRCode");

    /**
     * PDF417, as defined in ISO 15438.
     */
    @Generated
    public static final DocumentBarcodeKind PDF417 = fromString("PDF417");

    /**
     * GS1 12-digit Universal Product Code.
     */
    @Generated
    public static final DocumentBarcodeKind UPCA = fromString("UPCA");

    /**
     * GS1 6-digit Universal Product Code.
     */
    @Generated
    public static final DocumentBarcodeKind UPCE = fromString("UPCE");

    /**
     * Code 39 barcode, as defined in ISO/IEC 16388:2007.
     */
    @Generated
    public static final DocumentBarcodeKind CODE39 = fromString("Code39");

    /**
     * Code 128 barcode, as defined in ISO/IEC 15417:2007.
     */
    @Generated
    public static final DocumentBarcodeKind CODE128 = fromString("Code128");

    /**
     * GS1 8-digit International Article Number (European Article Number).
     */
    @Generated
    public static final DocumentBarcodeKind EAN8 = fromString("EAN8");

    /**
     * GS1 13-digit International Article Number (European Article Number).
     */
    @Generated
    public static final DocumentBarcodeKind EAN13 = fromString("EAN13");

    /**
     * GS1 DataBar barcode.
     */
    @Generated
    public static final DocumentBarcodeKind DATA_BAR = fromString("DataBar");

    /**
     * Code 93 barcode, as defined in ANSI/AIM BC5-1995.
     */
    @Generated
    public static final DocumentBarcodeKind CODE93 = fromString("Code93");

    /**
     * Codabar barcode, as defined in ANSI/AIM BC3-1995.
     */
    @Generated
    public static final DocumentBarcodeKind CODABAR = fromString("Codabar");

    /**
     * GS1 DataBar Expanded barcode.
     */
    @Generated
    public static final DocumentBarcodeKind DATA_BAR_EXPANDED = fromString("DataBarExpanded");

    /**
     * Interleaved 2 of 5 barcode, as defined in ANSI/AIM BC2-1995.
     */
    @Generated
    public static final DocumentBarcodeKind ITF = fromString("ITF");

    /**
     * Micro QR code, as defined in ISO/IEC 23941:2022.
     */
    @Generated
    public static final DocumentBarcodeKind MICRO_QRCODE = fromString("MicroQRCode");

    /**
     * Aztec code, as defined in ISO/IEC 24778:2008.
     */
    @Generated
    public static final DocumentBarcodeKind AZTEC = fromString("Aztec");

    /**
     * Data matrix code, as defined in ISO/IEC 16022:2006.
     */
    @Generated
    public static final DocumentBarcodeKind DATA_MATRIX = fromString("DataMatrix");

    /**
     * MaxiCode, as defined in ISO/IEC 16023:2000.
     */
    @Generated
    public static final DocumentBarcodeKind MAXI_CODE = fromString("MaxiCode");

    /**
     * Creates a new instance of DocumentBarcodeKind value.
     * 
     * @deprecated Use the {@link #fromString(String)} factory method.
     */
    @Generated
    @Deprecated
    public DocumentBarcodeKind() {
    }

    /**
     * Creates or finds a DocumentBarcodeKind from its string representation.
     * 
     * @param name a name to look for.
     * @return the corresponding DocumentBarcodeKind.
     */
    @Generated
    @JsonCreator
    public static DocumentBarcodeKind fromString(String name) {
        return fromString(name, DocumentBarcodeKind.class);
    }

    /**
     * Gets known DocumentBarcodeKind values.
     * 
     * @return known DocumentBarcodeKind values.
     */
    @Generated
    public static Collection<DocumentBarcodeKind> values() {
        return values(DocumentBarcodeKind.class);
    }
}