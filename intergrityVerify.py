import hashlib

def verify_integrity(file_path, expected_hash):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest() == expected_hash

# Example usage
# file_path = './file.zip'
# expected_hash = 'your_expected_sha256_hash_here'
# if verify_integrity(file_path, expected_hash):
#     print("File integrity verified.")
# else:
#     print("File integrity check failed.")
