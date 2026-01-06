from unittest import TestCase
from unittest.mock import patch

from constants import (
    BaseStats,
    DynamicValues,
    EffortValues,
    ExperienceGroup,
    Stat,
    Stats,
)
from calculations import (
    calculate_effort_value_given,
    calculate_stat,
    calculate_stats,
    get_experience,
)


class TestCalculation(TestCase):
    def setUp(self):
        self.levels = (25, 50, 75, 100)

    def test_calculate_stat(self):
        stats = (30, 55, 80, 105)
        hp_stats = (60, 110, 160, 210)
        for level, stat in zip(self.levels, stats):
            self.assertEqual(
                calculate_stat(
                    base_stat=50, dynamic_value=0, effort_value=0, level=level
                ),
                stat,
            )
        for level, hp_stat in zip(self.levels, hp_stats):
            self.assertEqual(
                calculate_stat(
                    base_stat=50,
                    dynamic_value=0,
                    effort_value=0,
                    level=level,
                    is_hp=True,
                ),
                hp_stat,
            )

    @patch("calculations.calculate_stat", return_value=100)
    def test_calculate_stats(self, calculate_stat_mock):
        base_stats = BaseStats(0, 0, 0, 0, 0, 0)
        dynamic_values = DynamicValues(0, 0, 0, 0, 0, 0)
        effort_values = EffortValues(0, 0, 0, 0, 0, 0)
        stats = calculate_stats(base_stats, dynamic_values, effort_values, level=50)
        print(type(stats))
        self.assertIsInstance(stats, Stats)
        calculate_stat_mock.assert_any_call(0, 0, 0, 50, is_hp=True)
        calculate_stat_mock.assert_any_call(0, 0, 0, 50, is_hp=False)
        for stat in Stat:
            self.assertEqual(stats[stat.value], 100)

    def test_calculate_effort_value_given(self):
        base_stats = BaseStats(70, 130, 100, 55, 80, 65)
        stage = 2
        self.assertEqual(
            calculate_effort_value_given(base_stats, stage),
            ("Attack", 2)
        )

    def test_get_experience_at_level_one(self):
        self.assertEqual(0, get_experience(experience_group=None, level=1))

    def test_get_experience_slow(self):
        experiences = (19_531, 156_250, 527_343, 1_250_000)
        for level, experience in zip(self.levels, experiences):
            self.assertEqual(get_experience(ExperienceGroup.SLOW, level), experience)

    def test_get_experience_medium_slow(self):
        level_exp_pairs = [(25, 11_735), (50, 117_360), (75, 429_235), (100, 1_059_860)]
        for level, experience in level_exp_pairs:
            self.assertEqual(
                get_experience(ExperienceGroup.MEDIUM_SLOW, level), experience
            )

    def test_get_experience_medium_fast(self):
        level_exp_pairs = [(25, 15_625), (50, 125_000), (75, 421_875), (100, 1_000_000)]
        for level, experience in level_exp_pairs:
            self.assertEqual(
                get_experience(ExperienceGroup.MEDIUM_FAST, level), experience
            )

    def test_get_experience_fast(self):
        level_exp_pairs = [(25, 12_500), (50, 100_000), (75, 337_500), (100, 800_000)]
        for level, experience in level_exp_pairs:
            self.assertEqual(get_experience(ExperienceGroup.FAST, level), experience)

    def test_get_experience_erratic(self):
        level_exp_pairs = [(25, 23_437), (50, 125_000), (75, 326_531), (100, 600_000)]
        for level, experience in level_exp_pairs:
            self.assertEqual(get_experience(ExperienceGroup.ERRATIC, level), experience)

    def test_get_experience_fluctuating(self):
        level_exp_pairs = [(25, 12_187), (50, 142_500), (75, 582_187), (100, 1_640_000)]
        for level, experience in level_exp_pairs:
            self.assertEqual(
                get_experience(ExperienceGroup.FLUCTUATING, level), experience
            )
