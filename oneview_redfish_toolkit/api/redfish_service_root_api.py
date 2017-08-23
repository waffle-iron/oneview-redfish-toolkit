# -*- coding: utf-8 -*-

# Copyright (2017) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from flask import jsonify
from flask import make_response
from flask_api import status
from flask_restful import Resource


class RedfishServiceRootAPI(Resource):
    def __init__(self, schema_dict):
        self.schema_dict = schema_dict

    def get(self):
        """Get Redfish service root.

            Return a validated Redfish service root JSON.

            Returns:
                JSON: print the JSON Redfish service root.
        """

        return make_response(jsonify({"service_root": "service_root"}),
                             status.HTTP_200_OK)
