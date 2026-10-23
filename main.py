from test_frame_stats import get_frame_stats

if __name__ == "__main__":
    # Sample frame data simulation
    sample_frame = [12, 45, 78, 23, 90]
    
    print("Processing frame data in Docker container...")
    stats = get_frame_stats(sample_frame)
    print(f"Results: {stats}")
