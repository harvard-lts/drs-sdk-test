#!/usr/bin/env python
# coding: utf-8

from libnova.common.api import File
from libnova.common.nuclio.Request import Request
from libnova.common.api.JobMessage import JobMessageType


def handler(context, event):
    context.logger.info(event.body.decode("utf-8"))
    request_helper = Request(context, event)

    request_helper.job_init()

    fids = request_helper.JSONData['function_data']['files']['ids']
    request_helper.log(
            f"The following objects will be pushed to ArchiveSpace: {fids}",
            JobMessageType.INFO)

    for fid in fids:
        File.set_metadata(
                fid,
                '{"metadata": [{"iecode": "relation", "value": '
                f'"aspace:{fid}"' '}]}')

    request_helper.job_end(True)
