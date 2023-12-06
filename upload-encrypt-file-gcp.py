import base64

from google.cloud import storage 

def bucket_blob_file(
    bucket_name,
    source_file_name,
    destination_blob_name,
    base64_encryption_key
):
    

    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    
    encryption_key = base64.b64decode(base64_encryption_key)
    blob = bucket.blob(
        destination_blob_name, encryption_key=encryption_key
    )
    
    
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)
    if True:
        print(
            f"File {source_file_name} uploaded to {destination_blob_name}."
        )
    else:
        print("file is not uploaded")

bucket_blob_file(
    bucket_name = "test-enabill-gcp-productionapi",
    source_file_name = "/Users/hunaidv/Documents/GCP-django-k8s/Python_Projects/GCP-Python-scripts/key.json",
    destination_blob_name = "key.json",
    base64_encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
    )