import boto3
import csv

# Initialize Boto3 clients
session = boto3.Session()
compute_optimizer_client = session.client('compute-optimizer', region_name='ap-south-1')

# Retrieve EC2 instance recommendations
def retrieve_ec2_instance_recommendations():
    try:
        response = compute_optimizer_client.get_ec2_instance_recommendations()

        if 'instanceRecommendations' in response:
            recommendations = response['instanceRecommendations']
            return recommendations

        return []

    except Exception as e:
        print(f"Error retrieving EC2 instance recommendations: {e}")
        return []

# Retrieve EBS volume recommendations
def retrieve_ebs_volume_recommendations():
    try:
        response = compute_optimizer_client.get_ebs_volume_recommendations()

        if 'volumeRecommendations' in response:
            recommendations = response['volumeRecommendations']
            return recommendations

        return []

    except Exception as e:
        print(f"Error retrieving EBS volume recommendations: {e}")
        return []

# Create CSV file with EC2 instance recommendations
def create_ec2_recommendations_csv(recommendations):
    try:
        with open('ec2_compute_optimizations.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Instance ID', 'Instance Name', 'Current Type', 'Recommendation Options',
                             'Projected Utilization Metrics Name', 'Projected Utilization Metric Value',
                             'Savings Opportunity Percentage', 'Savings Opportunity Cost $'])

            for recommendation in recommendations:
                if recommendation['recommendationOptions']:
                    if recommendation['finding'] == 'OVER_PROVISIONED':
                        instance_id = recommendation['instanceArn'].split('/')[-1]
                        instance_name = recommendation['instanceName']
                        instance_type = recommendation['currentInstanceType']

                        for item in recommendation['recommendationOptions']:
                            if 'savingsOpportunity' in item:
                                recommendation_options = item['instanceType']
                                projected_utilization_metrics_name = item['projectedUtilizationMetrics'][0]['name']
                                projected_utilization_metric_value = item['projectedUtilizationMetrics'][0]['value']
                                savings_opportunity_percentage = item['savingsOpportunity']['savingsOpportunityPercentage']
                                savings_opportunity_cost = item['savingsOpportunity']['estimatedMonthlySavings']['value']

                                writer.writerow([instance_id, instance_name, instance_type, recommendation_options,
                                                 projected_utilization_metrics_name, projected_utilization_metric_value,
                                                 savings_opportunity_percentage, savings_opportunity_cost])

                        writer.writerow([])  # Blank row after each recommendation

        print("CSV file with EC2 instance recommendations created successfully.")

    except Exception as e:
        print(f"Error creating CSV file with EC2 instance recommendations: {e}")

# Create CSV file with EBS volume recommendations
# Create CSV file with EBS volume recommendations
def create_ebs_recommendations_csv(recommendations):
    try:
        with open('ebs_compute_optimizations.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Volume ID', 'Volume Type', 'Recommendation Options Volume Type', 'Volume Size',
                             'Recommendation Options Volume Size', 'Volume Baseline IOPS',
                             'Recommendation Options Baseline IOPS', 'Volume Burst IOPS',
                             'Recommendation Options Burst IOPS', 'Volume Baseline Throughput',
                             'Recommendation Options Baseline Throughput', 'Volume Burst Throughput',
                             'Recommendation Options Burst Throughput', 'Savings Opportunity Percentage',
                             'Estimated Monthly Savings'])

            for recommendation in recommendations:
                if recommendation['finding'] == 'NotOptimized':
                    volume_id = recommendation['volumeArn'].split('/')[-1]
                    volume_type = recommendation['currentConfiguration']['volumeType']
                    recommendation_options_volume_type = recommendation['volumeRecommendationOptions'][0]['configuration']['volumeType']
                    volume_size = recommendation['currentConfiguration']['volumeSize']
                    recommendation_options_volume_size = recommendation['volumeRecommendationOptions'][0]['configuration']['volumeSize']
                    volume_baseline_iops = recommendation['currentConfiguration']['volumeBaselineIOPS']
                    recommendation_options_baseline_iops = recommendation['volumeRecommendationOptions'][0]['configuration']['volumeBaselineIOPS']
                    volume_burst_iops = recommendation['currentConfiguration']['volumeBurstIOPS']
                    recommendation_options_burst_iops = recommendation['volumeRecommendationOptions'][0]['configuration']['volumeBurstIOPS']
                    volume_baseline_throughput = recommendation['currentConfiguration']['volumeBaselineThroughput']
                    recommendation_options_baseline_throughput = recommendation['volumeRecommendationOptions'][0]['configuration']['volumeBaselineThroughput']
                    volume_burst_throughput = recommendation['currentConfiguration']['volumeBurstThroughput']
                    recommendation_options_burst_throughput = recommendation['volumeRecommendationOptions'][0]['configuration']['volumeBurstThroughput']

                    # Assign default values to savings_opportunity_percentage and estimated_monthly_savings
                    savings_opportunity_percentage = ""
                    estimated_monthly_savings = ""

                    if 'savingsOpportunity' in recommendation['volumeRecommendationOptions'][0]:
                        savings_opportunity_percentage = recommendation['volumeRecommendationOptions'][0]['savingsOpportunity']['savingsOpportunityPercentage']
                        estimated_monthly_savings = recommendation['volumeRecommendationOptions'][0]['savingsOpportunity']['estimatedMonthlySavings']['value']

                        writer.writerow([volume_id, volume_type, recommendation_options_volume_type, volume_size,
                                     recommendation_options_volume_size, volume_baseline_iops,
                                     recommendation_options_baseline_iops, volume_burst_iops,
                                     recommendation_options_burst_iops, volume_baseline_throughput,
                                     recommendation_options_baseline_throughput, volume_burst_throughput,
                                     recommendation_options_burst_throughput, savings_opportunity_percentage,
                                     estimated_monthly_savings])

        print("CSV file with EBS volume recommendations created successfully.")

    except Exception as e:
        print(f"Error creating CSV file with EBS volume recommendations: {e}")

# Retrieve EC2 instance recommendations
ec2_recommendations = retrieve_ec2_instance_recommendations()

# Create CSV file with EC2 instance recommendations
create_ec2_recommendations_csv(ec2_recommendations)

# Retrieve EBS volume recommendations
ebs_volume_recommendations = retrieve_ebs_volume_recommendations()

# Create CSV file with EBS volume recommendations
create_ebs_recommendations_csv(ebs_volume_recommendations)