from flask import Blueprint, jsonify, request

from util import constants

from controller import summary_controller

summary_bp = Blueprint('summary', __name__)
controller = summary_controller.SummaryController()

@summary_bp.route('/summarys', methods=['GET'])
def get_all_summaries():
    result = controller.get_all_summarys()
    return jsonify({constants.DATA: result, constants.MSG: constants.SUCCESS})

@summary_bp.route('/summarys/<student_name>', methods=['GET'])
def get_summary_by_student_name(student_name):
    result = controller.get_summary_by_student_name(student_name)
    return jsonify({constants.DATA: result, constants.MSG: constants.SUCCESS})

@summary_bp.route('/summarys', methods=['POST'])
def save_summary():
    summary_data = request.get_json()
    result = controller.save_summary(summary_data)
    return jsonify({constants.DATA: result, constants.MSG: constants.SUCCESS})

@summary_bp.route('/summarys', methods=['DELETE'])
def delete_summary():
    data = request.get_json()
    value = data.get('id')
    result = controller.delete_summary(value)
    return jsonify({constants.DATA: result, constants.MSG: constants.SUCCESS})

@summary_bp.route('/summarys/writeAComment.do', methods=['POST'])
def write_comment():
    summarys = request.get_json()
    if summarys:
        result = controller.writer_comment(summarys)
        return jsonify({constants.DATA: result, constants.MSG: constants.SUCCESS})
    else:
        return jsonify({constants.DATA: None, constants.MSG: constants.ERROR})