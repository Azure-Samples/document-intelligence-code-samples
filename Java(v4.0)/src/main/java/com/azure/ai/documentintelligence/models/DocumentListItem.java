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
 * An object representing a list item in the document.
 */
@Immutable
public final class DocumentListItem {
    /*
     * Level of the list item (1-indexed).
     */
    @Generated
    @JsonProperty(value = "level")
    private int level;

    /*
     * Content of the list item.
     */
    @Generated
    @JsonProperty(value = "content")
    private String content;

    /*
     * Bounding regions covering the list item.
     */
    @Generated
    @JsonProperty(value = "boundingRegions")
    private List<BoundingRegion> boundingRegions;

    /*
     * Location of the list item in the reading order concatenated content.
     */
    @Generated
    @JsonProperty(value = "spans")
    private List<DocumentSpan> spans;

    /*
     * Child elements of the list item.
     */
    @Generated
    @JsonProperty(value = "elements")
    private List<String> elements;

    /**
     * Creates an instance of DocumentListItem class.
     * 
     * @param level the level value to set.
     * @param content the content value to set.
     * @param spans the spans value to set.
     */
    @Generated
    @JsonCreator
    private DocumentListItem(@JsonProperty(value = "level") int level, @JsonProperty(value = "content") String content,
        @JsonProperty(value = "spans") List<DocumentSpan> spans) {
        this.level = level;
        this.content = content;
        this.spans = spans;
    }

    /**
     * Get the level property: Level of the list item (1-indexed).
     * 
     * @return the level value.
     */
    @Generated
    public int getLevel() {
        return this.level;
    }

    /**
     * Get the content property: Content of the list item.
     * 
     * @return the content value.
     */
    @Generated
    public String getContent() {
        return this.content;
    }

    /**
     * Get the boundingRegions property: Bounding regions covering the list item.
     * 
     * @return the boundingRegions value.
     */
    @Generated
    public List<BoundingRegion> getBoundingRegions() {
        return this.boundingRegions;
    }

    /**
     * Get the spans property: Location of the list item in the reading order concatenated content.
     * 
     * @return the spans value.
     */
    @Generated
    public List<DocumentSpan> getSpans() {
        return this.spans;
    }

    /**
     * Get the elements property: Child elements of the list item.
     * 
     * @return the elements value.
     */
    @Generated
    public List<String> getElements() {
        return this.elements;
    }
}