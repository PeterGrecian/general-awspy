logs_client = boto3.client("logs")
"""
# There can be multiple lambda START-REPORT blocks
# in a stream and we want the one associated with the current invocation
# Because this is asynchronous, it is possible that, for example, the blocks
# are in the wrong order etc.

# if the interval between lambda invocations is short, a new log stream may not be created
# so the timestamps on the log events should be used to determine the latest log stream

# the blocks have a unique RequestId but s3 cp in the test does not know what it is.
# metadata can be added to the cp which is reflected in the block.

# I'm worried about 2 simultanious invocations of the same script...

"""

def get_latest_log_stream(log_group_name):

    try:
        response = logs_client.describe_log_streams(
            logGroupName=log_group_name,
            orderBy="LastEventTime",
            descending=True,
            limit=1,
        )

        log_streams = response.get("logStreams", [])
        if log_streams:
            return log_streams[0]["logStreamName"]
        else:
            return None
    except Exception as e:
        print(f"Error getting latest log stream: {e}")
        return None


def get_log_events(log_group, log_stream):
    response = logs_client.get_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        startFromHead=True,  # True to start from the beginning of the stream
    )
    return response['events']


# wait for the latest_log_stream to change
time.sleep(1)
while new_log_stream == log_stream:
    print("Waiting stream...", new_log_stream[-4:])
    # is the last timestamp in the log newer than the trigger time?
    log = get_log_events(log_group, log_stream)
    last_ts = log[-1]['timestamp'] 
    print(trigger_time, last_ts, last_ts - trigger_time)      

    if last_ts > trigger_time: # new lines in log
        break

    time.sleep(3)
    new_log_stream = get_latest_log_stream(log_group)

log = get_log_events(log_group, new_log_stream)
for event in log:
    if event['timestamp'] > trigger_time:
        print(event['timestamp'] - trigger_time, event['message'].strip())

