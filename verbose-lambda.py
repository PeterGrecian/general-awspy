def handler(event, context):
    print("context:", context)
    print("event:", event)

    return {
        'statusCode': 200,
        'body': "",
        'headers': {
            'Content-Type': 'text/html',
        }
    }

