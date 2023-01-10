import boto3

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    filter = [{
            'Name': 'tag:Name',
            'Values': ['test-lambd-klb']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopedd']
        }]

    instances = ec2.instances.filter(Filters=filter)
    for instance in instances:
        instance.start()
    
    return 'Sucess'