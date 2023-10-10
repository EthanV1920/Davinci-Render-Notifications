#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Recognize markers and create render jobs based on them.
"""
import configparser
import json
import time
import logging
import requests
import os

from python_get_resolve import GetResolve
# import python_get_resolve
FORMAT = '%(asctime)s - %(module)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=os.path.expanduser(
    '~/Documents/Projects/GBCOMMS-UPDATE/davinci_render_log.log'), format=FORMAT, level=logging.INFO)

# Set up resolve objects
resolve = GetResolve()
if resolve == None: 
    logging.warning("DaVinci is not running...exiting script")
else:
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    timeline = project.GetCurrentTimeline()
    config = configparser.RawConfigParser()

    config.read(os.path.expanduser(
        '~/Documents/Projects/GBCOMMS-UPDATE/config.ini'))

    # Set up variables
    render_que = project.GetRenderJobList()
    completed_job = ""
    completion_status = ""
    completion_percentage = 0
    time_remaining = 0

    wait_time = int(config.get("PROD", "wait_time"))
    computer_number = int(config.get("PROD", "computer_number"))
    check_time = int(config.get("PROD", "check_time"))

    logging.info(
        'DaVinci is running...configuration parameters set. Congrats!')


# Define Webhook URL and Data
def notification_post():
    webhook_url = 'https://maker.ifttt.com/trigger/renderCompleteChart/json/with/key/Pan1YZZ1scxxWRC8WvCMb?'

    response_data = {
        "name":             completed_job,
        "status":           completion_status,
        "percentage":       completion_percentage,
        "mac_number":       computer_number,
        "time_remaining":   time_remaining
    }

    return requests.post(webhook_url, data=response_data)

# Render status given job id number


def job_status(job_id_number):
    return project.GetRenderJobStatus(render_que[job_id_number]["JobId"])["JobStatus"]

def information_update(i):
    logging.info(job_status(i))
    global completed_job
    completed_job = ((render_que[i]["OutputFilename"]).split(".")[0])
    logging.info(completed_job)
    global completion_status
    completion_status = job_status(i)
    logging.info(completion_status)
    global completion_percentage
    completion_percentage = project.GetRenderJobStatus(render_que[i]["JobId"])["CompletionPercentage"]
    logging.info(completion_percentage)
    global time_remaining
    if "EstimatedTimeRemainingInMs" in project.GetRenderJobStatus(render_que[i]["JobId"]):
        time_remaining = project.GetRenderJobStatus(render_que[i]["JobId"])["EstimatedTimeRemainingInMs"]
    
    # logging.info(time_remaining)
    notification_post()

#TODO change render_que to render_queue
def main():
    for i in range(len(render_que)):

        while job_status(i) != "Complete" and job_status(i) != "Failed":
            time.sleep(wait_time)
            information_update(i)
        
            if job_status(i) == "Cancelled":
                logging.info(job_status(i))
                break

        if job_status(i) == "Complete":
           information_update(i)

        elif job_status(i) == "Failed":
            information_update(i)
        else:
            logging.info(job_status(i))


if __name__ == "__main__":
    # Program start
    if resolve == None:
        logging.info("No rendering currently in progress, trying again in 1 minute")
    else:
        if project.IsRenderingInProgress():
            logging.info("Rendering...")
            main()
