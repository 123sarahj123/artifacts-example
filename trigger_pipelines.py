import time
import requests

def trigger_pipeline(pipeline_yaml):
    api_token = 'bkua_65d0c9a9178e156bac7d2aed6bfe3ec6d48345d1'
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        'pipeline': {
            'repository': 'https://github.com/123sarahj123/artifacts-example.git',
            'commit': 'master',
            'yaml': pipeline_yaml
        }
    }
    response = requests.post('https://api.buildkite.com/v2/organizations/sarahs-test-org/pipelines',
                             headers=headers,
                             json=payload)
    response.raise_for_status()
    print(f'Pipeline {pipeline_yaml} triggered successfully')

# Trigger the first pipeline
trigger_pipeline('pipeline.yml')

# Sleep for the desired time (0.3 seconds in this case)
# time.sleep(0.3)

# # Trigger the second pipeline
# trigger_pipeline('.buildkite/pipeline2.yml')