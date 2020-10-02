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

# Prerequisites
Docker, AWS, Gmail, Twilio, Max of $15 a month to run this.

# Instructions
1. Create an AWS account or login to an existing account.
2. Create a new gmail account or login to an existing account.
3. Create a new twilio account or login to an existing account.
4. Go to the AWS Lambda console home page and select layers from the side menu.
5. Hit create layer. Enter in your layer name and upload twilio-layer.zip from the aws folder in this project.
6. From the Compatable runtimes dropdown select Python 3.8 and finally hit create. 
7. Go to the AWS Lambda console home page and select functions from the side menu.
8. Select Author from Scrath, type in your function name, change the runtime to Python 3.8, and hit create function.
9. Under Configuration=>Designer hit add trigger, select API Gateway, select Create an API, select HTTP API, and finally hit add. Save the URL for this web api for later.
10. In the AWS Lambda code editor for your function copy and paste leftovers.py text into the editor. Furthermore, select layers in the designer and choose the layer you created.
10. Login to your gmail account and open it to less secure apps. Save the email address and password for later.
11. Login to your twilio account and create a new phone number. Keep track of the twilio auth token and twilio SID for the number.
12. Go back to AWS Lambda and reselect your function, scroll down to the section for environment variables. Enter and fill out these 8 variables: FROM_ADDRESS, FROM_PASSWORD, FROM_PHONE, QUERY_LIST, TO_ADDRESS, TO_PHONE, TWILIO_AUTH, and TWILIO_SID. FROM_ADDRESS/FROM_PASSWORD are from the gmail account created in step 2. FROM_PHONE/TWILIO_SID/TWILIO_AUTH are from the twilio account in step 3. TO_ADDRESS is where emails are sent and TO_PHONE is where text messages are sent. Finally, QUERY_LIST is the list of dear/elk tag ids that you would like to track (ie. DM018O3R,DF018O3R). Format the query list with commas separating the codes.
13. Under the docker folder in this project edit your script.sh. Replace every instance of <AWS_LAMBDA_URL> with the url of your Web API lambda trigger. 
14. In the AWS ECS Console Home select repositories, and add a new repository with a unique name. Select your newly created repository and follow the instructions when you select "View Push Commands". Make sure to build the docker image from the Dockerfile in this project's docker folder.
15. In the AWS ECS Console Home select Clusters and then Get Started. Under the container definition=>custom select configure and enter in the information for your newly created image. Hit next until you create the new cluster with your image.
16. Enjoy quick notifications for when a tag is put up on the list.

# Support
Email me at djwehrlin@gmail.com or submit requests via github for changes

# Questions
INSERT QUESTIONS HERE