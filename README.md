## Leftovers Notification Application
# Description
Alert System for Colorado Department of Wildlife's Leftover Dear/Elk Tags
Uses Amazon Web Services to create a simple notificaion service
Files
    * code.zip- The code that should be imported into lambda function
    * layer.zip- The layer/libraries that should be imported into lambda function
    * leftovers.py- The lambda function which performs the service
    * leftovers_stack.template- The CloudFormation template used to create lambda function
    * LICENSE- MIT license which makes this open source

# Instructions
1. Create or login to an AWS account.
2. Create a new role with a policy of AWSLambdaFullAccess
3. Create a new AWS S3 bucket and upload the code.zip and the layer.zip files.
4. Add new layer in AWS Lambda Service and use layer.zip from previous step
5. Create a new gmail account and open it to less secure apps
6. Create a Twilio account and startup a new phone number
7. Edit the leftovers_stack.template
    1. Change Code:S3Bucket and Code:S3Key to match your code.zip location
    2. Change the necessarry variables under Properties:Environment
    3. Add the ARN of layer.zip file you uploaded into the Layers List
    4. Add the ARN of the role you created in step 2 into the Roles property
8. Deploy the CloudFormation template from the website
9. Enter parameters for new stack in CloudFormation service
10. DONE!

# Support
Email me @ djwehrlin@gmail.com or submit requests via github for changes

# Questions
INSERT QUESTIONS HERE