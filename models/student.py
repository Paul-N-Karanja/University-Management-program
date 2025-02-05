from cloudinit.config.cc_spacewalk import required_packages
from odoo import api, models, fields
from pkg_resources import require


class UniversityStudent(models.Model):
    _name = "university.student"
    _description = "Student Model"

    firstName=fields.Char(string="First Name",required=True)
    surname = fields.Char(string="Surname", required=True)
    intake_year=fields.Integer(string="Year Joined",required=True)
    intake_semester=fields.Float(string="Semester Joined",required=True)
    course=fields.Char(string="Course",required=True)
    unitSelection=fields.Selection([("digitalLogic","Digital Logic"),
                                    ("calculus","Calculus"),
                                    ("DS","Discrete Structures"),
                                    ("ICP","Introduction to Computer Programming"),
                                    ("ICS","Introduction to Computer Systems"),
                                    ("CWS","Communication and Writing Skills"),
                                    ("HW","Health and Wellness"),
                                    ("ANN","Artificial Neural Networks"),
                                    ("ES","Environmental Sustainability"),
                                    ("PFA","Principles of Financial Accounting I ")],
                                   string="Unit Selection",)

