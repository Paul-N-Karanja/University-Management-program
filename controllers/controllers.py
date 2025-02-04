# -*- coding: utf-8 -*-
# from odoo import http


# class UniversityManagement(http.Controller):
#     @http.route('/university_management/university_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/university_management/university_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('university_management.listing', {
#             'root': '/university_management/university_management',
#             'objects': http.request.env['university_management.university_management'].search([]),
#         })

#     @http.route('/university_management/university_management/objects/<model("university_management.university_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('university_management.object', {
#             'object': obj
#         })

