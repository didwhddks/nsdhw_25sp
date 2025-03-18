import pytest
import math
from vector_angle import vector_angle, Vector2D

def test_vector_angle():
    v1 = Vector2D(1, 0)
    v2 = Vector2D(0, 1)
    assert math.isclose(vector_angle(v1, v2), math.pi / 2, rel_tol=1e-6)

    v3 = Vector2D(1, 1)
    v4 = Vector2D(-1, -1)
    assert math.isclose(vector_angle(v3, v4), math.pi, rel_tol=1e-6)

    v5 = Vector2D(1, 1)
    v6 = Vector2D(1, -1)
    assert math.isclose(vector_angle(v5, v6), math.pi / 2, rel_tol=1e-6)

    v7 = Vector2D(1, 0)
    v8 = Vector2D(1, 0)
    assert math.isclose(vector_angle(v7, v8), 0.0, rel_tol=1e-6)

    with pytest.raises(ValueError):
        vector_angle(Vector2D(0, 0), Vector2D(1, 1))

if __name__ == "__main__":
    pytest.main()