def chunker(arr, batch_size, skip=None, complete=True):
    """ Chunk an array into smaller sequences

    batch_size:
        The number of elements in each chunk
    skip:
        If None, skips indices so that there is no overlap between chunks
    complete:
        For only returning batches that have length batch_size
    """
    if skip is None:
        skip = batch_size

    start = 0
    end = len(arr)
    for i in range(start, end, skip):
        batch = arr[i:i+batch_size]
        if not complete or len(batch) == batch_size:
            yield batch
        else:
            break
