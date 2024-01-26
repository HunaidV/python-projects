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
    bucket_name = "your-bucket-name",
    source_file_name = "<use pwd command followed by / then file name>",
    destination_blob_name = "File name you want to add in gcp storage",
    base64_encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
    )