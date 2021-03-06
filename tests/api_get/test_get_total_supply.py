# -*- coding: utf-8 -*-
# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import TestCase, main

from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from tests.example_config import BASE_DOMAIN_URL_V3_FOR_TEST, VERSION_FOR_TEST


class TestGetTotalSupply(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.icon_service = IconService(HTTPProvider(BASE_DOMAIN_URL_V3_FOR_TEST, VERSION_FOR_TEST))

    def test_get_total_supply(self):
        # case 0: when calling the method successfully
        result = self.icon_service.get_total_supply()
        self.assertTrue(isinstance(result, int))


if __name__ == "__main__":
    main()
