expected_result = "11"
actual_result = "11"
if expected_result != actual_result:
    print("expected " + expected_result + ", got " + actual_result)

"""Так тоже можно: assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)"""
