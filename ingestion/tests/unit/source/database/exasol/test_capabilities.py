#  Copyright 2026 Collate
#  Licensed under the Collate Community License, Version 1.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  https://github.com/open-metadata/OpenMetadata/blob/main/ingestion/LICENSE
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""The Exasol connection declares the agents and features the connector backs.

OMD's UI offers an agent for a service only when the connection's schema declares the
matching ``supports*`` flag, so a missing flag hides an agent the connector supports.
"""

import pytest

from metadata.generated.schema.entity.services.connections.database.exasolConnection import (
    ExasolConnection as ExasolConnectionConfig,
)


def _config() -> ExasolConnectionConfig:
    return ExasolConnectionConfig(
        username="admin",
        password="password",
        hostPort="localhost:8563",
    )


@pytest.mark.parametrize(
    "flag",
    [
        "supportsMetadataExtraction",
        "supportsUsageExtraction",
        "supportsLineageExtraction",
        "supportsDBTExtraction",
        "supportsProfiler",
        "supportsQueryComment",
    ],
)
def test_supported_capability_is_enabled(flag):
    assert getattr(_config(), flag).root is True


def test_system_profile_flag_is_declared():
    assert hasattr(_config(), "supportsSystemProfile")


@pytest.mark.parametrize("flag", ["supportsDataDiff", "supportsColumnAccess", "supportsMaskedAccess"])
def test_unsupported_capability_is_not_declared(flag):
    assert not hasattr(_config(), flag)
