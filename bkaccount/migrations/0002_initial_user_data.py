# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa


from django.db import migrations
from django.conf import settings
from django.contrib.auth import get_user_model


def initial_user_data(apps, schema_editor):
    try:
        user_model = get_user_model()
        user_model.objects.create_superuser(settings.USERNAME, settings.PASSWORD)
    except Exception as e:
        print(e)
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('bkaccount', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_user_data),
    ]
