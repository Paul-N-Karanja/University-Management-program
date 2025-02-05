# -*- coding: utf-8 -*-
# from odoo import http


# class UniversityManagementProgram/(http.Controller):
#     @http.route('/university_management_program//university_management_program/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/university_management_program//university_management_program//objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('university_management_program/.listing', {
#             'root': '/university_management_program//university_management_program/',
#             'objects': http.request.env['university_management_program/.university_management_program/'].search([]),
#         })

#     @http.route('/university_management_program//university_management_program//objects/<model("university_management_program/.university_management_program/"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('university_management_program/.object', {
#             'object': obj
#         })

