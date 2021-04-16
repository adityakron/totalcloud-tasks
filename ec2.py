# This giving for only one region 
import boto3

ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print (instance.id , instance.state)
    
# For all region 

 for region in `aws ec2 describe-regions --output text | cut -f3`
do
     echo -e "\nInstances status in region: '$region'"
     aws ec2 describe-instance-status --include-all-instances
done
