from email.policy import default

from odoo import models,api,fields

class StudentRecord(models.Model):
    _name = "student.record"
    _description = "Holds student information records"
    _inherit =["mail.thread"]

    name = fields.Char(string="Student")
    first_name=fields.Char(string="First Name",required=True, tracking=True)
    last_name=fields.Char(string="Last Name",required=True, tracking=True)
    admission_number=fields.Char(string="Admission Number",required=True, tracking=True)
    email = fields.Char(string="Email Address", tracking=True)
    admission_date=fields.Date(string="Admission date", tracking=True)
    faculty=fields.Selection([("agriculture","Agriculture"),
                              ("art_and_social_sciences","Art And Social Sciences"),
                              ("architecture_and_construction","Architecture And Construction"),
                              ("business_and_finance", "Business And Finance"),
                              ("education","Education"),
                              ("engineering","Engineering"),
                              ("law","Law"),
                              ("technology","Technology"),
                              ],
                            string="Faculty", tracking=True)
    course=fields.Selection([("food_science","Food Science"),("animal_science","Animal Science"),("agricultural_economics","Agricultural Economics"),
                             ("philosophy_and_religious_studies","Philosophy And Religious Studies"),("diplomacy_and_international_studies","Diplomacy And International Studies"),("political_science_and_public_administration","Political Science And Public Administration"),
                             ("architecture","Architecture And Interior Design"),("urban_planning","Urban And Regional Planning"),("real_estate","Real Estate, Construction Management And Quantity Surveying"),
                             ("business_administration","Business Administration"),("finance_and_accounting","Finance And Accounting"),("economics","Economics"),
                             ("educational_management","Educational Management, Policy and Curriculum Studies"),("physical_education","Physical Education And Sport"),("educational_foundations","Educational Foundations"),
                             ("mechanical_engineering","Mechanical Engineering"),("civil_engineering","Civil and Construction Engineering "),("electrical_engineering","Electrical and Information Engineering"),
                             ("law","Law"),
                             ("computer_science","Computer Science"),("business_information_technology","Business Information Technology"),("networks_and_cybersecurity","Computer Networks And Cyber Security")], string="Course", tracking=True)
    currently_enrolled=fields.Boolean(string="Currently enrolled", tracking=True)
    enrollment_date=fields.Date(string="Enrollment Date", tracking=True)
    semester=fields.Selection([("1","1"),
                               ("2","2"),
                               ("3","3"),],
        string="Semester Joining", tracking=True)
