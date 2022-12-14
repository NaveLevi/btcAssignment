
How To Build and Deploy btcAssignment
---
- Fork the repository.
- Make sure you have Azure CLI installed and log into your Azure acocunt using the `az login` command.  
The following will create a service-principle, so the workflows on Github will be able to access your account.
Copy the json output as a secret to your GitHub repo. The secret should be called `AZURE_CREDENTIALS`.  
```
az ad sp create-for-rbac --name "Github" --role owner --scopes "<subscription-id>" --sdk-auth
```
[More Details](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure?tabs=azure-cli%2Clinux)

- Create a fine-grained personal access token on GitHub and copy it as a secret in your GitHub repo. The secret should be called `GH_TOKEN`.  
[Explanation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)  
[Settings page](https://github.com/settings/personal-access-tokens/new)  
The only required permission is Secrets.

- Create Dockerhub repos for both of the microservices -  bitcoin-fetcher and empty-responder.  
I looked into automating the creation of the repos, but it's not officially supported in the API, and the solution I found is too hacky and requires the user to export his Dockerhub password on Github.
- Create a Dockerhub access token and copy it as a secret to GitHub. It should be called `DOCKERHUB_TOKEN` - [Link to Dockerhub Settings](https://hub.docker.com/settings/security).  
Create a `DOCKERHUB_USERNAME` secret with your Dockerhub username.
- Run the create-cluster GitHub workflow, which will also trigger the deployment of ingress-nginx and the microservices.  
You can see the LoadBalancer IP in the output of the deploy-ingress-nginx workflow.  
From that point forward, you no longer need to manually deploy anything, the microsevices will be built and redeployed automatically with each code change you make.


After you're done, you can run the delete-cluster workflow to delete the cluster, the GitHub kubeconfig secret and all of its resources.