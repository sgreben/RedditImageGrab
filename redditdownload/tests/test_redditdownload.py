#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase
from os import getcwd

from redditdownload import parse_args, process_deviant_url


class TestParseArgs(TestCase):
    def test_simple_args(self):
        ARGS = parse_args(['funny'])
        self.assertEqual(ARGS.reddit, 'funny')
        self.assertEqual(ARGS.dir, getcwd())

    def test_multiple_reddit_plus(self):
        ARGS = parse_args(['funny+anime'])
        self.assertEqual(ARGS.reddit, 'funny+anime')

    def test_nsfw_sfw_arg(self):
        ARGS = parse_args(['--nsfw --sfw'])
        self.assertFalse(ARGS.nsfw)
        self.assertFalse(ARGS.sfw)


class TestProcessDeviantUrl(TestCase):
    def setUp(self):
        self.url = 'http://shortethan.deviantart.com/art/Bumbleby-Shirts-495533842'
        # actual link is :
        # http://www.deviantart.com/download/495533842/bumbleby_shirts_by_shortethan-d8710cy.png?token=a5c45dc54b928b8a9622203db5142f9b5e1c3e7f&ts=1440638185
        # token may change per request
        self.not_full_download_url = ('http://www.deviantart.com/download/'
                                      '495533842/bumbleby_shirts_by_shortethan-d8710cy.png')

    def test_link_with_download_button(self):
        result_url = process_deviant_url(self.url)
        # result_url is a list, contain one or more pic
        self.assertIsInstance(result_url, list)
        self.assertIn(self.not_full_download_url, result_url[0])
        self.assertGreaterEqual(len(result_url), 1)

if __name__ == '__main__':
    unittest.main()
