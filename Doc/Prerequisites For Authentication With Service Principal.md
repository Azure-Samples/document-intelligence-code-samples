# Prerequisites For Authentication With Service Principal

In this article, you'll learn how to create Azure AI Service, Microsoft Entra application and service principal that can be used with role-based access control (RBAC). When you register a new application in Microsoft Entra ID, a service principal is automatically created for the app registration. The service principal is the app's identity in the Microsoft Entra tenant. Access to resources is restricted by the roles assigned to the service principal, giving you control over which resources can be accessed and at which level.

## Create Azure AI Service
Create a [single-service](https://aka.ms/single-service) or [multi-service](https://aka.ms/multi-service) resource. You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.

## Register an application with Microsoft Entra ID and create a service principal
For this process, it could reference the [doc section](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#register-an-application-with-microsoft-entra-id-and-create-a-service-principal) completely.

## Assign a role to the application
1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Select the Azure AI Service which created in previous steps.
3. Select **Access control (IAM)**.
4. Select **Add**, then select **Add role assignment**.
5. In the **Role** tab, select the **"Cognitive Services User"**
6. Select Next.
7. On the **Members** tab, for **Assign access to**, select **User, group, or service principal**.
8. Select **Select members**. By default, Microsoft Entra applications aren't displayed in the available options. To find your application, search for it by the name which register in previous steps.
9. Select the Select button, then select Review + assign.

## Set up authentication
Reference the [document](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#set-up-authentication), there're three options to set up authentication.
For the sample in repo, it's used [option 3](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret).

So far, all the parameters will be used in the sample programs, it could be obtained from above resouces.
1) DOCUMENTINTELLIGENCE_ENDPOINT - the endpoint to your Document Intelligence resource.
2) DOCUMENTINTELLIGENCE_TENANT_ID - your Azure tenant id.
3) DOCUMENTINTELLIGENCE_CLIENT_ID - the Application (client) ID of Microsoft Entra App.
4) DOCUMENTINTELLIGENCE_CLIENT_SECRET - the Client Secrets of Microsoft Entra App.

