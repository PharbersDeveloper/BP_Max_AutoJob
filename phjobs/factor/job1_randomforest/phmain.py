# -*- coding: utf-8 -*-
"""alfredyang@pharbers.com.

This is job template for Pharbers Max Job
"""
import click
import traceback
from phjob import execute
from ph_logs.ph_logs import phs3logger
from ph_max_auto.ph_hook.ph_hook import exec_before, exec_after


@click.command()
@click.option('--owner')
@click.option('--job_id')
@click.option('--run_id')
@click.option('--max_path')
@click.option('--project_name')
@click.option('--outdir')
@click.option('--model_month_right')
@click.option('--model_month_left')
@click.option('--all_models')
@click.option('--universe_choice')
@click.option('--rf_ntree')
@click.option('--rf_minnode')
@click.option('--c')
@click.option('--d')
def debug_execute(**kwargs):
    try:
        args = {'name': 'job1_randomforest'}

        args.update(kwargs)
        result = exec_before(**args)

        args.update(result)
        result = execute(**args)

        args.update(result)
        result = exec_after(outputs=[], **args)

        return result
    except Exception as e:
        logger = phs3logger(kwargs["job_id"])
        logger.error(traceback.format_exc())
        raise e


if __name__ == '__main__':
    debug_execute()


