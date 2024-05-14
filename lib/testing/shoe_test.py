#!/usr/bin/env python3

from shoe import Shoe
import io
import sys
import pytest
from contextlib import redirect_stdout

class TestShoe:
    '''Test suite for the Shoe class in shoe.py'''

    @pytest.fixture
    def stan_smith(self):
        """Fixture to create a Shoe instance."""
        return Shoe("Adidas", 9)

    def test_has_brand_and_size(self, stan_smith):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9

    def test_requires_int_size(self, stan_smith):
        '''prints "size must be an integer" if size is not an integer.'''
        captured_out = io.StringIO()
        with redirect_stdout(captured_out):
            stan_smith.size = "not an integer"
        assert captured_out.getvalue() == "size must be an integer\n"

    def test_can_cobble(self, stan_smith):
        '''says that the shoe has been repaired.'''
        captured_out = io.StringIO()
        with redirect_stdout(captured_out):
            stan_smith.cobble()
        assert captured_out.getvalue() == "Your shoe is as good as new!\n"

    def test_cobble_makes_new(self, stan_smith):
        '''creates an attribute on the instance called 'condition' and sets it to 'New' after repair.'''
        stan_smith.cobble()
        assert stan_smith.condition == "New"

   
