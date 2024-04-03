// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) TypeSpec Code Generator.

package com.azure.ai.documentintelligence.models;

import com.azure.core.annotation.Generated;
import com.azure.core.annotation.Immutable;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;

/**
 * An object representing the field key or value in a key-value pair.
 */
@Immutable
public final class DocumentKeyValueElement {
    /*
     * Concatenated content of the key-value element in reading order.
     */
    @Generated
    @JsonProperty(value = "content")
    private String content;

    /*
     * Bounding regions covering the key-value element.
     */
    @Generated
    @JsonProperty(value = "boundingRegions")
    private List<BoundingRegion> boundingRegions;

    /*
     * Location of the key-value element in the reading order concatenated content.
     */
    @Generated
    @JsonProperty(value = "spans")
    private List<DocumentSpan> spans;

    /**
     * Creates an instance of DocumentKeyValueElement class.
     * 
     * @param content the content value to set.
     * @param spans the spans value to set.
     */
    @Generated
    @JsonCreator
    private DocumentKeyValueElement(@JsonProperty(value = "content") String content,
        @JsonProperty(value = "spans") List<DocumentSpan> spans) {
        this.content = content;
        this.spans = spans;
    }

    /**
     * Get the content property: Concatenated content of the key-value element in reading order.
     * 
     * @return the content value.
     */
    @Generated
    public String getContent() {
        return this.content;
    }

    /**
     * Get the boundingRegions property: Bounding regions covering the key-value element.
     * 
     * @return the boundingRegions value.
     */
    @Generated
    public List<BoundingRegion> getBoundingRegions() {
        return this.boundingRegions;
    }

    /**
     * Get the spans property: Location of the key-value element in the reading order concatenated content.
     * 
     * @return the spans value.
     */
    @Generated
    public List<DocumentSpan> getSpans() {
        return this.spans;
    }
}