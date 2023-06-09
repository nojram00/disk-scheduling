def look_disk_scheduling(requests, start):
    head_direction = 1  # 1 for moving upwards, -1 for moving downwards
    total_seek_count = 0
    current_track = start
    visited_tracks = []

    while True:
        # Check if there are any pending requests in the current direction
        pending_requests = [req for req in requests if head_direction * (req - current_track) >= 0]

        if not pending_requests:
            # If there are no pending requests, reverse the direction
            head_direction *= -1
            continue

        # Find the closest request in the current direction
        next_track = min(pending_requests, key=lambda x: abs(x - current_track))

        # Calculate the seek count to move to the next track
        seek_count = abs(next_track - current_track)
        total_seek_count += seek_count

        # Move the head to the next track
        current_track = next_track

        # Remove the processed request from the list
        requests.remove(next_track)

        # Add the current track to the visited tracks
        visited_tracks.append(current_track)

        if not requests:
            # If all requests have been processed, break the loop
            break

    return visited_tracks, total_seek_count


# Example usage
# requests = [98, 183, 37, 122, 14, 124, 65, 67]
# start_track = 53
#
# visited, seek_count = look_disk_scheduling(requests, start_track)
#
# print("Visited Tracks:", visited)
# print("Total Seek Count:", seek_count)
