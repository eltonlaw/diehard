def chunker(arr, batch_size, overlapping=False, complete=False):
    """ Chunk an array into smaller sequences

    complete:
        For only returning batches that have length n
    overlapping:
        For generating batches that overlap
    """
    skip = batch_size
    if overlapping:
        skip = 1

    start = 0
    end = len(arr)
    for i in range(start, end, skip):
        batch = arr[i:i+batch_size]
        if not complete or len(batch) == batch_size:
            yield batch
        else:
            break

