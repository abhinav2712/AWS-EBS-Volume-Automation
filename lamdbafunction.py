import boto3
def extarctID(volume_arn):
    arn_parts=volume_arn.split(':')
    volume_id=arn_parts[-1].split('/')[-1]
    return volume_id
 
def lambda_handler(event, context): 
    # cloudwatch event is the event
    volume_arn=event['resources'][0]   # getting the first entry from resources
    volume_id=extarctID(volume_arn)  # getting the volume id using function
    # using boto3 client and modify the volume
    ec2_client= boto3.client('ec2')
    # using boto3 
    response = client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
    )
