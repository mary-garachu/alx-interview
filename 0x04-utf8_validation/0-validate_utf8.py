def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each integer in the data
    for byte in data:
        # Only look at the 8 least significant bits
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If num_bytes is 0, it's a 1-byte character
            if num_bytes == 0:
                continue

            # Characters should be between 2 and 4 bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to process
        num_bytes -= 1

    # If we finished processing all bytes, num_bytes should be 0
    return num_bytes == 0
