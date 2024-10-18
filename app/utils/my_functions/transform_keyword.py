def transform_keyword(data):
    # Transform the data into the desired format
    transformed_data = [{"text": key, "value": value} for key, value in data.items()]
    
    # Sort the transformed data by 'value' in descending order and take the top 100 items
    sorted_data = sorted(transformed_data, key=lambda x: x['value'], reverse=True)[:100]
    
    return sorted_data