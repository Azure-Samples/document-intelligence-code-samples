# Prerequisites For Authentication With User-Assigned Managed Identity

In this article, you'll learn how to create Azure AI Service, and administrators can assign a role to an user-assigned managed identity.

## Create Azure AI Service
Create a [single-service](https://aka.ms/single-service) or [multi-service](https://aka.ms/multi-service) resource. You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.

## Assign A Role to User By Administrator
1. Sign in to the [Azure portal](https://portal.azure.com/) with administrator privileges.
2. Select the Azure AI Service which created in previous steps.
3. Select **Access control (IAM)**.
4. Select **Add**, then select **Add role assignment**.
5. In the **Role** tab, select the **"Cognitive Services User"**
6. Select Next.
7. On the **Members** tab, for **Assign access to**, select **User, group, or service principal**.
8. Select **Select members**, and choose the user who should have the role assigned.
9. Select the "Select" button, then select "Review + assign".

So far, the parameters will be used in the sample programs, it could be obtained from above resouces.
1) DOCUMENTINTELLIGENCE_ENDPOINT - the endpoint to your Document Intelligence resource.


