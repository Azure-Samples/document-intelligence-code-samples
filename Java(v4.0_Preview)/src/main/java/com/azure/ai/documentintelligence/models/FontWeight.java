// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) TypeSpec Code Generator.

package com.azure.ai.documentintelligence.models;

import com.azure.core.annotation.Generated;
import com.azure.core.util.ExpandableStringEnum;
import com.fasterxml.jackson.annotation.JsonCreator;
import java.util.Collection;

/**
 * Font weight.
 */
public final class FontWeight extends ExpandableStringEnum<FontWeight> {
    /**
     * Characters are represented normally.
     */
    @Generated
    public static final FontWeight NORMAL = fromString("normal");

    /**
     * Characters are represented with thicker strokes.
     */
    @Generated
    public static final FontWeight BOLD = fromString("bold");

    /**
     * Creates a new instance of FontWeight value.
     * 
     * @deprecated Use the {@link #fromString(String)} factory method.
     */
    @Generated
    @Deprecated
    public FontWeight() {
    }

    /**
     * Creates or finds a FontWeight from its string representation.
     * 
     * @param name a name to look for.
     * @return the corresponding FontWeight.
     */
    @Generated
    @JsonCreator
    public static FontWeight fromString(String name) {
        return fromString(name, FontWeight.class);
    }

    /**
     * Gets known FontWeight values.
     * 
     * @return known FontWeight values.
     */
    @Generated
    public static Collection<FontWeight> values() {
        return values(FontWeight.class);
    }
}