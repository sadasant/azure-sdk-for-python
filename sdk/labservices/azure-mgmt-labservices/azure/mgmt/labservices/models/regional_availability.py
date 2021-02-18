# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RegionalAvailability(Model):
    """The availability information of sizes across regions.

    :param region: Corresponding region
    :type region: str
    :param size_availabilities: List of all the size information for the
     region
    :type size_availabilities:
     list[~azure.mgmt.labservices.models.SizeAvailability]
    """

    _attribute_map = {
        'region': {'key': 'region', 'type': 'str'},
        'size_availabilities': {'key': 'sizeAvailabilities', 'type': '[SizeAvailability]'},
    }

    def __init__(self, **kwargs):
        super(RegionalAvailability, self).__init__(**kwargs)
        self.region = kwargs.get('region', None)
        self.size_availabilities = kwargs.get('size_availabilities', None)