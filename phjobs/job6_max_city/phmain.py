# -*- coding: utf-8 -*-
"""alfredyang@pharbers.com.

This is job template for Pharbers Max Job
"""
from phjob import execute
import click


@click.command()
@click.option('--owner')
@click.option('--run_id')
@click.option('--job_id')
@click.option('--max_path')
@click.option('--project_name')
@click.option('--time_left')
@click.option('--time_right')
@click.option('--left_models')
@click.option('--left_models_time_left')
@click.option('--right_models')
@click.option('--right_models_time_right')
@click.option('--all_models')
@click.option('--if_others')
@click.option('--out_path')
@click.option('--out_dir')
@click.option('--need_test')
@click.option('--minimum_product_columns')
@click.option('--minimum_product_sep')
@click.option('--minimum_product_newname')
@click.option('--if_two_source')
@click.option('--bedsize')
@click.option('--hospital_level')
@click.option('--id_bedsize_path')
@click.option('--a')
@click.option('--b')
def debug_execute(owner, run_id, job_id, a, b, max_path, project_name, time_left, time_right, left_models, left_models_time_left, right_models, right_models_time_right,
all_models, if_others, out_path, out_dir, need_test, minimum_product_columns, minimum_product_sep, minimum_product_newname, 
if_two_source, bedsize, hospital_level, id_bedsize_path):
	execute(max_path, project_name, time_left, time_right, left_models, left_models_time_left, right_models, right_models_time_right,
all_models, if_others, out_path, out_dir, need_test, minimum_product_columns, minimum_product_sep, minimum_product_newname, 
if_two_source, bedsize, hospital_level, id_bedsize_path)


if __name__ == '__main__':
    debug_execute()

