"""Defines the methods for handling file systems in the job execution's local container volume"""
from __future__ import unicode_literals

import os

from storage.container import SCALE_ROOT_PATH


SCALE_JOB_EXE_INPUT_PATH = os.path.join(SCALE_ROOT_PATH, 'input_data')
SCALE_JOB_EXE_OUTPUT_PATH = os.path.join(SCALE_ROOT_PATH, 'output_data')


def get_job_exe_input_vol_name(framework_id, job_exe_id):
    """Returns the container input volume name for the given job execution ID

    :param framework_id: The scheduling framework ID
    :type framework_id: string
    :param job_exe_id: The job execution ID
    :type job_exe_id: int
    :returns: The container input volume name
    :rtype: string
    """

    return 'scale_%s_%s_input_data' % (framework_id, job_exe_id)


def get_job_exe_output_vol_name(framework_id, job_exe_id):
    """Returns the container output volume name for the given job execution ID

    :param framework_id: The scheduling framework ID
    :type framework_id: string
    :param job_exe_id: The job execution ID
    :type job_exe_id: int
    :returns: The container output volume name
    :rtype: string
    """

    return 'scale_%s_%s_output_data' % (framework_id, job_exe_id)


def get_workspace_volume_name(framework_id, job_exe_id, workspace):
    """Returns the name of the workspace's container volume for the given job execution ID

    :param framework_id: The scheduling framework ID
    :type framework_id: string
    :param job_exe_id: The job execution ID
    :type job_exe_id: int
    :param workspace: The name of the workspace
    :type workspace: string
    :returns: The workspace's container volume name
    :rtype: string
    """

    return 'scale_%s_%s_wksp_%s' % (framework_id, job_exe_id, workspace)
