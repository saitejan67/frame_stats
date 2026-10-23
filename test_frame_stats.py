import pytest

# Target function simulating frame statistic calculations
def get_frame_stats(frame_data):
    if not frame_data:
        return {"count": 0, "average": 0.0}
    
    # Validation checking for out-of-range pixel values (0-255)
    for val in frame_data:
        if val < 0 or val > 255:
            raise ValueError("Pixel value out of range (0-255)")
            
    return {"count": len(frame_data), "average": sum(frame_data) / len(frame_data)}


# 1. Normal Value Test
def test_frame_stats_normal():
    result = get_frame_stats([10, 20, 30])
    assert result == {"count": 3, "average": 20.0}


# 2. Empty Value Test
def test_frame_stats_empty():
    result = get_frame_stats([])
    assert result == {"count": 0, "average": 0.0}


# 3. Out-of-Range Value Test
def test_frame_stats_out_of_range():
    with pytest.raises(ValueError, match="Pixel value out of range"):
        get_frame_stats([256, 12, -5])
