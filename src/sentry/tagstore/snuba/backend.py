"""
sentry.tagstore.snuba.backend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2018 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from __future__ import absolute_import

from sentry.tagstore import TagKeyStatus
from sentry.tagstore.base import TagStorage


class SnubaTagStorage(TagStorage):

    # Tag keys and values
    def get_tag_key(self, project_id, environment_id, key, status=TagKeyStatus.VISIBLE):
        pass

    def get_tag_keys(self, project_id, environment_id, status=TagKeyStatus.VISIBLE):
        pass

    def get_tag_value(self, project_id, environment_id, key, value):
        pass

    def get_tag_values(self, project_id, environment_id, key):
        pass

    def get_group_tag_key(self, project_id, group_id, environment_id, key):
        pass

    def get_group_tag_keys(self, project_id, group_id, environment_id, limit=None):
        pass

    def get_group_tag_value(self, project_id, group_id, environment_id, key, value):
        pass

    def get_group_tag_values(self, project_id, group_id, environment_id, key):
        pass

    def get_group_list_tag_value(self, project_id, group_id_list, environment_id, key, value):
        pass

    def get_group_tag_value_count(self, project_id, group_id, environment_id, key):
        pass

    def get_group_tag_values_for_users(self, event_users, limit=100):
        pass

    def get_top_group_tag_values(self, project_id, group_id, environment_id, key, limit=3):
        pass

    # Releases
    def get_first_release(self, project_id, group_id):
        pass

    def get_last_release(self, project_id, group_id):
        pass

    def get_release_tags(self, project_ids, environment_id, versions):
        pass

    def get_group_event_ids(self, project_id, group_id, environment_id, tags):
        pass

    def get_group_ids_for_users(self, project_ids, event_users, limit=100):
        pass

    def get_groups_user_counts(self, project_id, group_ids, environment_id):
        pass
