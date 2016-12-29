
# Steps to Use

First familize yourself with some of the example alexa skills

https://github.com/amzn/alexa-skills-kit-js  has some good examples

then create your own skill, using the intents, sample_utterances, and custom_slots files

## additional things needed in aws beyond the standard examples:

* Create of a dynamo db table named "game" with 5 read & write units
* to your " lambda_basic_execution" IAM role, add the AmazonDynamoDBFullAcess policy



