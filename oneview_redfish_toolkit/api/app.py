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

from flask import Flask
from flask_restful import Api

from oneview_redfish_toolkit.api.redfish_base_api import RedfishBaseAPI
from oneview_redfish_toolkit.api.redfish_service_root_api \
    import RedfishServiceRootAPI

app = Flask(__name__)

api = Api(app)
api.add_resource(RedfishBaseAPI, "/redfish/",
                 resource_class_kwargs={"schema_dict": {}})
api.add_resource(RedfishServiceRootAPI, "/redfish/v1/",
                 resource_class_kwargs={"schema_dict": {}})
