from task_16_5.task_16_5 import sum_up_song_times


def test_sum_up_song_times():
    assert sum_up_song_times([["Halo", 4.9], ["Clean", 5.83]], "Clean", 4.9) == 10.73
