"""
   Lumeer

   Copyright (C) since 2016 the original author or authors.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import requests

BASE_URL = "http://localhost:8080/lumeer-engine/rest/"
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


def create_organization(organization_json):
    return requests.post(BASE_URL + "organizations/", data=open(organization_json), headers=HEADERS)


def create_project(organization_code, project_json):
    return requests.post(BASE_URL + organization_code + "/projects/", data=open(project_json), headers=HEADERS)
