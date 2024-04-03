// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) TypeSpec Code Generator.

package com.azure.ai.documentintelligence.models;

import com.azure.core.annotation.Generated;
import com.azure.core.annotation.Immutable;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.time.OffsetDateTime;
import java.util.List;
import java.util.Map;

/**
 * Document classifier info.
 */
@Immutable
public final class DocumentClassifierDetails {
    /*
     * Unique document classifier name.
     */
    @Generated
    @JsonProperty(value = "classifierId", access = JsonProperty.Access.WRITE_ONLY)
    private String classifierId;

    /*
     * Document classifier description.
     */
    @Generated
    @JsonProperty(value = "description")
    private String description;

    /*
     * Date and time (UTC) when the document classifier was created.
     */
    @Generated
    @JsonProperty(value = "createdDateTime")
    private OffsetDateTime createdDateTime;

    /*
     * Date and time (UTC) when the document classifier will expire.
     */
    @Generated
    @JsonProperty(value = "expirationDateTime")
    private OffsetDateTime expirationDateTime;

    /*
     * API version used to create this document classifier.
     */
    @Generated
    @JsonProperty(value = "apiVersion")
    private String apiVersion;

    /*
     * Base classifierId on top of which the classifier was trained.
     */
    @Generated
    @JsonProperty(value = "baseClassifierId")
    private String baseClassifierId;

    /*
     * List of document types to classify against.
     */
    @Generated
    @JsonProperty(value = "docTypes")
    private Map<String, ClassifierDocumentTypeDetails> docTypes;

    /*
     * List of warnings encountered while building the classifier.
     */
    @Generated
    @JsonProperty(value = "warnings")
    private List<Warning> warnings;

    /**
     * Creates an instance of DocumentClassifierDetails class.
     * 
     * @param createdDateTime the createdDateTime value to set.
     * @param apiVersion the apiVersion value to set.
     * @param docTypes the docTypes value to set.
     */
    @Generated
    @JsonCreator
    private DocumentClassifierDetails(@JsonProperty(value = "createdDateTime") OffsetDateTime createdDateTime,
        @JsonProperty(value = "apiVersion") String apiVersion,
        @JsonProperty(value = "docTypes") Map<String, ClassifierDocumentTypeDetails> docTypes) {
        this.createdDateTime = createdDateTime;
        this.apiVersion = apiVersion;
        this.docTypes = docTypes;
    }

    /**
     * Get the classifierId property: Unique document classifier name.
     * 
     * @return the classifierId value.
     */
    @Generated
    public String getClassifierId() {
        return this.classifierId;
    }

    /**
     * Get the description property: Document classifier description.
     * 
     * @return the description value.
     */
    @Generated
    public String getDescription() {
        return this.description;
    }

    /**
     * Get the createdDateTime property: Date and time (UTC) when the document classifier was created.
     * 
     * @return the createdDateTime value.
     */
    @Generated
    public OffsetDateTime getCreatedDateTime() {
        return this.createdDateTime;
    }

    /**
     * Get the expirationDateTime property: Date and time (UTC) when the document classifier will expire.
     * 
     * @return the expirationDateTime value.
     */
    @Generated
    public OffsetDateTime getExpirationDateTime() {
        return this.expirationDateTime;
    }

    /**
     * Get the apiVersion property: API version used to create this document classifier.
     * 
     * @return the apiVersion value.
     */
    @Generated
    public String getApiVersion() {
        return this.apiVersion;
    }

    /**
     * Get the baseClassifierId property: Base classifierId on top of which the classifier was trained.
     * 
     * @return the baseClassifierId value.
     */
    @Generated
    public String getBaseClassifierId() {
        return this.baseClassifierId;
    }

    /**
     * Get the docTypes property: List of document types to classify against.
     * 
     * @return the docTypes value.
     */
    @Generated
    public Map<String, ClassifierDocumentTypeDetails> getDocTypes() {
        return this.docTypes;
    }

    /**
     * Get the warnings property: List of warnings encountered while building the classifier.
     * 
     * @return the warnings value.
     */
    @Generated
    public List<Warning> getWarnings() {
        return this.warnings;
    }
}