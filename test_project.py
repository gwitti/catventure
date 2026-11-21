import unittest
import pygame
from unittest.mock import MagicMock, patch
from project import display_score, Cat, Drop


class TestDisplayScore(unittest.TestCase):

    @patch('pygame.time.get_ticks', return_value=5000)
    def test_display_score(self, screen_mock):

        test_font_mock = MagicMock()
        surface_mock = MagicMock(spec=pygame.Surface)
        screen_mock = MagicMock()
        screen_mock.blit = MagicMock()
        test_font_mock.render.return_value = surface_mock
        get_rect_mock = surface_mock.get_rect.return_value

        with patch('pygame.font.Font', return_value=test_font_mock), \
             patch('pygame.display.update'), \
             patch('pygame.time.get_ticks', return_value=10000):

            start_time = 5
            result = display_score(start_time, test_font_mock, screen_mock)
            current_time = int(pygame.time.get_ticks() / 1000) - start_time

        self.assertEqual(result, current_time)
        test_font_mock.render.assert_called_once_with('Score: 5', False, (125, 74, 176))
        surface_mock.get_rect.assert_called_once_with(center=(400, 80))
        screen_mock.blit.assert_called_once_with(surface_mock, get_rect_mock)


class TestCatAnimation(unittest.TestCase):

    def setUp(self):
        self.my_cat = Cat()
        self.my_cat.cat_surface = None
        self.my_cat.cat_index = 0
        self.my_cat.cat_jump = MagicMock()
        self.my_cat.cat_step = [MagicMock(), MagicMock()]

        self.my_cat.cat_rect = MagicMock()
        self.my_cat.cat_rect.bottom = 430

    def test_cat_animation_jump(self):
        self.my_cat.cat_rect.bottom = 340
        self.my_cat.cat_animation()
        self.assertEqual(self.my_cat.cat_surface, self.my_cat.cat_jump)

    def test_cat_animation_step(self):
        self.my_cat.cat_rect.bottom = 430
        self.my_cat.cat_animation()
        self.assertEqual(self.my_cat.cat_surface, self.my_cat.cat_step[int(self.my_cat.cat_index)])



class TestDropAnimation(unittest.TestCase):

    def setUp(self):
        self.jump_drop = Drop()
        self.jump_drop.drop_index = 0
        self.jump_drop.drop = [MagicMock(), MagicMock()]
        self.jump_drop.drop_surface = self.jump_drop.drop[0]

    def test_drop_animation(self):
        self.assertEqual(self.jump_drop.drop_surface, self.jump_drop.drop[int(self.jump_drop.drop_index)])



if __name__ == '__main__':
    unittest.main()
