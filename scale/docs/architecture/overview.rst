
.. _architecture_overview:

Overview
========================================================================================================================

.. image:: ../_static/images/architecture/overview.png

.. |br| raw:: html

    <br />

The Scale system is comprised of several major pieces:

**Docker Registry** |br|
The Docker registry contains the images for each job type that can be run.

**Mesos Slaves** |br|
Each Mesos slave is a separate node (machine) that registers itself with the Mesos master in order to receive tasking to
run jobs. When a node runs a job, it grabs the appropriate image for the job's type from the Docker registry and
performs a Docker run command to execute the job.

**Mesos Master** |br|
The Mesos master keeps track of all nodes (including their available resources) in the cluster and all jobs that have
been scheduled on the nodes. When the master has available resources in the cluster, it offers these resources to the
Scale scheduler.

**Scale Scheduler** |br|
When the Scale scheduler receives resource offers from the Mesos master, it queries the database to determine the next
job(s) that are available on the queue and able to run within the given resources. The scheduler passes the necessary
information back to the Mesos master so the master can schedule the jobs on the available nodes.

**Scale Database** |br|
The Scale database is a PostGIS (PostgreSQL with the PostGIS extension) relational database that contains the job and
recipe status and history, meta-data for all source and product files, configuration data for all workspaces, triggers,
and ingest processes, and all historical metrics generated by Scale.

**Scale Web Server** |br|
The Scale web server provides the RESTful HTTP API and web front-end to any external clients/browsers. The web server
grabs data from both the Scale database and the Mesos RESTful HTTP API provided by the master.