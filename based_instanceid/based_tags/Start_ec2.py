import boto3

region = 'us-east-1'
instances = ['i-008aa0b958346b8b4', 'i-098146c31bc1b4893']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('stopping instances: ' + str(instances))
