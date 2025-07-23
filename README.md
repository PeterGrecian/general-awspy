## cloudwatch_logs.py<br>
mimic aws logs tail <log_group> --follow
* get_latest_log_stream(log_group_name)<br>
* get_log_events(log_group, log_stream)<br>

## s3_commands.py
mimic aws s3 commands
* cp(local_file, bucket_name, s3_object_key)<br>
* rm(bucket_name, s3_object_key)<br>
* ls(bucket_name)<br>
* cp_back(bucket_name, s3_object_key, local_file)<br>
* rm_all(bucket_name)<br>

## verbose_lambda.py
prints context and event
