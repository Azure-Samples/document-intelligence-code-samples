# Convert Office File To Pdf Format By Microsoft Graph API

## Overview
Microsoft Graph API Provide a good way to convert office file to pdf format. Let’s take a quick look at the functional core. The API of [Download a file in another format](https://learn.microsoft.com/en-us/graph/api/driveitem-get-content-format?view=graph-rest-1.0&tabs=http) support a lot of file type, briefly as below:

| Format value | Description | Supported source extensions |
| ------------ | ----------- | --------------------------- |
| pdf | Converts the item into PDF format. | csv, doc, docx, odp, ods, odt, pot, potm, potx, pps, ppsx, ppsxm, ppt, pptm, pptx, rtf, xls, xlsx |
| html | Converts the item into HTML format. | loop, fluid, wbtx |

It almost supports convert all the MS Office document formats to pdf with good quality. Before using this API, you need to understand the authentication and authorization concepts in the Microsoft identity platform. 

## Prerequisites
- A Microsoft Entra ID tenant. If you don't have a tenant, create a [free Azure account to get free subscription](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- An account that has at least the [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json#cloud-application-administrator) role.
- The <a name="drive">drive</a> resource to storage file, it could be [OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage/), [OneDrive for business](https://www.microsoft.com/en-us/microsoft-365/onedrive/onedrive-for-business), or [Sharepoint](https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration). For enterprise scenario, suggest [Sharepoint](https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration).

## Process
There is a comprehensive documentation about [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/overview). Due to Microsoft Graph API has a wide function range, it only summarizes the topics related to Microsoft Office file conversion, in this article.

### 1. Register the app in Microsoft Identity Platform
To call Microsoft Graph, an app must obtain an access token from the Microsoft identity platform. To register the app in Microsoft Identity Platform, reference the steps from https://learn.microsoft.com/en-us/graph/auth-register-app-v2.

### 2. Authentication and authorization basics
As previous step introduced, the app could obtain the access token. The access token includes information about whether the app is authorized to access Microsoft Graph on behalf of a signed-in user or with its own identity. 
- Access scenarios introduce : https://learn.microsoft.com/en-us/graph/auth/auth-concepts#access-scenarios. For enterprise scenario, suggest **Get access without a user**
- Get access without a user : https://learn.microsoft.com/en-us/graph/auth-v2-service?tabs=http
    + Extension - OAuth 2.0 client credentials flow : https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow
    + Extension - OAuth 2.0 client credentials flow by SDK : https://learn.microsoft.com/en-us/graph/sdks/choose-authentication-providers?view=graph-rest-1.0#client-credentials-provider

### 3. Create temporary folder by Microsoft Graph API
After getting the access token, it could use the Microsoft Graph API now. 
You'd better to create a temporary folder to store the Microsoft Office file by *[API: Create a new folder in a drive](https://learn.microsoft.com/en-us/graph/api/driveitem-post-children?view=graph-rest-1.0&tabs=http)*. For temporary folder, it's a file transfer station. Once the conversion is complete, this temporary folder and sub files can be deleted easily.


### 4. Upload the Microsoft Office file to drive by Microsoft Graph API
When the temporary folder is ready, could upload the Microsoft Office file to the temporary folder in <a href="#drive">drive</a> by *[API: Upload or replace the contents of a driveItem](https://learn.microsoft.com/en-us/graph/api/driveitem-put-content?view=graph-rest-1.0&tabs=http)*. Up to this step, you have made the full preparations for Microsoft Office file conversion.

### 5. Convert the Microsoft Office file to pdf format by Microsoft Graph API
Here's the key step, just calling the *[API: Download a file in another format](https://learn.microsoft.com/en-us/graph/api/driveitem-get-content-format?view=graph-rest-1.0&tabs=http)* to convert the Microsoft Office file to pdf format and save it to your local. <br>
Notice: the parameters of ***format*** should be ***pdf***

- #### Sample code for Python:
    ~~~
    query_params = ContentRequestBuilder.ContentRequestBuilderGetQueryParameters(
        format="pdf",
    )
    request_config = ContentRequestBuilder.ContentRequestBuilderGetRequestConfiguration(
        query_parameters=query_params
    )
    pdf_bytes = (
        await graph_client.drives.by_drive_id(user_drive_id)
        .items.by_drive_item_id(file_item.id)
        .content.get(request_config)
    )

    pdf_abspath = os.path.abspath(
        os.path.join(
            save_dir_path,
            f"./{file_name}.pdf",
        )
    )
    ~~~

- #### Sample code for C#:
    ~~~
    using var pdfStream = await graphClient.Drives[driveId].Items[fileItem.Id].Content.GetAsync((requestConfiguration) =>
    {
        requestConfiguration.QueryParameters.Format = "pdf";
    });

    if (pdfStream != null)
    {
        var savePdfFileName = $"{saveDirPath}\\{fileName}.pdf";
        using FileStream saveStream = File.Create(savePdfFileName);
        pdfStream.CopyTo(saveStream);
    }
    ~~~

### 6. Delete temporary folder by Microsoft Graph API
After converting Microsoft Office file to pdf format successfully, it's better to delete the temporary folder which used to store Microsoft Office file to keep the drive clear. You could implement this behavior by ***[API:Delete a DriveItem](https://learn.microsoft.com/en-us/graph/api/driveitem-delete?view=graph-rest-1.0&tabs=http)***.

This is an introduction for complete process of converting Microsoft Office file to pdf format. You could integrate the above related APIs in your exist system to achieve this feature.