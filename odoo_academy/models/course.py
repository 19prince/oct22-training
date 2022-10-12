# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model): 
    
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(strings='Description')
    
    level = fields.Selection(string='Level',
                            selection=[('beginner', 'Beginner'),
                                      ('intermediate', 'Intermediate'),
                                      ('advanced', 'Advanced')],
                             copy=Fasle)
    
    active = fields.Boolean(string='Active', default=True)