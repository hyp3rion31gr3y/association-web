#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest #this imports pytest package
import django # this imports django package

def test_current_django_version(): #def is used to create a function
    assert django.VERSION >= (1, 6, 1)


if __name__ == '__main__':
    pytest.main()
