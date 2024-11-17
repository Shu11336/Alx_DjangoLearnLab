Step 1: Configure Authentication
Installed Token Authentication: Added rest_framework.authtoken to INSTALLED_APPS in settings.py.

Database Setup: Executed python manage.py migrate to create the necessary database tables for token management.

Updated DRF Settings: Configured settings.py to include token authentication by adding TokenAuthentication to 
DEFAULT_AUTHENTICATION_CLASSES.

Step 2: Generate and Use Tokens
Token Retrieval Endpoint: Implemented an endpoint using DRF’s obtain_auth_token view that allows users to obtain a token
by providing their username and password.

Step 3: Define Permission Classes
Configured Permissions: Utilized rest_framework.permissions to apply IsAuthenticated and IsAdminUser permissions, along
with custom permissions as needed, to control access based on user roles and authentication status.

Updated ViewSet Permissions: Modified configurations in ViewSets to include the appropriate permission classes ensuring

secure API access.
Step 4: Test Authentication and Permissions
Authentication Testing: Used Postman to send authenticated and unauthenticated requests to the API endpoints to verify
that permissions are correctly enforced, ensuring only authorized users could access certain resources.